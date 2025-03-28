FROM python:3.11-slim

WORKDIR /app

COPY ./app /app/app
COPY ./app/main.py /app/main.py

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6080"]
