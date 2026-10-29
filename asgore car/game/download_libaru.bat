@echo off
chcp 65001 > log.txt
echo ===================================================
echo   Перевірка та встановлення бібліотек для гри
echo ===================================================
echo.

:: Перевірка, чи встановлений Python в системі
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ПОМИЛКА] Python не знайдено в системі!
    echo Будь ласка, встановіть Python та поставте галочку "Add Python to PATH".
    pause
    exit
)

echo [1/4] Оновлення інструменту pip...
python -m pip install --upgrade pip

echo.
echo [2/4] Встановлення бібліотеки sounddevice (для відтворення звуку)...
pip install sounddevice

echo.
echo [3/4] Встановлення бібліотеки soundfile (для читання mp3/wav)...
pip install soundfile

echo.
echo [4/4] Встановлення бібліотеки keyboard (для зчитування клавіш)...
pip install keyboard

echo.
echo ===================================================
echo   Всі сторонні бібліотеки успішно встановлено, які для гри
echo ===================================================
echo.
pause
