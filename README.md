# OnlineBooks Project

## Запуск проекта

1. Backend:
```bash
cd backend
source env/bin/activate
cd app
uvicorn main:app --reload --port 8001
```

2. Authors API:
```bash
cd AuthorsApi
source env/bin/activate
cd app
uvicorn main:app --reload --port 8000
```

3. Frontend:
```bash
cd frontend
npm run dev
```

4. Email Service:
```bash
cd EmailService
source env/bin/activate
python3 app.py
```

## Скриншот проекта
![Описание изображения](docs/api.png)