<#
  crear-tablero.ps1 - crea el tablero (GitHub Project) de la hoja de ruta con sus campos,
  lo hace publico, lo conecta al repositorio y le mete las solicitudes que ya existen.

  ANTES de correr esto, una sola vez, hay que ampliar el permiso de gh:

      gh auth refresh -s project

  Abre el navegador, confirmas, y listo. Sin ese permiso GitHub no deja crear tableros
  desde la linea de comandos.

  Se puede correr dos veces? NO: crearia un segundo tablero. Si ya existe, no lo corras.
#>

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

$REPO   = 'controldepresupuesto/roadmap-cimelec'
$TITULO = 'Hoja de ruta - Plataforma CIMELEC'

function Gql($consulta) {
  # La consulta va por archivo sin BOM: pasarla como argumento rompe los acentos en PS 5.1
  $f = Join-Path $env:TEMP ("gql_" + [guid]::NewGuid().ToString('N') + '.graphql')
  [System.IO.File]::WriteAllText($f, $consulta, (New-Object System.Text.UTF8Encoding $false))
  $salida = gh api graphql -F query="@$f" 2>&1
  $codigo = $LASTEXITCODE
  Remove-Item $f -Force -ErrorAction SilentlyContinue
  if ($codigo -ne 0) { throw ($salida | Out-String) }
  return ($salida | Out-String | ConvertFrom-Json)
}

Clear-Host
Write-Host ''
Write-Host '  =============================================' -ForegroundColor Cyan
Write-Host '   CREAR EL TABLERO DE LA HOJA DE RUTA' -ForegroundColor Cyan
Write-Host '  =============================================' -ForegroundColor Cyan
Write-Host ''

# ------------------------------------------------------ 0. revisar el permiso ----
$estadoAuth = (gh auth status 2>&1 | Out-String)
if ($estadoAuth -notmatch 'project') {
  Write-Host '  Falta el permiso de tableros. Corre esto primero:' -ForegroundColor Red
  Write-Host ''
  Write-Host '      gh auth refresh -s project' -ForegroundColor White
  Write-Host ''
  Read-Host '  Enter para salir'
  exit 1
}

# -------------------------------------------------------- 1. crear el tablero ----
$ownerId = (gh api user --jq .node_id)
$repoId  = (gh api "repos/$REPO" --jq .node_id)

Write-Host '  Creando el tablero...' -ForegroundColor Cyan
$r = Gql @"
mutation {
  createProjectV2(input: { ownerId: "$ownerId", title: "$TITULO" }) {
    projectV2 { id number url }
  }
}
"@
$idTablero = $r.data.createProjectV2.projectV2.id
$numero    = $r.data.createProjectV2.projectV2.number
$url       = $r.data.createProjectV2.projectV2.url
Write-Host "  Tablero #$numero creado" -ForegroundColor Green

# ------------------------------------------------ 2. publico y con descripcion ----
$desc = 'Que se esta construyendo, que salio y que viene en las herramientas internas del grupo CIMELEC INGENIEROS.'
$lineas = @(
  '## Como leer este tablero',
  '',
  'Cada tarjeta es una solicitud: una mejora, un error o una idea.',
  '',
  '- **Estado** dice en que va.',
  '- **Herramienta** dice a que app pertenece.',
  '- **Prioridad** la fija la direccion, no el orden de llegada.',
  '- **Fecha objetivo** aparece cuando la solicitud entra en curso.',
  '',
  'El detalle de cada una esta en su solicitud. Los criterios de priorizacion estan en',
  'docs/como-priorizamos.md del repositorio.'
)
$lea = ($lineas -join '\n').Replace('"', '\"')

Gql @"
mutation {
  updateProjectV2(input: {
    projectId: "$idTablero"
    public: true
    shortDescription: "$desc"
    readme: "$lea"
  }) { projectV2 { id } }
}
"@ | Out-Null
Write-Host '  Publico y con descripcion' -ForegroundColor Green

# ---------------------------------------------------------- 3. campo Estado ----
# El tablero nace con un campo "Status" (Todo / In Progress / Done). Se reusa: se renombra
# a Estado y se le cambian las opciones por las nuestras.
$campos = Gql @"
query {
  node(id: "$idTablero") {
    ... on ProjectV2 {
      fields(first: 30) { nodes { ... on ProjectV2FieldCommon { id name dataType } } }
    }
  }
}
"@
$status = $campos.data.node.fields.nodes | Where-Object { $_.name -eq 'Status' } | Select-Object -First 1

$opcionesEstado = @'
{ name: "Idea",        color: GRAY,   description: "Recibido y anotado. Sin compromiso de fecha" }
{ name: "En analisis", color: BLUE,   description: "Definiendo alcance y estimando" }
{ name: "En curso",    color: PURPLE, description: "Se esta construyendo ahora" }
{ name: "En prueba",   color: YELLOW, description: "Construido, en verificacion" }
{ name: "Publicado",   color: GREEN,  description: "En produccion" }
{ name: "Pausado",     color: ORANGE, description: "Detenido a proposito" }
{ name: "No va",       color: RED,    description: "Se decidio no hacerlo" }
'@

$estadoOk = $false
if ($status) {
  try {
    Gql @"
mutation {
  updateProjectV2Field(input: {
    fieldId: "$($status.id)"
    name: "Estado"
    singleSelectOptions: [ $opcionesEstado ]
  }) { projectV2Field { ... on ProjectV2SingleSelectField { id name } } }
}
"@ | Out-Null
    $estadoOk = $true
    Write-Host '  Campo Estado (reusando Status)' -ForegroundColor Green
  } catch {
    Write-Host '  No se pudo reusar Status; creo un campo Estado aparte' -ForegroundColor Yellow
  }
}
if (-not $estadoOk) {
  Gql @"
mutation {
  createProjectV2Field(input: {
    projectId: "$idTablero"
    dataType: SINGLE_SELECT
    name: "Estado"
    singleSelectOptions: [ $opcionesEstado ]
  }) { projectV2Field { ... on ProjectV2SingleSelectField { id } } }
}
"@ | Out-Null
  Write-Host '  Campo Estado creado' -ForegroundColor Green
}

# ------------------------------------------------------ 4. los otros campos ----
$opcHerramienta = @'
{ name: "Tablero DataMart",       color: BLUE,   description: "Indicadores del ERP" }
{ name: "Bitacora de Obra",       color: BLUE,   description: "Informes diarios de obra" }
{ name: "Registro de Horarios",   color: BLUE,   description: "Asistencia y novedades" }
{ name: "Portal de Proveedores",  color: BLUE,   description: "Alta de proveedores" }
{ name: "Gestion de Proyectos",   color: BLUE,   description: "Seguimiento de proyectos" }
{ name: "Biblioteca de Informes", color: BLUE,   description: "Informes publicados" }
{ name: "Consulta Geografica",    color: BLUE,   description: "Malla vial de Bogota" }
{ name: "Asistente",              color: BLUE,   description: "Consultas por WhatsApp" }
{ name: "Menu de entrada",        color: BLUE,   description: "Acceso a las herramientas" }
{ name: "Plataforma",             color: PURPLE, description: "Afecta a varias herramientas" }
'@

$opcPrioridad = @'
{ name: "Alta",  color: RED,    description: "Cifra mala, caido, o bloquea a un area" }
{ name: "Media", color: YELLOW, description: "Molesta a varios todos los dias" }
{ name: "Baja",  color: GREEN,  description: "Comodidad, o una sola persona" }
'@

$nuevos = @(
  @{ nombre = 'Herramienta';    tipo = 'SINGLE_SELECT'; opciones = $opcHerramienta },
  @{ nombre = 'Prioridad';      tipo = 'SINGLE_SELECT'; opciones = $opcPrioridad },
  @{ nombre = 'Inicio';         tipo = 'DATE';          opciones = $null },
  @{ nombre = 'Fecha objetivo'; tipo = 'DATE';          opciones = $null }
)

foreach ($c in $nuevos) {
  $extra = ''
  if ($c.opciones) { $extra = "singleSelectOptions: [ $($c.opciones) ]" }
  try {
    Gql @"
mutation {
  createProjectV2Field(input: {
    projectId: "$idTablero"
    dataType: $($c.tipo)
    name: "$($c.nombre)"
    $extra
  }) { projectV2Field { ... on ProjectV2FieldCommon { id name } } }
}
"@ | Out-Null
    Write-Host "  Campo $($c.nombre)" -ForegroundColor Green
  } catch {
    Write-Host "  FALLO el campo $($c.nombre)" -ForegroundColor Red
  }
}

# ------------------------------------------------ 5. conectar al repositorio ----
try {
  Gql @"
mutation {
  linkProjectV2ToRepository(input: { projectId: "$idTablero", repositoryId: "$repoId" }) {
    repository { id }
  }
}
"@ | Out-Null
  Write-Host '  Conectado al repositorio' -ForegroundColor Green
} catch {
  Write-Host '  No se pudo conectar al repositorio (hazlo desde la web)' -ForegroundColor Yellow
}

# ------------------------------------------ 6. meter las solicitudes que hay ----
Write-Host ''
Write-Host '  Metiendo las solicitudes abiertas...' -ForegroundColor Cyan
$issues = gh issue list --repo $REPO --state open --limit 200 --json number | ConvertFrom-Json
foreach ($i in $issues) {
  $nodeId = gh api "repos/$REPO/issues/$($i.number)" --jq .node_id
  try {
    Gql @"
mutation {
  addProjectV2ItemById(input: { projectId: "$idTablero", contentId: "$nodeId" }) { item { id } }
}
"@ | Out-Null
    Write-Host "  #$($i.number) agregada" -ForegroundColor DarkGray
  } catch {
    Write-Host "  #$($i.number) FALLO" -ForegroundColor Red
  }
}

# ---------------------------------------------------------------- cierre ----
Write-Host ''
Write-Host '  Tablero listo:' -ForegroundColor Green
Write-Host "  $url" -ForegroundColor White
Write-Host ''
Write-Host '  FALTAN LAS DOS VISTAS. Eso GitHub no lo deja hacer por linea de comandos;' -ForegroundColor Yellow
Write-Host '  son unos clics en la web, una sola vez:' -ForegroundColor Yellow
Write-Host ''
Write-Host '   VISTA "Tablero"' -ForegroundColor White
Write-Host '     1. Abre el tablero y en la pestana "View 1" dale a la flechita > Duplicate view'
Write-Host '     2. Renombrala "Tablero" y arriba elige el layout "Board"'
Write-Host '     3. En "Group by" elige Estado'
Write-Host ''
Write-Host '   VISTA "Hoja de ruta"' -ForegroundColor White
Write-Host '     1. Dale al + al lado de las pestanas > New view'
Write-Host '     2. Renombrala "Hoja de ruta" y elige el layout "Roadmap"'
Write-Host '     3. En el engranaje de la derecha > Date fields: Start = Inicio, Target = Fecha objetivo'
Write-Host '     4. "Zoom level" en Month'
Write-Host ''
Write-Host '   Y borra la vista "View 1" que quedo vacia.' -ForegroundColor White
Write-Host ''
Read-Host '  Enter para cerrar'
