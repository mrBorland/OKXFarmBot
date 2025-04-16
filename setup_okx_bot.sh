#!/bin/bash

echo "=== [1] Створення та активація venv ==="
python3 -m venv venv
source venv/bin/activate

echo "=== [2] Встановлення OKX SDK через GitHub токен ==="
pip install --upgrade pip
pip install git+https://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@github.com/okxapi/okx-api-sdk-python.git

echo "=== [3] Перевірка наявності test_balance.py ==="
if [ -f "test_balance.py" ]; then
    echo "Файл знайдено. Запуск..."
    python3 test_balance.py
else
    echo "Файл test_balance.py не знайдено. Створи його вручну."
fi
