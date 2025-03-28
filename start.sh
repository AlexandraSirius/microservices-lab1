#!/bin/bash

echo "🧼 Отключаем SELinux (если включён)..."
sudo setenforce 0 2>/dev/null || true

echo "🚀 Перезапуск проекта..."
docker compose down
docker compose up --build
