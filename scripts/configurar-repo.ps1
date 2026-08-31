<#
  configurar-repo.ps1 — deja el repositorio del roadmap con sus etiquetas, hitos y
  candados puestos. Es idempotente: se puede correr las veces que sea.

  Requiere: gh autenticado (gh auth status).
#>

$ErrorActionPreference = 'Stop'
$REPO = 'controldepresupuesto/roadmap-cimelec'

Write-Host ''
Write-Host "  Configurando $REPO" -ForegroundColor Cyan
Write-Host ''

# ---------------------------------------------------------------- ETIQUETAS ----
$etiquetas = @(
  # Herramienta
  @{ n='app: datamart';      c='0969DA'; d='Tablero DataMart' },
  @{ n='app: bitacora';      c='0969DA'; d='Bitacora de Obra' },
  @{ n='app: horarios';      c='0969DA'; d='Registro de Horarios' },
  @{ n='app: proveedores';   c='0969DA'; d='Portal de Proveedores' },
  @{ n='app: proyectos';     c='0969DA'; d='Gestion de Proyectos' },
  @{ n='app: biblioteca';    c='0969DA'; d='Biblioteca de Informes' },
  @{ n='app: geo';           c='0969DA'; d='Consulta Geografica' },
  @{ n='app: asistente';     c='0969DA'; d='Asistente de consulta por WhatsApp' },
  @{ n='app: menu';          c='0969DA'; d='Menu de entrada' },
  @{ n='app: plataforma';    c='8250DF'; d='Transversal: afecta a varias herramientas' },
  # Tipo
  @{ n='tipo: mejora';       c='A2EEEF'; d='Existe y puede quedar mejor' },
  @{ n='tipo: error';        c='D73A4A'; d='No funciona o muestra un dato equivocado' },
  @{ n='tipo: idea';         c='FBCA04'; d='Algo nuevo que no existe todavia' },
  @{ n='tipo: nuevo';        c='0E8A16'; d='Modulo o herramienta nueva completa' },
  # Estado
  @{ n='estado: idea';       c='EDEDED'; d='Recibido y anotado. Sin compromiso de fecha' },
  @{ n='estado: en analisis';c='C5DEF5'; d='Definiendo alcance y estimando' },
  @{ n='estado: en curso';   c='1D76DB'; d='Se esta construyendo ahora' },
  @{ n='estado: en prueba';  c='FEF2C0'; d='Construido, en verificacion' },
  @{ n='estado: publicado';  c='0E8A16'; d='En produccion' },
  @{ n='estado: pausado';    c='E4E669'; d='Detenido a proposito' },
  @{ n='estado: no va';      c='6E7781'; d='Se decidio no hacerlo' },
  # Prioridad
  @{ n='prioridad: alta';    c='B60205'; d='Cifra mala, caido, o bloquea a un area' },
  @{ n='prioridad: media';   c='FBCA04'; d='Molesta a varios todos los dias' },
  @{ n='prioridad: baja';    c='C2E0C6'; d='Comodidad o una sola persona' }
)

foreach ($e in $etiquetas) {
  gh label create $e.n --repo $REPO --color $e.c --description $e.d --force 2>&1 | Out-Null
  if ($?) { Write-Host "  etiqueta  $($e.n)" -ForegroundColor DarkGray }
  else    { Write-Host "  FALLO     $($e.n)" -ForegroundColor Red }
}

# Las etiquetas por defecto de GitHub no aplican aqui
foreach ($v in @('bug','documentation','duplicate','enhancement','good first issue','help wanted','invalid','question','wontfix')) {
  gh label delete $v --repo $REPO --yes 2>&1 | Out-Null
}

# -------------------------------------------------------------------- HITOS ----
# Un hito por mes, seis meses hacia adelante. Sirve para agrupar entregas.
$hoy = Get-Date
for ($i = 0; $i -lt 6; $i++) {
  $m = $hoy.AddMonths($i)
  $titulo = $m.ToString('yyyy-MM')
  $ultimo = [DateTime]::new($m.Year, $m.Month, [DateTime]::DaysInMonth($m.Year, $m.Month))
  gh api "repos/$REPO/milestones" -f title="$titulo" -f due_on="$($ultimo.ToString('yyyy-MM-dd'))T23:59:59Z" 2>&1 | Out-Null
  if ($?) { Write-Host "  hito      $titulo" -ForegroundColor DarkGray }
}

# ---------------------------------------------------------------- CANDADOS ----
Write-Host ''
Write-Host '  Cerrando lo que no se usa...' -ForegroundColor Cyan

# Sin wiki. La pestana Projects SI se queda: es donde vive el tablero y el README apunta ahi.
gh api -X PATCH "repos/$REPO" -F has_wiki=false -F has_projects=true 2>&1 | Out-Null
if ($?) { Write-Host '  wiki apagada, pestana Projects encendida' -ForegroundColor DarkGray }

# Solo colaboradores escriben. CADUCA A LOS 6 MESES: hay que volver a correr esto.
# El respaldo permanente es .github/workflows/solo-equipo.yml, que no caduca.
gh api -X PUT "repos/$REPO/interaction-limits" -f limit=collaborators_only -f expiry=six_months 2>&1 | Out-Null
if ($?) { Write-Host '  escritura limitada al equipo (6 meses, renovable)' -ForegroundColor DarkGray }

Write-Host ''
Write-Host '  Listo.' -ForegroundColor Green
Write-Host ''
Write-Host '  Recordatorio: el limite de interaccion caduca en 6 meses.' -ForegroundColor Yellow
Write-Host '  Vuelve a correr este script para renovarlo.' -ForegroundColor Yellow
Write-Host ''
