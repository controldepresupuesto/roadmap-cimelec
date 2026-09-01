# -*- coding: utf-8 -*-
"""
Vigila que el roadmap no se podrida. Un tablero desactualizado es peor que no tener tablero,
porque miente con cara de estar al dia.

Esto es exactamente lo que le falto al roadmap publico de Sincosoft: su campo de trimestre
quedo con el 93,8% de los items vacio y cero periodos activos desde diciembre de 2024, y nadie
se dio cuenta porque nada lo avisaba.

No corrige nada. Reporta y sale con codigo 1 si hay algo que exige accion, para que el
envoltorio muestre el aviso de escritorio.

Solo lectura. Requiere gh con el permiso 'project'.
"""

import datetime
import io
import json
import os
import subprocess
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = "controldepresupuesto/roadmap-cimelec"
DUENO = "controldepresupuesto"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Umbrales
DIAS_ESTANCADO_AVISO = 30      # en desarrollo sin moverse
DIAS_ESTANCADO_ALARMA = 60
DIAS_TABLERO_QUIETO = 45       # el tablero ENTERO sin un solo cambio
HORAS_LATIDO = 3               # la tarea de sincronizacion corre cada 10 minutos
DIAS_CANDADO_AVISO = 60        # el limite de interaccion por vencer
DIAS_TRIMESTRES_MINIMO = 365   # cobertura restante del campo Periodo

HOY = datetime.datetime.now(datetime.timezone.utc)


def gh(args):
    r = subprocess.run(["gh"] + args, capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "").strip()[:300])
    return r.stdout


def gql(consulta):
    f = os.path.join(tempfile.gettempdir(), "gql_vig.graphql")
    io.open(f, "w", encoding="utf-8", newline="\n").write(consulta)
    d = json.loads(gh(["api", "graphql", "-F", "query=@" + f]))
    if "errors" in d:
        raise RuntimeError(json.dumps(d["errors"], ensure_ascii=False)[:300])
    return d["data"]


def dias(iso):
    if not iso:
        return None
    t = datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return (HOY - t).days


def main():
    accion = []    # exige que alguien haga algo
    relojes = []   # avisos con antelacion
    nota = []      # informativo

    # ───────────────────────────── el tablero ─────────────────────────────
    t = gql("""
    query{ user(login:"%s"){ projectV2(number:1){
      title url updatedAt
      fields(first:50){ nodes{
        ... on ProjectV2SingleSelectField { name options{ name } }
        ... on ProjectV2IterationField { name configuration{ iterations{ title startDate duration } } } } }
      items(first:100){ nodes{
        updatedAt
        content{ ... on Issue { number title url state updatedAt labels(first:15){ nodes{ name } } } }
        fieldValues(first:25){ nodes{
          ... on ProjectV2ItemFieldSingleSelectValue { name field{ ... on ProjectV2SingleSelectField { name } } }
          ... on ProjectV2ItemFieldIterationValue { title field{ ... on ProjectV2IterationField { name } } } } } } }
    } } }
    """ % DUENO)["user"]["projectV2"]

    items = []
    for it in t["items"]["nodes"]:
        c = it.get("content") or {}
        if not c.get("number"):
            continue
        campos = {}
        for fv in it["fieldValues"]["nodes"]:
            if fv and fv.get("field"):
                campos[fv["field"]["name"]] = fv.get("name") or fv.get("title")
        items.append({
            "n": c["number"], "titulo": c["title"], "url": c["url"], "abierto": c["state"] == "OPEN",
            "etiquetas": {l["name"] for l in c["labels"]["nodes"]},
            "dias": dias(c.get("updatedAt")), "campos": campos,
        })

    # 1. el tablero entero sin moverse
    d = dias(t.get("updatedAt"))
    if d is not None and d >= DIAS_TABLERO_QUIETO:
        accion.append("El tablero completo lleva %d dias sin un solo cambio. O no se esta "
                      "trabajando, o se esta trabajando y no se esta registrando." % d)
    else:
        nota.append("El tablero se movio hace %d dia(s)." % (d if d is not None else -1))

    # 2. lo que esta en desarrollo y no se mueve
    for i in items:
        if i["campos"].get("Status") == "En desarrollo" and i["dias"] is not None:
            if i["dias"] >= DIAS_ESTANCADO_ALARMA:
                accion.append("#%d lleva %d dias en desarrollo sin moverse. Decide: sigue, "
                              "se pausa, o no va.  %s" % (i["n"], i["dias"], i["url"]))
            elif i["dias"] >= DIAS_ESTANCADO_AVISO:
                relojes.append("#%d lleva %d dias en desarrollo sin moverse." % (i["n"], i["dias"]))

    # 3. en desarrollo sin trimestre: invisible en la Hoja de ruta
    for i in items:
        if i["campos"].get("Status") == "En desarrollo" and not i["campos"].get("Periodo"):
            accion.append("#%d esta en desarrollo SIN trimestre, asi que no se dibuja en la "
                          "Hoja de ruta. Ponle un Periodo.  %s" % (i["n"], i["url"]))

    # 4. estado terminal y el issue todavia abierto (el error que tiene Sincosoft 111 veces)
    for i in items:
        st = i["campos"].get("Status")
        if st in ("Publicado", "No va") and i["abierto"]:
            accion.append("#%d esta marcada como '%s' pero sigue abierta. Cierrala o corrige "
                          "el estado." % (i["n"], st))
        if st not in ("Publicado", "No va") and not i["abierto"]:
            accion.append("#%d esta cerrada con estado '%s': nadie sabe si salio o se "
                          "descarto." % (i["n"], st or "sin estado"))

    # 5. el tablero contra las etiquetas (si alguien edito el tablero a mano)
    mapa_estado = {
        "estado: en evaluacion": "En evaluación", "estado: en backlog": "En backlog",
        "estado: en desarrollo": "En desarrollo", "estado: en pruebas": "En pruebas",
        "estado: en implementacion": "En implementación", "estado: publicado": "Publicado",
        "estado: pausado": "Pausado", "estado: no va": "No va",
    }
    for i in items:
        esperado = next((v for k, v in mapa_estado.items() if k in i["etiquetas"]), None)
        real = i["campos"].get("Status")
        if esperado and real and esperado != real:
            accion.append("#%d: la etiqueta dice '%s' y el tablero dice '%s'. La etiqueta manda; "
                          "alguien edito el tablero a mano." % (i["n"], esperado, real))

    # ─────────────────────── el latido de la sincronizacion ───────────────────────
    latido = os.path.join(RAIZ, "_estado-sincronizacion.txt")
    if not os.path.exists(latido):
        accion.append("No existe _estado-sincronizacion.txt: la tarea automatica nunca ha corrido.")
    else:
        edad = (datetime.datetime.now() -
                datetime.datetime.fromtimestamp(os.path.getmtime(latido)))
        horas = edad.total_seconds() / 3600.0
        if horas >= HORAS_LATIDO:
            accion.append("La sincronizacion automatica no corre desde hace %.0f horas. La tarea "
                          "'Roadmap CIMELEC - Sincronizar tablero' esta caida." % horas)
        else:
            nota.append("La sincronizacion corrio hace %.0f minuto(s)." % (horas * 60))

    # ──────────────────────────── los relojes largos ────────────────────────────
    # el candado de escritura
    try:
        lim = json.loads(gh(["api", "repos/%s/interaction-limits" % REPO]))
        if lim.get("expires_at"):
            quedan = -dias(lim["expires_at"])
            if quedan <= DIAS_CANDADO_AVISO:
                relojes.append("El candado de escritura vence en %d dias (%s). Se renueva "
                               "corriendo scripts/configurar-repo.ps1."
                               % (quedan, lim["expires_at"][:10]))
            else:
                nota.append("Candado de escritura: %d dias por delante." % quedan)
    except RuntimeError:
        relojes.append("No se pudo leer el candado de escritura del repositorio.")

    # los trimestres del campo Periodo
    per = next((f for f in t["fields"]["nodes"] if f and f.get("name") == "Periodo"), None)
    if per:
        its = per["configuration"]["iterations"]
        if not its:
            accion.append("El campo Periodo no tiene ningun trimestre activo. La Hoja de ruta "
                          "no puede dibujar nada. (Es como quedo el de Sincosoft.)")
        else:
            ult = max(its, key=lambda x: x["startDate"])
            fin = (datetime.date.fromisoformat(ult["startDate"])
                   + datetime.timedelta(days=ult["duration"]))
            cobertura = (fin - datetime.date.today()).days
            if cobertura < DIAS_TRIMESTRES_MINIMO:
                relojes.append("Los trimestres del campo Periodo se acaban en %d dias (%s). "
                               "Amplia TRIMESTRES_HASTA en configurar_tablero.py y vuelve a "
                               "correrlo." % (cobertura, fin.isoformat()))
            else:
                nota.append("Trimestres definidos hasta %s (%d dias)." % (fin.isoformat(), cobertura))

    # ─────────────────────────────── el informe ───────────────────────────────
    lineas = []
    lineas.append("VIGILANTE DEL ROADMAP — %s" % HOY.astimezone().strftime("%Y-%m-%d %H:%M"))
    lineas.append("=" * 74)
    lineas.append("")
    lineas.append("%s" % t["url"])
    lineas.append("%d solicitudes en el tablero" % len(items))
    lineas.append("")

    if accion:
        lineas.append("EXIGE ACCION (%d):" % len(accion))
        for a in accion:
            lineas.append("  x %s" % a)
        lineas.append("")
    if relojes:
        lineas.append("RELOJES (avisan con antelacion) (%d):" % len(relojes))
        for r in relojes:
            lineas.append("  ! %s" % r)
        lineas.append("")
    if not accion and not relojes:
        lineas.append("NADA QUE REPORTAR. El roadmap esta al dia.")
        lineas.append("")
    if nota:
        lineas.append("Para referencia:")
        for n in nota:
            lineas.append("  - %s" % n)
        lineas.append("")

    informe = "\n".join(lineas)
    print(informe)
    io.open(os.path.join(RAIZ, "_VIGILANTE-ROADMAP.txt"), "w",
            encoding="utf-8", newline="\r\n").write(informe)

    # Una linea corta para el aviso de escritorio
    if accion:
        resumen = accion[0] if len(accion) == 1 else "%d cosas exigen accion en el roadmap" % len(accion)
    elif relojes:
        resumen = relojes[0]
    else:
        resumen = ""
    io.open(os.path.join(RAIZ, "_VIGILANTE-AVISO.txt"), "w",
            encoding="utf-8", newline="\r\n").write(resumen)

    return 1 if accion else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as e:
        print("FALLO DEL VIGILANTE: %s" % e)
        sys.exit(2)
