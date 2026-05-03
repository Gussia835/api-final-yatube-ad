# API для Yatube

REST API для платформы микроблогов Yatube. Позволяет публиковать записи, комментировать их, объединять в тематические группы и подписываться на авторов. Предназначен для взаимодействия с фронтенд-приложением (SPA) или мобильными клиентами.

## Технологии
- Python 3.12
- Django 3.2
- Django REST Framework 3.12
- Djoser + djangorestframework-simplejwt (JWT-аутентификация)
- pytest (тестирование)

## Установка
1. Клонируйте репозиторий и перейдите в папку проекта:
```bash
git clone <url-вашего-репозитория>
cd api-final-yatube-ad
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

Сервер будет доступен по адресу: http://127.0.0.1:8000

## Примеры запросов
Для запросов, требующих авторизации, передавайте заголовок: `Authorization: Bearer <ваш_токен>`

### Получение JWT-токена
```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
"username": "testuser",
"password": "SecurePass123!"
}
```

### Создание публикации
```http
POST /api/v1/posts/
Authorization: Bearer <ваш_токен>
Content-Type: application/json

{
  "text": "Изучаю Django REST Framework",
  "group": 1
}
```

### Подписка на автора
```http
POST /api/v1/follow/
Authorization: Bearer <ваш_токен>
Content-Type: application/json

{
  "following": "username_автора"
}
```

## Документация
Интерактивная документация API (Redoc) доступна после запуска сервера по адресу:  
http://127.0.0.1:8000/redoc/