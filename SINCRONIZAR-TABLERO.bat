@echo off
chcp 65001 >nul
title Sincronizar el tablero - Roadmap CIMELEC
cd /d "%~dp0"
python "%~dp0scripts\sincronizar_tablero.py"
echo.
pause
