# Запуск

```
uvicorn --host 0.0.0.0 --port 8100 app:app
unicorn --host 0.0.0.0 --port 8100 app:app
gunicorn -b :5000 microblog:app
python run.py runserver
```

# Миграции 

```pyton
python run.py db init
python run.py db migrate
python run.py db upgrade
```
