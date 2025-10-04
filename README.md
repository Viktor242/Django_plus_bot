# 🤖 Django + Telegram Bot

Полнофункциональный проект, объединяющий Django REST API с Telegram ботом для управления пользователями.

## 🚀 Возможности

- **Django REST API** для управления пользователями
- **Telegram бот** с интерактивными командами
- **Безопасность** - токены и секреты в переменных окружения
- **База данных** SQLite с моделями пользователей
- **Обработка ошибок** с понятными сообщениями

## 📋 Команды бота

- `/start` - Регистрация пользователя в системе
- `/myinfo` - Просмотр информации о пользователе
- `/help` - Список доступных команд

## 🛠️ Технологии

- **Backend:** Django 5.2.6, Django REST Framework
- **Bot:** pyTelegramBotAPI (telebot)
- **Database:** SQLite
- **Environment:** python-dotenv

## 📦 Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone <repository-url>
   cd Django_plus_bot_DJ07
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройте переменные окружения:**
   Создайте файл `.env` в корне проекта:
   ```env
   BOT_TOKEN=ваш_telegram_bot_token
   API_URL=http://127.0.0.1:8000/api
   DJANGO_SECRET_KEY=ваш_secret_key
   ```

4. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```

## 🚀 Запуск

1. **Запустите Django сервер:**
   ```bash
   python manage.py runserver
   ```

2. **Запустите Telegram бота:**
   ```bash
   python bot_main.py
   ```

## 📡 API Endpoints

### Регистрация пользователя
```http
POST /api/register/
Content-Type: application/json

{
  "user_id": 123456789,
  "username": "john_doe"
}
```

### Получение информации о пользователе
```http
GET /api/user/{user_id}/
```

## 🧪 Тестирование API

Используйте любой API клиент (Postman, Boomerang, curl):

```bash
# Регистрация
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 123, "username": "test"}'

# Получение информации
curl http://127.0.0.1:8000/api/user/123/
```

## 📁 Структура проекта

```
Django_plus_bot_DJ07/
├── bot/                    # Django приложение
│   ├── models.py          # Модель TelegramUser
│   ├── views.py           # API views
│   ├── urls.py            # URL маршруты
│   └── serializers.py     # DRF сериализаторы
├── djangobot/             # Настройки Django
├── bot_main.py            # Telegram бот
├── .env                   # Переменные окружения
├── requirements.txt       # Зависимости
└── README.md             # Документация
```

## 🔧 Конфигурация

### Переменные окружения (.env)
- `BOT_TOKEN` - токен Telegram бота от @BotFather
- `API_URL` - URL Django API (по умолчанию: http://127.0.0.1:8000/api)
- `DJANGO_SECRET_KEY` - секретный ключ Django

### Django Settings
- База данных: SQLite (db.sqlite3)
- Debug режим: включен
- CORS: настроен для локальной разработки

## 🐛 Обработка ошибок

Бот обрабатывает следующие ошибки:
- **ConnectionError** - сервер недоступен
- **Timeout** - превышено время ожидания
- **API ошибки** - неправильные HTTP коды
- **Неожиданные ошибки** - любые другие исключения

## 📊 Примеры использования

### Успешная регистрация
```json
{
  "id": 1,
  "user_id": 123456789,
  "username": "john_doe",
  "created_at": "2025-10-04T12:00:00Z"
}
```

### Пользователь уже существует
```json
{
  "message": "User is already registered"
}
```

## 🔒 Безопасность

- ✅ Токены в переменных окружения
- ✅ .env файл исключен из Git
- ✅ Валидация входных данных
- ✅ Обработка ошибок без утечки информации

## 📝 Лицензия

Этот проект распространяется под лицензией MIT.

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request

## 📞 Поддержка

Если у вас есть вопросы или проблемы, создайте Issue в репозитории.