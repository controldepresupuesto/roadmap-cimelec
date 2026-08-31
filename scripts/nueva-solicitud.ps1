<#
  nueva-solicitud.ps1 — registra en el roadmap una solicitud que llego por WhatsApp,
  correo o de viva voz. Para la gente que no tiene cuenta de GitHub.

  No hace falta saber GitHub: responde las preguntas y al final te da el enlace
  para devolverselo a quien lo pidio.
#>

$ErrorActionPreference = 'Stop'
$REPO = 'controldepresupuesto/roadmap-cimelec'

function Preguntar($texto, $obligatorio = $true) {
  while ($true) {
    $r = Read-Host "  $texto"
    if ($r -or -not $obligatorio) { return $r }
    Write-Host '  (hace falta)' -ForegroundColor Yellow
  }
}

function Menu($titulo, $opciones) {
  Write-Host ''
  Write-Host "  $titulo" -ForegroundColor Cyan
  for ($i = 0; $i -lt $opciones.Count; $i++) {
    Write-Host ("    {0}) {1}" -f ($i + 1), $opciones[$i].texto)
  }
  while ($true) {
    $n = Read-Host '  Numero'
    $k = 0
    if ([int]::TryParse($n, [ref]$k)) {
      if ($k -ge 1 -and $k -le $opciones.Count) { return $opciones[$k - 1] }
    }
    Write-Host '  (elige un numero de la lista)' -ForegroundColor Yellow
  }
}

Clear-Host
Write-Host ''
Write-Host '  ===============================================' -ForegroundColor Cyan
Write-Host '   NUEVA SOLICITUD - Roadmap Plataforma CIMELEC' -ForegroundColor Cyan
Write-Host '  ===============================================' -ForegroundColor Cyan

gh auth status 2>&1 | Out-Null
if (-not $?) {
  Write-Host ''
  Write-Host '  No estas conectado a GitHub. Corre:  gh auth login' -ForegroundColor Red
  Write-Host ''
  Read-Host '  Enter para salir'
  exit 1
}

# ------------------------------------------------------------------- TIPO ----
$tipo = Menu 'Que es?' @(
  @{ texto = 'Una mejora (existe pero puede quedar mejor)'; label = 'tipo: mejora'; pre = 'Mejora'; estado = 'estado: idea' },
  @{ texto = 'Un error (no funciona o el dato esta mal)';   label = 'tipo: error';  pre = 'Error';  estado = 'estado: en analisis' },
  @{ texto = 'Una idea nueva (no existe todavia)';          label = 'tipo: idea';   pre = 'Idea';   estado = 'estado: idea' }
)

# --------------------------------------------------------------- HERRAMIENTA ----
$app = Menu 'En que herramienta?' @(
  @{ texto = 'Tablero DataMart';                  label = 'app: datamart';    nombre = 'Tablero DataMart' },
  @{ texto = 'Bitacora de Obra';                  label = 'app: bitacora';    nombre = 'Bitacora de Obra' },
  @{ texto = 'Registro de Horarios';              label = 'app: horarios';    nombre = 'Registro de Horarios' },
  @{ texto = 'Portal de Proveedores';             label = 'app: proveedores'; nombre = 'Portal de Proveedores' },
  @{ texto = 'Gestion de Proyectos';              label = 'app: proyectos';   nombre = 'Gestion de Proyectos' },
  @{ texto = 'Biblioteca de Informes';            label = 'app: biblioteca';  nombre = 'Biblioteca de Informes' },
  @{ texto = 'Consulta Geografica';               label = 'app: geo';         nombre = 'Consulta Geografica' },
  @{ texto = 'Asistente por WhatsApp';            label = 'app: asistente';   nombre = 'Asistente de consulta' },
  @{ texto = 'Menu de entrada';                   label = 'app: menu';        nombre = 'Menu de entrada' },
  @{ texto = 'Varias / transversal';              label = 'app: plataforma';  nombre = 'Plataforma' }
)

# --------------------------------------------------------------- PRIORIDAD ----
$pri = Menu 'Que prioridad?' @(
  @{ texto = 'ALTA  - cifra mala, caido, o bloquea a un area'; label = 'prioridad: alta' },
  @{ texto = 'MEDIA - molesta a varios todos los dias';        label = 'prioridad: media' },
  @{ texto = 'BAJA  - comodidad, o una sola persona';          label = 'prioridad: baja' }
)

# -------------------------------------------------------------- CONTENIDO ----
Write-Host ''
Write-Host '  Ahora el contenido' -ForegroundColor Cyan
Write-Host ''
$solicitante = Preguntar 'Quien lo pidio (nombre y area)'
$canal       = Preguntar 'Por donde llego (WhatsApp / correo / reunion)'
$titulo      = Preguntar 'Titulo en una linea'

Write-Host ''
if ($tipo.pre -eq 'Error') {
  $c1 = Preguntar 'Que estaba haciendo'
  $c2 = Preguntar 'Que esperaba ver'
  $c3 = Preguntar 'Que paso en realidad'
  $cuerpoDetalle = @"
### Que estaba haciendo
$c1

### Que esperaba ver
$c2

### Que paso en realidad
$c3
"@
} else {
  $c1 = Preguntar 'Que pasa hoy / que problema hay'
  $c2 = Preguntar 'Que quisiera que pasara'
  $c3 = Preguntar 'A cuanta gente le sirve y cada cuanto' $false
  $cuerpoDetalle = @"
### Que pasa hoy
$c1

### Que quisiera que pasara
$c2

### Alcance
$c3
"@
}

$fecha = Get-Date -Format 'yyyy-MM-dd'
$cuerpo = @"
> **Solicitud registrada por el equipo.** La pidio **$solicitante** por $canal el $fecha.
> Se registra aqui para que quede el seguimiento; el solicitante no tiene cuenta de GitHub.

**Herramienta:** $($app.nombre)

$cuerpoDetalle
"@

$tmp = Join-Path $env:TEMP "solicitud_$(Get-Date -Format 'yyyyMMddHHmmss').md"
Set-Content -Path $tmp -Value $cuerpo -Encoding utf8

Write-Host ''
Write-Host '  Creando la solicitud...' -ForegroundColor Cyan

$url = gh issue create --repo $REPO `
  --title "[$($tipo.pre)] $titulo" `
  --body-file $tmp `
  --label $tipo.label `
  --label $app.label `
  --label $pri.label `
  --label $tipo.estado

Remove-Item $tmp -Force -ErrorAction SilentlyContinue

if ($?) {
  Write-Host ''
  Write-Host '  Registrada.' -ForegroundColor Green
  Write-Host ''
  Write-Host "  $url" -ForegroundColor White
  Write-Host ''
  Write-Host '  Copia ese enlace y mandaselo a quien lo pidio.' -ForegroundColor DarkGray
  Write-Host '  Falta un paso a mano: agregarla al tablero (Projects) para que salga en la hoja de ruta.' -ForegroundColor Yellow
} else {
  Write-Host ''
  Write-Host '  No se pudo crear. Revisa el mensaje de arriba.' -ForegroundColor Red
}

Write-Host ''
Read-Host '  Enter para cerrar'
