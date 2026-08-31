@echo off
chcp 65001 >nul
title Guardar cambios - Roadmap CIMELEC
cd /d "%~dp0"
echo.
set /p MSG="  Que cambiaste? "
if "%MSG%"=="" set MSG=Ajustes
git add -A
git commit -m "%MSG%"
git push
echo.
pause
