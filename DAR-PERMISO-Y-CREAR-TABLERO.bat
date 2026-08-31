@echo off
chcp 65001 >nul
title Permiso de tableros + crear el tablero - Roadmap CIMELEC
cd /d "%~dp0"

echo.
echo   ============================================================
echo    PASO 1 de 2 - Autorizar el permiso de tableros en GitHub
echo   ============================================================
echo.
echo   Va a aparecer un CODIGO de 8 caracteres (algo como A1B2-C3D4).
echo.
echo    1. Copialo.
echo    2. Dale Enter: se abre el navegador en github.com/login/device
echo    3. Pega el codigo y dale "Continue"
echo    4. Dale "Authorize github"
echo.
echo   Si el navegador no abre solo, entra a mano a:
echo       https://github.com/login/device
echo.
echo   ------------------------------------------------------------
echo.

gh auth refresh -s project

if errorlevel 1 (
  echo.
  echo   No se pudo autorizar. Revisa el mensaje de arriba.
  echo.
  pause
  exit /b 1
)

echo.
echo   Permiso concedido.
echo.
echo   ============================================================
echo    PASO 2 de 2 - Crear el tablero
echo   ============================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\crear-tablero.ps1"
