FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --default-timeout=100 --retries=10 --no-cache-dir -r requirements.txt


COPY . .

# 👉 Скажи Python, что /app — это корень проекта
ENV PYTHONPATH=/app

CMD ["python", "app/main.py"]
