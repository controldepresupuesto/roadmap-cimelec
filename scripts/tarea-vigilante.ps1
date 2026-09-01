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

# Lo que se construyo y todavia no esta contado en el roadmap. Sale del historial de los
# repositorios, que es el registro fiable de lo que se hizo. No publica nada: deja la lista.
& python (Join-Path $RAIZ 'scripts\proponer_desde_commits.py') | Out-Null
$porContar = $LASTEXITCODE   # 1 = hay candidatos

$avisoPath = Join-Path $RAIZ '_VIGILANTE-AVISO.txt'
$aviso = ''
if (Test-Path $avisoPath) { $aviso = (Get-Content $avisoPath -Raw -Encoding UTF8).Trim() }

if ($codigo -eq 2) {
  Avisar 'Roadmap CIMELEC - el vigilante fallo' 'No se pudo revisar el roadmap. Mira _VIGILANTE-ROADMAP.txt'
}
elseif ($codigo -eq 1 -and $aviso) {
  # Se corta para que quepa en el globo de Windows
  if ($aviso.Length -gt 200) { $aviso = $aviso.Substring(0, 197) + '...' }
  $extra = ''
  if ($porContar -eq 1) { $extra = "`nY hay cambios construidos sin contar: _PROPUESTAS-ROADMAP.md" }
  Avisar 'Roadmap CIMELEC - hay algo pendiente' ($aviso + "`n`nDetalle en _VIGILANTE-ROADMAP.txt" + $extra)
}
elseif ($porContar -eq 1) {
  Avisar 'Roadmap CIMELEC - hay cambios sin contar' `
    ("Se construyeron cosas que no estan en la hoja de ruta.`n`n" +
     "La lista esta en _PROPUESTAS-ROADMAP.md. Nada se publico: marca lo que quieras que entre.")
}
# Si no hay nada que exija accion ni nada por contar, no molesta.
# El informe y la lista quedan escritos igual.

exit 0
