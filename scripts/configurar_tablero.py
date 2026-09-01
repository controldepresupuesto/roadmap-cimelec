# -*- coding: utf-8 -*-
"""
Configura el tablero de la hoja de ruta: los estados, el campo de trimestre y las vistas.

Sigue el modelo del roadmap publico de Sincosoft (los autores del ERP SINCO), con dos
diferencias deliberadas:

  1. Ellos no publican lo que se descarta. Aqui si: los estados Pausado y No va existen, y
     la solicitud queda cerrada con el motivo escrito. Una lista donde todo esta "en
     evaluacion" para siempre no genera confianza.
  2. Su campo de trimestre quedo abandonado (la ultima iteracion es 2024 T2). Aqui los
     trimestres se PRE-GENERAN varios anios hacia adelante, que es exactamente el modo de
     falla que se les vio.

Es idempotente: se puede correr las veces que sea.
Requiere: gh con el permiso 'project'.
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

DUENO = "controldepresupuesto"
NUMERO_TABLERO = 1
REPO = "controldepresupuesto/roadmap-cimelec"

SALTO = "\n          "   # solo para que las mutaciones queden legibles al depurarlas

# Los estados, en el orden en que se leen en el tablero.
# 'antes' es el nombre que tenia la opcion, para conservar lo ya asignado al renombrarla.
ESTADOS = [
    ("En evaluación",    "GRAY",   "Recibido. Estamos validando si entra en los planes",         "En evaluacion"),
    ("En backlog",       "BLUE",   "Aceptado y priorizado, todavía sin empezar",                 "En Backlog"),
    ("En desarrollo",    "PURPLE", "Se está construyendo ahora",                                 "En desarrollo"),
    ("En pruebas",       "YELLOW", "Construido, en verificación antes de publicarlo",            "En Pruebas"),
    ("En implementación","ORANGE", "Publicado y en marcha con algunas áreas antes que con todas","En implementacion"),
    ("Publicado",        "GREEN",  "Ya es parte de las herramientas y cualquiera lo usa",        "Publicado"),
    ("Pausado",          "PINK",   "Detenido a propósito. El motivo está en la solicitud",       "Pausado"),
    ("No va",            "RED",    "Se decidió no hacerlo. El motivo está en la solicitud",      "No va"),
]

TRIMESTRES_DESDE = datetime.date(2026, 7, 1)
TRIMESTRES_HASTA = datetime.date(2029, 1, 1)

# Cada app con su color. Ojo: la paleta de un campo de tablero tiene solo OCHO colores
# (GRAY BLUE GREEN YELLOW ORANGE RED PINK PURPLE) y hay diez herramientas, asi que dos
# parejas comparten color. En las ETIQUETAS del repo si hay un color distinto para cada una,
# porque ahi el color es un hex libre — ver configurar-repo.ps1.
#   (nombre, etiqueta, color del tablero, nombre anterior de la opcion, descripcion)
HERRAMIENTAS = [
    ("📊 Tablero DataMart",       "app: datamart",    "BLUE",   "Tablero DataMart",       "Indicadores del ERP"),
    ("📓 Bitácora de Obra",       "app: bitacora",    "ORANGE", "Bitácora de Obra",       "Informes diarios de obra"),
    ("⏰ Registro de Horarios",   "app: horarios",    "PURPLE", "Registro de Horarios",   "Asistencia y novedades"),
    ("🚚 Portal de Proveedores",  "app: proveedores", "PINK",   "Portal de Proveedores",  "Alta de proveedores"),
    ("📋 Gestión de Proyectos",   "app: proyectos",   "YELLOW", "Gestión de Proyectos",   "Seguimiento de proyectos"),
    ("📚 Biblioteca de Informes", "app: biblioteca",  "GREEN",  "Biblioteca de Informes", "Informes publicados"),
    ("🌎 Consulta Geográfica",    "app: geo",         "GREEN",  "Consulta Geográfica",    "Malla vial de Bogotá"),
    ("💬 Asistente",              "app: asistente",   "GRAY",   "Asistente",              "Consultas por WhatsApp"),
    ("🏠 Menú de entrada",        "app: menu",        "GRAY",   "Menú de entrada",        "Acceso a las herramientas"),
    ("🔧 Plataforma",             "app: plataforma",  "RED",    "Plataforma",             "Afecta a varias herramientas"),
]

# Que se ve en cada tarjeta / fila. SIN esto las tarjetas solo traen titulo y repositorio, y
# no hay forma de saber de un vistazo si algo es de Bitacora o de Horarios.
# En el modelo de Sincosoft las tarjetas llevan Labels y Periodo; aqui va ademas Herramienta,
# que es la que trae el color y el icono de la app.
CAMPOS_POR_VISTA = {
    "General":      ["Title", "Herramienta", "Status", "Prioridad", "Periodo", "Labels"],
    "Por estado":   ["Title", "Herramienta", "Prioridad", "Periodo"],
    "Hoja de ruta": ["Title", "Herramienta", "Status", "Periodo"],
}
# Las vistas de una sola app no repiten Herramienta: la pestana entera ya es esa app.
CAMPOS_VISTA_APP = ["Title", "Status", "Prioridad", "Periodo", "Labels"]


def gh(args, entrada=None):
    r = subprocess.run(["gh"] + args, capture_output=True, input=entrada,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "").strip())
    return r.stdout


def gql(consulta, **variables):
    """La consulta va por archivo UTF-8 sin BOM: pasarla como argumento rompe los acentos."""
    f = os.path.join(tempfile.gettempdir(), "gql_cfg.graphql")
    io.open(f, "w", encoding="utf-8", newline="\n").write(consulta)
    args = ["api", "graphql", "-F", "query=@" + f]
    for k, v in variables.items():
        args += ["-f", "%s=%s" % (k, v)]
    d = json.loads(gh(args))
    if "errors" in d:
        raise RuntimeError(json.dumps(d["errors"], ensure_ascii=False))
    return d["data"]


def trimestres():
    """Trimestres de calendario reales, con el nombre en el estilo '2026 T3 Jul - Sep'."""
    etiquetas = {1: "Ene - Mar", 4: "Abr - Jun", 7: "Jul - Sep", 10: "Oct - Dic"}
    salida = []
    anio = TRIMESTRES_DESDE.year
    while anio <= TRIMESTRES_HASTA.year:
        for i, mes in enumerate((1, 4, 7, 10)):
            ini = datetime.date(anio, mes, 1)
            if ini < TRIMESTRES_DESDE or ini >= TRIMESTRES_HASTA:
                continue
            sig = datetime.date(anio + 1, 1, 1) if mes == 10 else datetime.date(anio, mes + 3, 1)
            salida.append({
                "title": "%d T%d %s" % (anio, i + 1, etiquetas[mes]),
                "startDate": ini.isoformat(),
                "duration": (sig - ini).days,
            })
        anio += 1
    return salida


def main():
    print()
    print("  Configurando el tablero #%d de %s" % (NUMERO_TABLERO, DUENO))
    print()

    d = gql("""
    query($d:String!){
      user(login:$d){
        projectV2(number:%d){
          id url
          fields(first:50){
            nodes{
              ... on ProjectV2FieldCommon { id name dataType }
              ... on ProjectV2SingleSelectField { options { id name } }
            }
          }
          views(first:40){ nodes{ id number name layout filter } }
        }
      }
    }
    """ % NUMERO_TABLERO, d=DUENO)
    t = d["user"]["projectV2"]
    pid = t["id"]

    campos = {}
    for n in t["fields"]["nodes"]:
        if n and n.get("name"):
            campos[n["name"]] = n
    vistas = {v["name"]: v for v in t["views"]["nodes"]}

    # ------------------------------------------------------------ 1. los estados ----
    st = campos.get("Status")
    if not st:
        print("  No encuentro el campo Status")
        return 1
    previas = {o["name"]: o["id"] for o in st.get("options", [])}

    opciones = []
    conservadas = 0
    for nombre, color, desc, antes in ESTADOS:
        # Primero por el nombre actual, y solo si no esta, por el anterior. Al reves, un
        # cambio de nombre (ponerle un acento, por ejemplo) crea una opcion NUEVA y los
        # items que la tenian asignada se quedan en blanco.
        oid = previas.get(nombre) or (previas.get(antes) if antes else None)
        if oid:
            conservadas += 1
            opciones.append('{ id: "%s", name: "%s", color: %s, description: "%s" }'
                            % (oid, nombre, color, desc))
        else:
            opciones.append('{ name: "%s", color: %s, description: "%s" }'
                            % (nombre, color, desc))

    r = gql("""
    mutation {
      updateProjectV2Field(input:{
        fieldId: "%s"
        singleSelectOptions: [ %s ]
      }){ projectV2Field { ... on ProjectV2SingleSelectField { options { name } } } }
    }
    """ % (st["id"], "\n          ".join(opciones)))
    nombres = [o["name"] for o in r["updateProjectV2Field"]["projectV2Field"]["options"]]
    print("  Estados (%d, %d renombradas conservando lo asignado):" % (len(nombres), conservadas))
    for n in nombres:
        print("      %s" % n)

    # ------------------------------------------- 1b. el campo Herramienta, con color ----
    hr = campos.get("Herramienta")
    if hr:
        prev = {o["name"]: o["id"] for o in hr.get("options", [])}
        ops = []
        for nombre, _et, color, antes, desc in HERRAMIENTAS:
            oid = prev.get(nombre) or prev.get(antes)
            if oid:
                ops.append('{ id: "%s", name: "%s", color: %s, description: "%s" }'
                           % (oid, nombre, color, desc))
            else:
                ops.append('{ name: "%s", color: %s, description: "%s" }'
                           % (nombre, color, desc))
        r = gql("""
        mutation {
          updateProjectV2Field(input:{
            fieldId: "%s"
            singleSelectOptions: [ %s ]
          }){ projectV2Field { ... on ProjectV2SingleSelectField { options { name color } } } }
        }
        """ % (hr["id"], SALTO.join(ops)))
        print()
        print("  Herramientas (cada una con su color):")
        for o in r["updateProjectV2Field"]["projectV2Field"]["options"]:
            print("      %-24s %s" % (o["name"], o["color"]))

    # -------------------------------------------------- 2. el campo de trimestre ----
    tri = trimestres()
    if "Periodo" in campos:
        print()
        print("  Campo Periodo: ya existe, no se toca (%d trimestres definidos)" % len(tri))
    else:
        items = ", ".join(
            '{ title: "%s", startDate: "%s", duration: %d }'
            % (q["title"], q["startDate"], q["duration"]) for q in tri
        )
        gql("""
        mutation {
          createProjectV2Field(input:{
            projectId: "%s"
            dataType: ITERATION
            name: "Periodo"
            iterationConfiguration: {
              startDate: "%s"
              duration: %d
              iterations: [ %s ]
            }
          }){ projectV2Field { ... on ProjectV2IterationField { id name } } }
        }
        """ % (pid, tri[0]["startDate"], tri[0]["duration"], items))
        print()
        print("  Campo Periodo creado con %d trimestres: %s ... %s"
              % (len(tri), tri[0]["title"], tri[-1]["title"]))

    # ------------------------- 3. fuera los campos de fecha (un solo mecanismo) ----
    print()
    for viejo in ("Inicio", "Fecha objetivo"):
        if viejo in campos:
            gql("""mutation { deleteProjectV2Field(input:{fieldId:"%s"}){ clientMutationId } }"""
                % campos[viejo]["id"])
            print("  Campo %s eliminado (el tiempo lo lleva Periodo)" % viejo)

    # ---------------------------------------------------------------- 4. vistas ----
    print()
    print("  Vistas:")

    def vista(nombre, layout, filtro=""):
        v = vistas.get(nombre)
        if v:
            if (v.get("filter") or "") == filtro and v["layout"] == layout:
                print("      = %-24s %s" % (nombre, layout.replace("_LAYOUT", "")))
                return
            gql("""
            mutation($n:String!,$f:String!){
              updateProjectV2View(input:{ viewId:"%s", name:$n, layout:%s, filter:$f }){
                projectV2View { name }
              }
            }
            """ % (v["id"], layout), n=nombre, f=filtro)
            print("      ~ %-24s %s  ajustada" % (nombre, layout.replace("_LAYOUT", "")))
            return
        r = gql("""
        mutation($n:String!){
          createProjectV2View(input:{ projectId:"%s", name:$n, layout:%s }){
            projectV2View { id name }
          }
        }
        """ % (pid, layout), n=nombre)
        nid = r["createProjectV2View"]["projectV2View"]["id"]
        if filtro:
            gql("""
            mutation($f:String!){
              updateProjectV2View(input:{ viewId:"%s", filter:$f }){ projectV2View { name } }
            }
            """ % nid, f=filtro)
        print("      + %-24s %s%s" % (nombre, layout.replace("_LAYOUT", ""),
                                      ("  filtro " + filtro) if filtro else ""))

    # las tres globales, como en el modelo
    vista("General",    "TABLE_LAYOUT")
    vista("Por estado", "BOARD_LAYOUT")
    vista("Hoja de ruta", "ROADMAP_LAYOUT")

    # una por herramienta, pero SOLO si tiene solicitudes: 10 pestanas vacias estorban
    issues = json.loads(gh(["issue", "list", "--repo", REPO, "--state", "all",
                            "--limit", "300", "--json", "labels"]))
    con_uso = set()
    for i in issues:
        for l in i["labels"]:
            con_uso.add(l["name"])

    for nombre, etiqueta, _c, _a, _d in HERRAMIENTAS:
        if etiqueta in con_uso:
            vista(nombre, "BOARD_LAYOUT", 'label:"%s"' % etiqueta)

    # Vistas sobrantes: quedan cuando una herramienta se renombra (por ejemplo al ponerle
    # el acento) y la vista vieja no se borra. Sin esto el tablero acumula pestanas muertas.
    legitimas = {"General", "Por estado", "Hoja de ruta"} | {h[0] for h in HERRAMIENTAS}
    for nombre, v in vistas.items():
        if nombre not in legitimas:
            gql("""mutation { deleteProjectV2View(input:{viewId:"%s"}){ clientMutationId } }"""
                % v["id"])
            print("      - %-24s sobrante, borrada" % nombre)

    saltadas = [h[0] for h in HERRAMIENTAS if h[1] not in con_uso]
    if saltadas:
        print()
        print("  Sin pestana propia porque todavia no tienen solicitudes:")
        print("      %s" % ", ".join(saltadas))
        print("  (vuelve a correr este script cuando las tengan)")

    # -------------------------------------- 5. que campos se ven en cada tarjeta ----
    # Se vuelve a leer las vistas: las que se acabaron de crear no estan en el mapa inicial.
    fresco = gql("""
    query($d:String!){ user(login:$d){ projectV2(number:%d){
      views(first:40){ nodes{ id name layout } }
      fields(first:50){ nodes{ ... on ProjectV2FieldCommon { id name } } } } } }
    """ % NUMERO_TABLERO, d=DUENO)["user"]["projectV2"]
    frescas = fresco["views"]["nodes"]
    for n in fresco["fields"]["nodes"]:
        if n and n.get("name") and n["name"] not in campos:
            campos[n["name"]] = {"id": n["id"]}

    nombres_app = {h[0] for h in HERRAMIENTAS}
    print()
    print("  Campos visibles en cada vista:")
    for v in frescas:
        # La vista Roadmap no acepta campos visibles: "Roadmap views do not support
        # visible fields". Se salta por tipo, no por nombre.
        if v["layout"] == "ROADMAP_LAYOUT":
            print("      %-24s (Roadmap: GitHub no permite elegir campos)" % v["name"])
            continue
        quiere = CAMPOS_POR_VISTA.get(v["name"])
        if quiere is None:
            quiere = CAMPOS_VISTA_APP if v["name"] in nombres_app else None
        if not quiere:
            continue
        ids = [campos[n]["id"] for n in quiere if n in campos]
        gql("""
        mutation {
          updateProjectV2View(input:{
            viewId: "%s"
            configuration: { visibleFieldIds: [%s] }
          }){ projectV2View { name } }
        }
        """ % (v["id"], ", ".join('"%s"' % i for i in ids)))
        print("      %-24s %s" % (v["name"], " · ".join(quiere)))

    print()
    print("  %s" % t["url"])
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
