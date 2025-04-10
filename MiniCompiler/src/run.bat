@echo off
cd /d "%~dp0"

echo.
echo [1] Compiling all Java files...
javac -cp ".;../lib/antlr-4.13.1-complete.jar" *.java
if errorlevel 1 (
    echo Compilation failed. Check errors above.
    pause
    exit /b
)

echo.
echo [2] Running CompilerMain...
java -cp ".;../lib/antlr-4.13.1-complete.jar" CompilerMain

pause
