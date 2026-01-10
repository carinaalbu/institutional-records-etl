@echo off
REM Windows Automation Pipeline

IF "%1"=="install" GOTO install
IF "%1"=="run" GOTO run
IF "%1"=="clean" GOTO clean
IF "%1"=="all" GOTO all
GOTO help

:install
echo [1/4] Installing dependencies...
conda install --yes --file requirements.txt
GOTO end

:run
echo [2/4] Verifying Data Integrity...
python src/checksum.py verify
IF %ERRORLEVEL% NEQ 0 (
    echo INTEGRITY CHECK FAILED. Stopping pipeline.
    EXIT /B 1
)

echo [3/4] Running ETL Cleaning...
python src/etl.py
IF %ERRORLEVEL% NEQ 0 (
    echo ETL FAILED. Stopping pipeline.
    EXIT /B 1
)

echo [4/4] Generating Analysis Report...
python src/analyze.py
echo PIPELINE COMPLETE SUCCESS.
GOTO end

:clean
echo Cleaning processed data and reports...
del /Q "data\processed\*"
del /Q "reports\pipeline_summary.txt"
echo Done.
GOTO end

:all
CALL :install
CALL :run
GOTO end

:help
echo.
echo Usage:
echo   .\make.bat all       - Install + Verify + Clean + Report
echo   .\make.bat run       - Verify + Clean + Report
echo   .\make.bat clean     - Delete outputs
echo.
GOTO end

:end