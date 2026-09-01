<#
  tarea-vigilante.ps1 — lo que corre la tarea "Roadmap CIMELEC - Vigilante" los lunes.

  Revisa que el roadmap no se este podriendo y, SOLO si hay algo que exige accion, muestra un
  aviso de escritorio. Mismo patron que check-alertas.ps1 de la VM: sin credenciales, sin correo,
  sin nada que configurar.

  El informe completo queda siempre en _VIGILANTE-ROADMAP.txt, se haya avisado o no.
#>

$ErrorActionPreference = 'Continue'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RAIZ = Split-Path -Parent $PSScriptRoot
Set-Location $RAIZ

function Avisar($titulo, $texto) {
  try {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $n = New-Object System.Windows.Forms.NotifyIcon
    $n.Icon = [System.Drawing.SystemIcons]::Information
    $n.BalloonTipTitle = $titulo
    $n.BalloonTipText  = $texto
    $n.Visible = $true
    $n.ShowBalloonTip(25000)
    Start-Sleep -Seconds 14
    $n.Dispose()
  } catch {}
}

& python (Join-Path $RAIZ 'scripts\vigilante_roadmap.py') | Out-Null
$codigo = $LASTEXITCODE

$avisoPath = Join-Path $RAIZ '_VIGILANTE-AVISO.txt'
$aviso = ''
if (Test-Path $avisoPath) { $aviso = (Get-Content $avisoPath -Raw -Encoding UTF8).Trim() }

if ($codigo -eq 2) {
  Avisar 'Roadmap CIMELEC - el vigilante fallo' 'No se pudo revisar el roadmap. Mira _VIGILANTE-ROADMAP.txt'
}
elseif ($codigo -eq 1 -and $aviso) {
  # Se corta para que quepa en el globo de Windows
  if ($aviso.Length -gt 220) { $aviso = $aviso.Substring(0, 217) + '...' }
  Avisar 'Roadmap CIMELEC - hay algo pendiente' ($aviso + "`n`nEl detalle esta en _VIGILANTE-ROADMAP.txt")
}
# Si no hay nada que exija accion, no molesta. El informe queda escrito igual.

exit 0
