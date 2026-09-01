# -*- coding: utf-8 -*-
"""
Lee los commits de los repositorios de trabajo y redacta CANDIDATOS para el roadmap.

Por que asi y no con un hook de la sesion: el registro de lo que se hizo ya existe y es el
historial de git. Es mas fiable que cualquier captura al vuelo — no depende de que una sesion
termine bien, funciona hacia atras, y lo escribio quien hizo el trabajo.

Este script NO PUBLICA NADA. Deja una lista en _PROPUESTAS-ROADMAP.md para que una persona
decida cual entra al roadmap publico y cual no. Ese es el punto: capturar es lo que se olvida,
revisar son treinta segundos.

Solo lectura sobre GitHub. Guarda su marca de avance en _ultimo-commit-visto.json.
"""

import io
import json
import os
import re
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DUENO = "controldepresupuesto"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARCA = os.path.join(RAIZ, "_ultimo-commit-visto.json")
SALIDA = os.path.join(RAIZ, "_PROPUESTAS-ROADMAP.md")

# repositorio -> etiqueta de app del roadmap
REPOS = {
    "app-horarios":    "app: horarios",
    "bitacora-obra":   "app: bitacora",
    "api-geo-bogota":  "app: geo",
    "web-proveedores": "app: proveedores",
    "robot-sinco":     "app: proveedores",
    "datamart-motor":  "app: datamart",
    "datamart-api":    "app: datamart",
    "app-proyectos":   "app: proyectos",
    "bot-whatsapp":    "app: asistente",
}

# Tres cajones. Nada se descarta: se separa, para que la persona mire poco y decida rapido.
#
# NUNCA: infraestructura, pruebas, credenciales, despliegue. La regla escrita del repositorio
# publico prohibe exactamente esto, asi que ni siquiera merece revisarse.
NUNCA = re.compile(
    r"\b(ci|cd|runner|workflow|pipeline|docker|contenedor|nginx|postgres|postgis|vm|servidor|"
    r"backup|respaldo|llave|token|secreto|credencial|clave|ssh|deploy|dns|certificad|"
    r"seccomp|cron|systemd|firewall|puerto)\b|"
    r"\.(py|bat|sh|yml|yaml|json|ini|ps1|md)\b|"
    r"prueba|pruebas|suite|cobertura|banco de pruebas|refactor|linter|"
    r"ingesta|migracion de ambientes|base de datos|repositorio|rama\b|commit",
    re.IGNORECASE)

# RUIDO: no es infraestructura, pero tampoco es noticia — bitacoras, notas, versiones.
RUIDO = re.compile(
    r"desplegad|despliegue|^traspaso|^anota|^documenta|^deja |^precisa|^sube la version|"
    r"guardar|leeme|readme|^poner al dia el mapa|^foto de los cambios|"
    r"^cierra la (sesion|jornada)|^segunda ronda|^bitacora:|^cerrar el mapa|"
    r"^dejar el|^lo que el repositorio",
    re.IGNORECASE)


def gh(args):
    r = subprocess.run(["gh"] + args, capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "").strip()[:250])
    return r.stdout


def cargar_marca():
    if os.path.exists(MARCA):
        try:
            return json.load(io.open(MARCA, encoding="utf-8"))
        except Exception:
            pass
    return {}


def main():
    desde = "--desde" in sys.argv
    fecha_desde = None
    if desde:
        i = sys.argv.index("--desde")
        if i + 1 < len(sys.argv):
            fecha_desde = sys.argv[i + 1]

    marca = cargar_marca()
    nueva_marca = dict(marca)

    titulos_existentes = set()
    try:
        for iss in json.loads(gh(["issue", "list", "--repo", "%s/roadmap-cimelec" % DUENO,
                                  "--state", "all", "--limit", "300", "--json", "title"])):
            titulos_existentes.add(iss["title"].lower())
    except RuntimeError:
        pass

    noticias = []
    ruido = []
    nunca = []

    for repo, etiqueta in REPOS.items():
        ruta = "repos/%s/%s/commits?per_page=100" % (DUENO, repo)
        if fecha_desde:
            ruta += "&since=%sT00:00:00Z" % fecha_desde
        try:
            commits = json.loads(gh(["api", ruta]))
        except RuntimeError:
            continue
        if not commits:
            continue

        visto = marca.get(repo)
        nueva_marca[repo] = commits[0]["sha"]

        for c in commits:
            if visto and c["sha"] == visto:
                break
            msg = (c["commit"]["message"] or "").split("\n")[0].strip()
            if not msg:
                continue
            fila = {
                "repo": repo, "etiqueta": etiqueta,
                "fecha": c["commit"]["author"]["date"][:10],
                "msg": msg, "sha": c["sha"][:7],
            }
            if NUNCA.search(msg):
                nunca.append(fila)
            elif RUIDO.search(msg):
                ruido.append(fila)
            else:
                noticias.append(fila)

    # ─────────────────────────────── el informe ───────────────────────────────
    lineas = []
    lineas.append("# Candidatos para el roadmap")
    lineas.append("")
    lineas.append("Sale del historial de los repositorios. **Nada de esto está publicado.**")
    lineas.append("Marca lo que quieras que entre y dímelo; lo redacto en lenguaje de negocio")
    lineas.append("y lo cargo. Lo que no marques, se queda aquí.")
    lineas.append("")
    lineas.append("Recuerda la regla del repositorio público: **cero infraestructura y cero")
    lineas.append("deuda técnica interna**. Varias de estas líneas no deben salir nunca.")
    lineas.append("")

    if not noticias and not ruido and not nunca:
        lineas.append("Sin cambios nuevos desde la última revisión.")
    else:
        if noticias:
            lineas.append("## Probablemente sí son noticia (%d)" % len(noticias))
            lineas.append("")
            por_app = {}
            for f in noticias:
                por_app.setdefault(f["etiqueta"], []).append(f)
            for etq in sorted(por_app):
                lineas.append("### `%s`" % etq)
                lineas.append("")
                for f in sorted(por_app[etq], key=lambda x: x["fecha"], reverse=True):
                    ya = "  ← ya parece estar en el roadmap" if f["msg"].lower() in titulos_existentes else ""
                    lineas.append("- [ ] `%s` %s%s" % (f["fecha"], f["msg"], ya))
                lineas.append("")
        if ruido:
            lineas.append("## Probablemente NO (despliegues, notas, documentación) (%d)" % len(ruido))
            lineas.append("")
            for f in sorted(ruido, key=lambda x: x["fecha"], reverse=True)[:40]:
                lineas.append("- `%s` %s · %s" % (f["fecha"], f["msg"][:88], f["repo"]))
            if len(ruido) > 40:
                lineas.append("- … y %d más" % (len(ruido) - 40))
            lineas.append("")
        if nunca:
            lineas.append("## Nunca: infraestructura, pruebas, credenciales (%d)" % len(nunca))
            lineas.append("")
            lineas.append("No se listan. La regla del repositorio público las excluye por definición;")
            lineas.append("aparecen aquí solo como conteo, para que sepas que se miraron y se dejaron fuera.")
            lineas.append("")

    io.open(SALIDA, "w", encoding="utf-8", newline="\r\n").write("\n".join(lineas) + "\n")
    io.open(MARCA, "w", encoding="utf-8", newline="\n").write(
        json.dumps(nueva_marca, indent=2, ensure_ascii=False))

    print()
    print("  %d candidatos y %d probables descartes" % (len(noticias), len(ruido)))
    print("  %s" % SALIDA)
    print()
    return len(noticias)


if __name__ == "__main__":
    try:
        n = main()
        sys.exit(1 if n else 0)   # 1 = hay algo por revisar
    except RuntimeError as e:
        print("  FALLO: %s" % e)
        sys.exit(2)
