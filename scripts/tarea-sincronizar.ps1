<#
  tarea-sincronizar.ps1 — lo que corre la tarea programada cada 10 minutos.

  Nadie tiene que ejecutar esto a mano: la tarea "Roadmap CIMELEC - Sincronizar tablero" lo
  llama sola. Cambias una etiqueta en una solicitud y a los pocos minutos el tablero se acomoda.

  POR QUE AQUI Y NO EN GITHUB ACTIONS
  Actions no puede escribir en el tablero con su token automatico (el GITHUB_TOKEN no alcanza a
  Projects v2), y como el tablero es de una cuenta personal tampoco sirve una GitHub App. Haria
  falta crear un token nuevo a mano. En cambio el gh de esta maquina YA esta autorizado con el
  permiso 'project', asi que aqui funciona sin crear nada.
  El flujo de Actions (.github/workflows/sincronizar-tablero.yml) queda listo para el dia que se
  quiera mover alla: solo le falta el secreto.

  QUE ESCRIBE
    sincronizacion.log            historial, solo cuando hubo cambios o fallos
    _estado-sincronizacion.txt    latido: cuando corrio por ultima vez y como salio
#>

$ErrorActionPreference = 'Continue'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RAIZ    = Split-Path -Parent $PSScriptRoot
$LOG     = Join-Path $RAIZ 'sincronizacion.log'
$LATIDO  = Join-Path $RAIZ '_estado-sincronizacion.txt'
$SELLO   = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'

Set-Location $RAIZ

function Correr($script) {
  $salida = & python (Join-Path $RAIZ ('scripts\' + $script)) 2>&1 | Out-String
  return @{ ok = ($LASTEXITCODE -eq 0); salida = $salida.TrimEnd() }
}

$sync = Correr 'sincronizar_tablero.py'
$audi = Correr 'auditar_etiquetas.py'

# Solo interesa dejar rastro cuando algo cambio o algo fallo. Si no, el log se vuelve ilegible.
$huboCambios = $sync.salida -notmatch '0 solicitudes agregadas, 0 valores fijados'
$huboFallo   = (-not $sync.ok) -or (-not $audi.ok)

if ($huboFallo -or $huboCambios) {
  $bloque = @()
  $bloque += ''
  $bloque += '=' * 78
  if ($huboFallo) { $bloque += "$SELLO   FALLO" } else { $bloque += "$SELLO   cambios aplicados" }
  $bloque += '=' * 78
  $bloque += $sync.salida
  if (-not $audi.ok) {
    $bloque += ''
    $bloque += '--- auditoria de etiquetas ---'
    $bloque += $audi.salida
  }
  Add-Content -Path $LOG -Value ($bloque -join "`r`n") -Encoding utf8

  # El log no crece para siempre: se queda con las ultimas 900 lineas.
  if (Test-Path $LOG) {
    $lineas = Get-Content $LOG
    if ($lineas.Count -gt 900) {
      Set-Content -Path $LOG -Value ($lineas[-900..-1]) -Encoding utf8
    }
  }
}

# El latido se escribe SIEMPRE. Si este archivo se queda viejo, la sincronizacion esta muerta:
# es la senal que va a leer el vigilante, y la que se puede mirar a ojo.
$estado = if ($huboFallo) { 'FALLO' } elseif ($huboCambios) { 'cambios aplicados' } else { 'sin cambios' }
$resumen = @(
  "Ultima sincronizacion: $SELLO"
  "Resultado:             $estado"
  ""
  "Tablero:  https://github.com/users/controldepresupuesto/projects/1"
  "Vitrina:  https://github.com/controldepresupuesto/roadmap-cimelec"
  ""
  "--- ultima salida del sincronizador ---"
  $sync.salida
  ""
  "--- ultima salida del auditor de etiquetas ---"
  $audi.salida
) -join "`r`n"
Set-Content -Path $LATIDO -Value $resumen -Encoding utf8

if ($huboFallo) { exit 1 }
exit 0
