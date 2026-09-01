# -*- coding: utf-8 -*-
"""
Proyecta las solicitudes del repositorio sobre el tablero de la hoja de ruta.

Las ETIQUETAS del issue son la fuente de verdad. Este script las copia a los campos del
tablero, para no llevar el estado en dos lados a mano:

    estado: en curso      ->  campo Status      = "En curso"
    app: bitacora         ->  campo Herramienta = "Bitacora de Obra"
    prioridad: alta       ->  campo Prioridad   = "Alta"

Se puede correr las veces que sea: agrega lo que falte, corrige lo que este distinto y no
toca lo que ya esta bien.

Requiere: gh autenticado con el permiso 'project'  (gh auth refresh --hostname github.com -s project)
"""

import json
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = "controldepresupuesto/roadmap-cimelec"
DUENO = "controldepresupuesto"
NUMERO_TABLERO = 1

# etiqueta -> nombre de la opcion en el tablero
MAPA = {
    "Status": {
        "estado: en evaluacion":    "En evaluación",
        "estado: en backlog":       "En backlog",
        "estado: en desarrollo":    "En desarrollo",
        "estado: en pruebas":       "En pruebas",
        "estado: en implementacion":"En implementación",
        "estado: publicado":        "Publicado",
        "estado: pausado":          "Pausado",
        "estado: no va":            "No va",
    },
    "Herramienta": {
        "app: datamart": "Tablero DataMart",
        "app: bitacora": "Bitácora de Obra",
        "app: horarios": "Registro de Horarios",
        "app: proveedores": "Portal de Proveedores",
        "app: proyectos": "Gestión de Proyectos",
        "app: biblioteca": "Biblioteca de Informes",
        "app: geo": "Consulta Geográfica",
        "app: asistente": "Asistente",
        "app: menu": "Menú de entrada",
        "app: plataforma": "Plataforma",
    },
    "Prioridad": {
        "prioridad: alta": "Alta",
        "prioridad: media": "Media",
        "prioridad: baja": "Baja",
    },
}


def gh(args, entrada=None):
    r = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        input=entrada,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "").strip())
    return r.stdout


def gql(consulta, **variables):
    args = ["api", "graphql", "-f", "query=" + consulta]
    for k, v in variables.items():
        args += ["-f", "%s=%s" % (k, v)]
    d = json.loads(gh(args))
    if "errors" in d:
        raise RuntimeError(json.dumps(d["errors"], ensure_ascii=False))
    return d["data"]


# ------------------------------------------------------------------ el tablero ----

# El numero del tablero va literal: gh -f manda todo como texto y aqui hace falta un Int
Q_TABLERO = """
query($d:String!){
  user(login:$d){
    projectV2(number:1){
      id title url
      fields(first:40){
        nodes{
          ... on ProjectV2SingleSelectField { id name options { id name } }
          ... on ProjectV2FieldCommon { id name }
        }
      }
    }
  }
}
"""

Q_ITEMS = """
query($p:ID!,$c:String){
  node(id:$p){
    ... on ProjectV2 {
      items(first:100, after:$c){
        pageInfo { hasNextPage endCursor }
        nodes{
          id
          content{ ... on Issue { number } }
          fieldValues(first:20){
            nodes{
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field{ ... on ProjectV2SingleSelectField { name } }
              }
            }
          }
        }
      }
    }
  }
}
"""

M_AGREGAR = """
mutation($p:ID!,$c:ID!){
  addProjectV2ItemById(input:{projectId:$p, contentId:$c}){ item { id } }
}
"""

M_FIJAR = """
mutation($p:ID!,$i:ID!,$f:ID!,$o:String!){
  updateProjectV2ItemFieldValue(input:{
    projectId:$p, itemId:$i, fieldId:$f, value:{singleSelectOptionId:$o}
  }){ projectV2Item { id } }
}
"""


def main():
    print()
    print("  Sincronizando el tablero desde las etiquetas de %s" % REPO)
    print()

    d = gql(Q_TABLERO, d=DUENO)
    tablero = d["user"]["projectV2"]
    if not tablero:
        print("  No encuentro el tablero #%d de %s" % (NUMERO_TABLERO, DUENO))
        return 1
    pid = tablero["id"]

    # campos por nombre, con sus opciones
    campos = {}
    for n in tablero["fields"]["nodes"]:
        if not n or "name" not in n:
            continue
        campos[n["name"]] = {
            "id": n["id"],
            "opciones": {o["name"]: o["id"] for o in n.get("options", [])},
        }

    faltan = [c for c in MAPA if c not in campos]
    if faltan:
        print("  Al tablero le faltan campos: %s" % ", ".join(faltan))
        return 1

    # items que ya estan, con el valor actual de cada campo
    existentes = {}
    cursor = None
    while True:
        args = {"p": pid}
        if cursor:
            args["c"] = cursor
        r = gql(Q_ITEMS, **args)["node"]["items"]
        for it in r["nodes"]:
            cont = it.get("content") or {}
            num = cont.get("number")
            if num is None:
                continue
            valores = {}
            for fv in it["fieldValues"]["nodes"]:
                if fv and fv.get("field"):
                    valores[fv["field"]["name"]] = fv.get("name")
            existentes[num] = {"item": it["id"], "valores": valores}
        if not r["pageInfo"]["hasNextPage"]:
            break
        cursor = r["pageInfo"]["endCursor"]

    # las solicitudes del repo
    issues = json.loads(
        gh(["issue", "list", "--repo", REPO, "--state", "all", "--limit", "300",
            "--json", "number,title,labels,url"])
    )
    issues.sort(key=lambda i: i["number"])

    agregados = 0
    fijados = 0
    intactos = 0

    for iss in issues:
        num = iss["number"]
        etiquetas = {l["name"] for l in iss["labels"]}
        titulo = iss["title"]
        if len(titulo) > 58:
            titulo = titulo[:57] + "…"

        if num in existentes:
            item = existentes[num]["item"]
            actuales = existentes[num]["valores"]
            nota = "        "
        else:
            node_id = gh(["api", "repos/%s/issues/%d" % (REPO, num), "--jq", ".node_id"]).strip()
            item = gql(M_AGREGAR, p=pid, c=node_id)["addProjectV2ItemById"]["item"]["id"]
            actuales = {}
            agregados += 1
            nota = "  NUEVA  "

        cambios = []
        for campo, tabla in MAPA.items():
            deseado = None
            for etiqueta, opcion in tabla.items():
                if etiqueta in etiquetas:
                    deseado = opcion
                    break
            if deseado is None:
                continue
            if actuales.get(campo) == deseado:
                continue
            oid = campos[campo]["opciones"].get(deseado)
            if not oid:
                print("  #%-3d  el campo %s no tiene la opcion '%s'" % (num, campo, deseado))
                continue
            gql(M_FIJAR, p=pid, i=item, f=campos[campo]["id"], o=oid)
            cambios.append("%s=%s" % (campo, deseado))
            fijados += 1

        if cambios:
            print("%s#%-3d %-58s  %s" % (nota, num, titulo, " ".join(cambios)))
        else:
            intactos += 1
            print("%s#%-3d %-58s  (sin cambios)" % (nota, num, titulo))

    print()
    print("  %d solicitudes agregadas, %d valores fijados, %d ya estaban bien"
          % (agregados, fijados, intactos))
    print("  %s" % tablero["url"])
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
