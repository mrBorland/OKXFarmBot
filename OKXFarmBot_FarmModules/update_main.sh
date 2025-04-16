#!/bin/bash

cd ~/OKXFarmBot || exit

echo "Додаємо всі файли..."
git add .

echo "Комітимо зміни..."
git commit -m "Автоматичне оновлення всіх файлів"

echo "Пушимо на GitHub..."
git push origin main

echo "Готово!"
