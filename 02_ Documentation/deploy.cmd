@echo off
SETLOCAL EnableDelayedExpansion

:: --- Configuration ---
SET VENV_DIR=..\venv
SET REQ_FILE=..\requirements.txt
SET PYTHON_EXE=python

echo [1/5] Checking Python version (Targeting 3.14)...
%PYTHON_EXE% --version

echo [2/5] Creating Virtual Environment in %VENV_DIR%...
if not exist "%VENV_DIR%" (
    %PYTHON_EXE% -m venv "%VENV_DIR%"
) else (
    echo Virtual environment already exists.
)

echo [3/5] Activating Virtual Environment and Upgrading Pip...
call "%VENV_DIR%\Scripts\activate"
python -m pip install --upgrade pip

echo [4/5] Installing Dependencies from %REQ_FILE%...
pip install -r "%REQ_FILE%"

echo [5/5] Initializing Playwright and Ollama models...
playwright install chromium
echo Pulling Llama 3.2 (3B) for Sentiment...
ollama pull llama3.2:3b-instruct-q4_K_M
rem echo Pulling Mistral Nemo (12B) for Intelligence...
rem ollama pull mistral-nemo:12b-instruct-v1-q4_K_M

echo.
echo ===================================================
echo Deployment Complete! 
echo To start work, run: call venv\Scripts\activate
echo ===================================================
pause
