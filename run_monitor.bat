@echo off
REM Market News Monitor Batch Script
REM This script runs the Python market monitoring tool

setlocal enabledelayedexpansion

REM Set the project directory
set PROJECT_DIR=C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor

REM Change to project directory
cd /d "%PROJECT_DIR%"

REM Run the Python script
python market_news_monitor.py

REM Log execution
echo Market News Monitor executed at %date% %time% >> "%PROJECT_DIR%\execution_log.txt"

endlocal
