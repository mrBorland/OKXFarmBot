#!/bin/bash

# Налаштування
REPO_URL="https://github.com/mrBorland/OKXFarmBot.git"
COMMIT_MSG="💥 Full sync: Autonomous OKXFarmBot"
GIT_USERNAME="mrBorland"
GIT_EMAIL="youremail@example.com"  # заміни на свою пошту

# Переходимо в папку з проєктом
cd /root/OKXFarmBot || exit

# Очищення старого git, якщо був криво ініціалізований
rm -rf .git

# Повна ініціалізація
git init
git config user.name "$GIT_USERNAME"
git config user.email "$GIT_EMAIL"
git remote add origin "$REPO_URL"

# Додавання і пуш
git add .
git commit -m "$COMMIT_MSG"
git branch -M main
git push -u origin main --force
