@echo off
cd /d %~dp0

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python wurde nicht gefunden. Es wird jetzt automatisch heruntergeladen und installiert...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe' -OutFile 'python_installer.exe'"
    echo Installation laeuft, bitte kurz warten...
    python_installer.exe /quiet InstallAllUsers=0 PrependPath=1
    del python_installer.exe
    echo.
    echo Python wurde installiert!
    echo Bitte dieses Fenster schliessen und Start.bat NOCHMAL doppelklicken.
    pause
    exit
)

python age_check.py
pause
