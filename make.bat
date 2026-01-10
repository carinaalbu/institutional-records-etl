@echo off
REM Windows Automation Script (Conda Version)

IF "%1"=="install" GOTO install
IF "%1"=="run" GOTO run
IF "%1"=="clean" GOTO clean
IF "%1"=="all" GOTO all
GOTO help

:install
echo Installing dependencies via Conda...
conda install --yes --file requirements.txt
GOTO end

:run
echo Running ETL pipeline...
python src/etl.py
GOTO end

:clean
echo Cleaning processed directory...
del /Q "data\processed\*"
echo Done.
GOTO end

:all
CALL :install
CALL :run
GOTO end

:help
echo.
echo Usage:
echo   .\make.bat install   - Install dependencies (Conda)
echo   .\make.bat run       - Run the pipeline
echo   .\make.bat clean     - Delete processed files
echo.
GOTO end

:end