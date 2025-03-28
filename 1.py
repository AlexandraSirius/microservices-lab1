
import os

project_path = os.path.dirname(os.path.abspath(__file__))

files_to_create = {
    "README.md": '''# Лабораторная работа №1: Микросервисы (FastAPI + Docker + NGINX)

## 📌 Цель

- Реализация REST API-сервера на FastAPI
- Балансировка нагрузки с помощью NGINX
- Упаковка приложения в Docker
- Запуск проекта с использованием Docker Compose

---

## 📁 Структура проекта

```
microservices_lab1/
├── app/
│   ├── main.py
│   ├── contact.py
│   └── group.py
├── docker/
├── nginx/
├── nginx_conf_runtime/
├── docker-compose.yml
├── Makefile
├── start.sh
└── README.md
```

---

## 🚀 Запуск проекта

1. Установить Docker и Docker Compose
2. Запустить проект:

```bash
./start.sh
```

или

```bash
make up
```

3. Проверка:

- http://localhost/api/v1/contact
- http://localhost/api/v1/group

4. Остановка:

```bash
make down
```
''',

    "Makefile": '''up:
\tdocker compose up --build

down:
\tdocker compose down

logs:
\tdocker compose logs -f

ps:
\tdocker compose ps
''',

    "start.sh": '''#!/bin/bash

echo "🧼 Отключаем SELinux (если включён)..."
sudo setenforce 0 2>/dev/null || true

echo "🚀 Перезапуск проекта..."
docker compose down
docker compose up --build
'''
}

def create_meta_files():
    for filename, content in files_to_create.items():
        path = os.path.join(project_path, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        if filename == "start.sh":
            os.chmod(path, 0o755)
    print("✅ Файлы README.md, Makefile и start.sh успешно созданы.")

if __name__ == "__main__":
    create_meta_files()
