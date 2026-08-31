@echo off
chcp 65001 >nul
title Publicar actualizacion - Roadmap CIMELEC
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\publicar-actualizacion.ps1"
