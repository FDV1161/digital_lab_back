# Запуск

```
uvicorn --host 0.0.0.0 --port 8100 app:app
unicorn --host 0.0.0.0 --port 8100 app:app
gunicorn -b 0.0.0.0:8000 app:app
python run.py runserver
```

# Миграции 

```pyton
python run.py db init
python run.py db migrate
python run.py db upgrade
```

# Deploy 

Использовалась статья: [Мега-Учебник Flask, Часть XVII: Развертывание под Linux](https://habr.com/ru/post/352266/)