# -*- coding: utf-8 -*-
"""
Vigila que el vocabulario de etiquetas no se degrade, y falla RUIDOSAMENTE si se degrado.

Por que existe: en el roadmap publico de Sincosoft hay 95 etiquetas distintas, con la misma
idea escrita de tres formas ('IA', 'Inteligencia Artificial') y errores de dedo publicados
('Odenes de trabajo'). Ahi es un problema cosmetico. Aqui seria grave: las etiquetas SON la
fuente de verdad del tablero, asi que una etiqueta mal escrita es una solicitud que el
sincronizador ignora en silencio y que nunca aparece en el tablero.

No corrige nada: reporta y sale con codigo distinto de cero, para que la corrida de Actions
quede en rojo y llegue el correo.

Solo lectura. No escribe nada en GitHub.
"""

import json
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, __file__.rsplit("\\", 1)[0].rsplit("/", 1)[0])
from sincronizar_tablero import MAPA, REPO  # noqa: E402  el vocabulario vive en un solo sitio

# Familias que gobernamos. Toda etiqueta con estos prefijos tiene que estar en el MAPA
# (o, para 'tema:', simplemente existir: los temas son libres y no alimentan ningun campo).
FAMILIAS_GOBERNADAS = {
    "estado: ": "Status",
    "app: ": "Herramienta",
    "prioridad: ": "Prioridad",
}
FAMILIAS_LIBRES = ("tema: ", "tipo: ")


def gh(args):
    r = subprocess.run(["gh"] + args, capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "").strip())
    return r.stdout


def main():
    print()
    print("  Auditando el vocabulario de etiquetas de %s" % REPO)
    print()

    definidas = {l["name"] for l in json.loads(
        gh(["label", "list", "--repo", REPO, "--limit", "200", "--json", "name"]))}
    issues = json.loads(gh(["issue", "list", "--repo", REPO, "--state", "all",
                            "--limit", "500", "--json", "number,title,labels,state"]))

    problemas = []
    avisos = []

    # ---- 1. etiquetas definidas en el repo que el MAPA no conoce (el caso del error de dedo)
    for prefijo, campo in FAMILIAS_GOBERNADAS.items():
        conocidas = set(MAPA[campo].keys())
        for nombre in sorted(definidas):
            if nombre.startswith(prefijo) and nombre not in conocidas:
                problemas.append(
                    "La etiqueta '%s' existe en el repositorio pero el sincronizador no la "
                    "conoce. O es un error de dedo, o hay que agregarla al MAPA de "
                    "sincronizar_tablero.py y la opcion al campo %s del tablero."
                    % (nombre, campo))

    # ---- 2. lo contrario: el MAPA espera una etiqueta que no existe
    for prefijo, campo in FAMILIAS_GOBERNADAS.items():
        for nombre in sorted(MAPA[campo].keys()):
            if nombre not in definidas:
                problemas.append(
                    "El sincronizador espera la etiqueta '%s' y no existe en el repositorio. "
                    "Cualquier solicitud que deberia llevarla se va a quedar sin %s."
                    % (nombre, campo))

    # ---- 3. cada solicitud: una y solo una de cada familia gobernada
    for iss in issues:
        n = iss["number"]
        nombres = [l["name"] for l in iss["labels"]]
        for prefijo, campo in FAMILIAS_GOBERNADAS.items():
            puestas = [x for x in nombres if x.startswith(prefijo)]
            if len(puestas) > 1:
                problemas.append(
                    "#%d tiene %d etiquetas '%s': %s. El sincronizador toma la primera que "
                    "encuentra, asi que el tablero va a mostrar algo arbitrario."
                    % (n, len(puestas), prefijo.strip(), ", ".join(sorted(puestas))))
            elif not puestas:
                # 'prioridad:' ausente es tolerable; 'estado:' y 'app:' no.
                if prefijo == "prioridad: ":
                    avisos.append("#%d no tiene prioridad todavia" % n)
                else:
                    problemas.append(
                        "#%d no tiene ninguna etiqueta '%s'. No va a aparecer en el tablero "
                        "con %s, ni en la pestana de su app." % (n, prefijo.strip(), campo))

    # ---- 4. coherencia entre estado y abierto/cerrado
    for iss in issues:
        n, estado = iss["number"], iss["state"]
        nombres = [l["name"] for l in iss["labels"]]
        terminal = any(x in nombres for x in ("estado: publicado", "estado: no va"))
        if estado == "OPEN" and terminal:
            avisos.append("#%d esta marcada como terminada pero sigue abierta" % n)
        if estado == "CLOSED" and not terminal:
            avisos.append("#%d esta cerrada pero sin un estado terminal "
                          "(publicado o no va), asi que nadie sabe por que se cerro" % n)

    # ---- 5. etiquetas fuera de toda familia conocida
    gobernadas = tuple(FAMILIAS_GOBERNADAS) + FAMILIAS_LIBRES
    sueltas = sorted(x for x in definidas if not x.startswith(gobernadas))
    if sueltas:
        avisos.append("Etiquetas fuera de las familias conocidas: %s" % ", ".join(sueltas))

    # ------------------------------------------------------------------ informe ----
    print("  %d etiquetas definidas · %d solicitudes revisadas" % (len(definidas), len(issues)))
    print()
    if avisos:
        print("  AVISOS (no rompen nada):")
        for a in avisos:
            print("    - %s" % a)
        print()
    if problemas:
        print("  PROBLEMAS (%d):" % len(problemas))
        for p in problemas:
            print("    x %s" % p)
            # anotacion para que salga destacado en la corrida de Actions
            print("::error::%s" % p)
        print()
        return 1

    print("  Vocabulario coherente. Nada que corregir.")
    print()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as e:
        print()
        print("  FALLO: %s" % e)
        print()
        sys.exit(1)
