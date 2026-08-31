<#
  publicar-actualizacion.ps1 — anuncia lo que acaba de salir a produccion.

  Hace tres cosas de una:
    1. Agrega la entrada al principio del CHANGELOG.md
    2. Commitea y sube el cambio
    3. Crea el Release en GitHub con la misma nota
#>

$ErrorActionPreference = 'Stop'
$REPO = 'controldepresupuesto/roadmap-cimelec'
$RAIZ = Split-Path -Parent $PSScriptRoot
$CHANGELOG = Join-Path $RAIZ 'CHANGELOG.md'

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
Write-Host '  ==================================================' -ForegroundColor Cyan
Write-Host '   PUBLICAR ACTUALIZACION - Roadmap Plataforma' -ForegroundColor Cyan
Write-Host '  ==================================================' -ForegroundColor Cyan

if (-not (Test-Path $CHANGELOG)) {
  Write-Host ''
  Write-Host "  No encuentro $CHANGELOG" -ForegroundColor Red
  Read-Host '  Enter para salir'
  exit 1
}

$hoy = Get-Date -Format 'yyyy-MM-dd'
Write-Host ''
$fecha = Read-Host "  Fecha de la publicacion [$hoy]"
if (-not $fecha) { $fecha = $hoy }

$bloques = @()

do {
  $app = Menu 'Herramienta que se actualizo' @(
    @{ texto = 'Tablero DataMart';       nombre = 'Tablero DataMart' },
    @{ texto = 'Bitacora de Obra';       nombre = 'Bitácora de Obra' },
    @{ texto = 'Registro de Horarios';   nombre = 'Registro de Horarios' },
    @{ texto = 'Portal de Proveedores';  nombre = 'Portal de Proveedores' },
    @{ texto = 'Gestion de Proyectos';   nombre = 'Gestión de Proyectos' },
    @{ texto = 'Biblioteca de Informes'; nombre = 'Biblioteca de Informes' },
    @{ texto = 'Consulta Geografica';    nombre = 'Consulta Geográfica' },
    @{ texto = 'Asistente por WhatsApp'; nombre = 'Asistente de consulta' },
    @{ texto = 'Menu de entrada';        nombre = 'Menú de entrada' },
    @{ texto = 'Varias / plataforma';    nombre = 'Plataforma' }
  )

  Write-Host ''
  Write-Host '  Escribe los cambios uno por linea. Enter vacio para terminar esta herramienta.' -ForegroundColor DarkGray
  Write-Host '  Antepon el tipo:  n = nuevo   m = mejorado   c = corregido   a = aviso/cambio' -ForegroundColor DarkGray
  Write-Host '  Ejemplo:  c El total facturado sumaba dos veces las notas credito' -ForegroundColor DarkGray
  Write-Host ''

  $lineas = @()
  while ($true) {
    $l = Read-Host '  >'
    if (-not $l) { break }
    $marca = '🔧'
    $texto = $l
    if ($l.Length -gt 2 -and $l.Substring(1, 1) -eq ' ') {
      $t = $l.Substring(0, 1).ToLower()
      $texto = $l.Substring(2)
      if ($t -eq 'n') { $marca = '✨' }
      if ($t -eq 'm') { $marca = '🔧' }
      if ($t -eq 'c') { $marca = '🐞' }
      if ($t -eq 'a') { $marca = '⚠️' }
    }
    if ($texto -notmatch '[.!?]$') { $texto = "$texto." }
    $lineas += "- $marca $texto"
  }

  if ($lineas.Count -gt 0) {
    $bloques += "**$($app.nombre)**`n" + ($lineas -join "`n")
  } else {
    Write-Host '  (sin cambios, se omite)' -ForegroundColor Yellow
  }

  Write-Host ''
  $mas = Read-Host '  Otra herramienta en esta misma publicacion? (s/n)'
} while ($mas -eq 's' -or $mas -eq 'S')

if ($bloques.Count -eq 0) {
  Write-Host ''
  Write-Host '  No escribiste ningun cambio. Nada que publicar.' -ForegroundColor Yellow
  Read-Host '  Enter para salir'
  exit 0
}

$entrada = "## $fecha`n`n" + ($bloques -join "`n`n") + "`n`n---`n"

Write-Host ''
Write-Host '  --------- ASI VA A QUEDAR ---------' -ForegroundColor Cyan
Write-Host $entrada
Write-Host '  -----------------------------------' -ForegroundColor Cyan
Write-Host ''
$ok = Read-Host '  Publicar? (s/n)'
if ($ok -ne 's' -and $ok -ne 'S') {
  Write-Host '  Cancelado. No se toco nada.' -ForegroundColor Yellow
  Read-Host '  Enter para salir'
  exit 0
}

# ------------------------------------------------- 1. meter en el CHANGELOG ----
$actual = Get-Content $CHANGELOG -Raw -Encoding UTF8
$marcador = "---`r`n"
$i = $actual.IndexOf($marcador)
if ($i -lt 0) {
  $marcador = "---`n"
  $i = $actual.IndexOf($marcador)
}
if ($i -lt 0) {
  Write-Host '  No encuentro el separador --- en el CHANGELOG. Lo agrego al final.' -ForegroundColor Yellow
  $nuevo = $actual + "`n" + $entrada
} else {
  $corte = $i + $marcador.Length
  $nuevo = $actual.Substring(0, $corte) + "`n" + $entrada + $actual.Substring($corte)
}
Set-Content -Path $CHANGELOG -Value $nuevo -Encoding utf8
Write-Host '  CHANGELOG.md actualizado' -ForegroundColor Green

# ---------------------------------------------------------- 2. git y push ----
Push-Location $RAIZ
git add CHANGELOG.md
git commit -m "Actualizacion $fecha"
if ($?) {
  git push
  if ($?) { Write-Host '  Subido a GitHub' -ForegroundColor Green }
  else    { Write-Host '  El push fallo. Revisa arriba.' -ForegroundColor Red }
}
Pop-Location

# -------------------------------------------------------------- 3. Release ----
$tag = "v$($fecha.Replace('-', '.'))"
$notas = ($bloques -join "`n`n")
$tmp = Join-Path $env:TEMP "release_$tag.md"
Set-Content -Path $tmp -Value $notas -Encoding utf8

gh release create $tag --repo $REPO --title "Actualizacion $fecha" --notes-file $tmp
if ($?) { Write-Host "  Release $tag creado" -ForegroundColor Green }
else    { Write-Host "  El release fallo (puede que el tag $tag ya exista)" -ForegroundColor Yellow }
Remove-Item $tmp -Force -ErrorAction SilentlyContinue

Write-Host ''
Write-Host '  Listo. Falta cerrar los issues que salieron en esta version' -ForegroundColor Yellow
Write-Host "  y mencionarles el tag $tag." -ForegroundColor Yellow
Write-Host ''
Read-Host '  Enter para cerrar'
