Моисеева Александра Сергеевна, к0611-23
# Лабораторная работа №1: Микросервисы (FastAPI + Docker + NGINX)

## Цель

- Реализация REST API-сервера на FastAPI
- Балансировка нагрузки с помощью NGINX
- Упаковка приложения в Docker
- Запуск проекта с использованием Docker Compose



## Структура проекта


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


## Запуск проекта

1. Установить Docker и Docker Compose
2. Запустить проект:

    ./start.sh

или

    make up


3. Проверка:

- http://localhost/api/v1/contact
- http://localhost/api/v1/group

4. Остановка:

    make down

