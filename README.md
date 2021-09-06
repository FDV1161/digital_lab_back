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

# Авторизация 

При работе с api используется `Bearer Token`. Для получения токена нужно отправить `get` запрос на url: `/token` с указанием логина и пароля в `Basic Auth`

Для отзыва токена на тотже адрес отправляется `delete` запрос