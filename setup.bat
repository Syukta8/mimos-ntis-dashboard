@echo off

REM Step 1: Create environment with Python <3.12
echo Creating python environment: NTIS
call python -m venv "%USERPROFILE%\.envs\NTIS"
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to create environment.
    pause
    exit /b %ERRORLEVEL%
)

REM Step 2: Activate environment
echo Activating NTIS environment
call "%USERPROFILE%\.envs\NTIS\Scripts\activate"
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to activate environment.
    pause
    exit /b %ERRORLEVEL%
)

REM Step 3: Install core packages
echo Installing core Python packages via pip
pip install streamlit pandas plotly st-gsheets-connection
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install.
    pause
    exit /b %ERRORLEVEL%
)

