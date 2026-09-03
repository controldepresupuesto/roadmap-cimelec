# -*- coding: utf-8 -*-
"""
Inyecta los datos REALES del tablero en los dos artboards, en el marcador /*__DATOS__*/.

No se transcribe nada a mano: la lista sale de `gh issue list` (roadmap.json) y las 58
solicitudes se serializan tal cual. Correr de nuevo cada vez que cambie el tablero.
"""

import datetime
import io
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

AQUI = os.path.dirname(os.path.abspath(__file__))
FUENTE = os.path.join(AQUI, "roadmap.json")

# El color de cada app es el de su etiqueta en el repositorio: es su identidad, no una eleccion nueva.
APPS = [
    ("horarios",   "Registro de Horarios",  "Horarios",    "#9C36B5"),
    ("proveedores","Portal de Proveedores", "Proveedores", "#5F3DC4"),
    ("datamart",   "Tablero DataMart",      "DataMart",    "#1864AB"),
    ("plataforma", "Plataforma",            "Plataforma",  "#C2255C"),
    ("geo",        "Consulta Geográfica",   "Geo",         "#5C940D"),
    ("bitacora",   "Bitácora de Obra",      "Bitácora",    "#E8590C"),
    ("proyectos",  "Gestión de Proyectos",  "Proyectos",   "#0C8599"),
    ("asistente",  "Asistente",             "Asistente",   "#2F9E44"),
    ("menu",       "Menú de entrada",       "Menú",        "#495057"),
    ("biblioteca", "Biblioteca de Informes","Biblioteca",  "#099268"),
]

# Orden y tintes de estado: el MISMO orden del tablero (evaluacion -> publicado). Los tintes son
# los de `.pill` de la app de Horarios, que ya estan medidos: tinta >= 4.9 sobre su fondo.
ESTADOS = [
    ("en evaluacion",   "En evaluación",   "#ECEEF2", "#5B6472", "#DCE1E9"),
    ("en backlog",      "En backlog",      "#DDECF8", "#1C5D9B", "#C3DBEF"),
    ("en desarrollo",   "En desarrollo",   "#CFE4F5", "#14507F", "#B3D3EC"),
    ("en pruebas",      "En pruebas",      "#F6E8D2", "#8A5A00", "#E8D3AE"),
    ("en implementacion","En implementación","#FAF0D6","#7a5600", "#EBDCB4"),
    ("publicado",       "Publicado",       "#DFEEE2", "#3f5a1e", "#C7E0CE"),
    ("pausado",         "Pausado",         "#EFEAE1", "#7a5600", "#E0D6C4"),
    ("no va",           "No va",           "#ECEEF2", "#6E7781", "#DCE1E9"),
]

TIPOS = [
    ("nuevo",  "Nuevo",  "#3f5a1e"),
    ("mejora", "Mejora", "#1C5D9B"),
    ("error",  "Error",  "#B42318"),
    ("idea",   "Idea",   "#7a5600"),
]

NOMBRE = {a[0]: a[1] for a in APPS}


def limpiar(titulo, app):
    t = re.sub(r"^\[[^\]]+\]\s*", "", titulo).strip()
    pre = NOMBRE.get(app, "") + ": "
    if t.startswith(pre):
        t = t[len(pre):]
    return t[:1].upper() + t[1:]


def js(v):
    return json.dumps(v, ensure_ascii=False)


def main():
    d = json.load(io.open(FUENTE, encoding="utf-8"))
    items = []
    for i in d:
        et = [l["name"] for l in i["labels"]]
        app = next((n[5:] for n in et if n.startswith("app: ")), None)
        est = next((n[8:] for n in et if n.startswith("estado: ")), None)
        tip = next((n[6:] for n in et if n.startswith("tipo: ")), None)
        if not (app and est and tip):
            print("  OJO: #%s sin etiquetas completas, fuera" % i["number"])
            continue
        items.append({"n": i["number"], "t": limpiar(i["title"], app), "a": app, "e": est, "k": tip})
    items.sort(key=lambda x: -x["n"])

    orden_app = sorted(APPS, key=lambda a: -len([1 for i in items if i["a"] == a[0]]))

    L = []
    L.append("const APPS = [")
    for a in orden_app:
        L.append("  { id: %s, nom: %s, corto: %s, col: %s }," % (js(a[0]), js(a[1]), js(a[2]), js(a[3])))
    L.append("];")
    L.append("const APP = {}; APPS.forEach((a) => { APP[a.id] = a; });")
    L.append("const APP_ORD = {}; APPS.forEach((a, k) => { APP_ORD[a.id] = k; });")
    L.append("")
    L.append("const ESTADOS = [")
    for e in ESTADOS:
        L.append("  { id: %s, nom: %s, bg: %s, ink: %s, borde: %s }," %
                 (js(e[0]), js(e[1]), js(e[2]), js(e[3]), js(e[4])))
    L.append("];")
    L.append("const EST = {}; ESTADOS.forEach((e) => { EST[e.id] = e; });")
    L.append("const EST_ORD = {}; ESTADOS.forEach((e, k) => { EST_ORD[e.id] = k; });")
    L.append("")
    L.append("const TIP = {")
    for t in TIPOS:
        L.append("  %s: { nom: %s, col: %s }," % (t[0], js(t[1]), js(t[2])))
    L.append("};")
    L.append("")
    MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
             "septiembre", "octubre", "noviembre", "diciembre"]
    hoy = datetime.date.today()
    L.append("// La fecha es la de esta inyeccion: la pagina no la escribe a mano.")
    L.append("const FECHA = %s;" % js("%d de %s de %d" % (hoy.day, MESES[hoy.month - 1], hoy.year)))
    L.append("")
    L.append("// Las %d solicitudes del tablero, tal como las devuelve el repositorio." % len(items))
    L.append("const ITEMS = [")
    for i in items:
        L.append("  { n: %d, t: %s, a: %s, e: %s, k: %s }," %
                 (i["n"], js(i["t"]), js(i["a"]), js(i["e"]), js(i["k"])))
    L.append("];")
    bloque = "\n".join(L)

    for f in ("Main.dc.html", "Movil.dc.html"):
        p = os.path.join(AQUI, f)
        t = io.open(p, encoding="utf-8").read()
        if "/*__DATOS__*/" in t:
            t = t.replace("/*__DATOS__*/", bloque)
        else:
            t = re.sub(r"const APPS = \[.*?\nconst ITEMS = \[.*?\n\];", bloque, t, flags=re.S)
        io.open(p, "w", encoding="utf-8", newline="\n").write(t)
        print("  %s  <-  %d solicitudes" % (f, len(items)))

    est = {}
    for i in items:
        est[i["e"]] = est.get(i["e"], 0) + 1
    print("  %s" % est)
    return 0


if __name__ == "__main__":
    sys.exit(main())
