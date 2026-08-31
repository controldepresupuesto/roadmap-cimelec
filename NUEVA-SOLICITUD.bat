@echo off
chcp 65001 >nul
title Nueva solicitud - Roadmap CIMELEC
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\nueva-solicitud.ps1"
