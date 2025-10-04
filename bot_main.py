import telebot
from telebot.types import Message
import requests
import os
import sys
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

print("RUNNING:", os.path.abspath(__file__))
print("PYTHON:", sys.executable)

# Получаем переменные из окружения
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/api")
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("ОШИБКА: BOT_TOKEN не найден в переменных окружения!")
    print("Создайте файл .env и добавьте BOT_TOKEN=ваш_токен")
    sys.exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message: Message):
    try:
        data = {
            "user_id": message.from_user.id,
            "username": message.from_user.username
        }
        response = requests.post(API_URL + "/register/", json=data, timeout=10)
        
        if response.status_code == 201:
            # Новый пользователь зарегистрирован
            bot.send_message(message.chat.id, f"Вы успешно зарегистрированы! Ваш уникальный номер: {response.json()['id']}")
        elif response.status_code == 200:
            # Пользователь уже существует
            bot.send_message(message.chat.id, "Вы уже были зарегистрированы ранее!")
        else:
            bot.send_message(message.chat.id, f"Произошла ошибка при регистрации! Код: {response.status_code}")
            print(f"API Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.Timeout:
        bot.send_message(message.chat.id, "⏰ Время ожидания истекло. Попробуйте еще раз.")
        print("Timeout error")
    except Exception as e:
        bot.send_message(message.chat.id, "❌ Произошла неожиданная ошибка. Попробуйте позже.")
        print(f"Unexpected error: {e}")


@bot.message_handler(commands=['myinfo'])
def user_info(message: Message):
    try:
        response = requests.get(f"{API_URL}/user/{message.from_user.id}/", timeout=10)
        
        if response.status_code == 200:
            user_data = response.json()
            bot.reply_to(message, f"📋 Ваша регистрация:\n\n"
                                f"🆔 ID: {user_data['id']}\n"
                                f"👤 Username: {user_data.get('username', 'Не указан')}\n"
                                f"📅 Дата регистрации: {user_data['created_at'][:10]}")
        elif response.status_code == 404:
            bot.send_message(message.chat.id, "❌ Вы не зарегистрированы! Используйте команду /start")
        else:
            bot.send_message(message.chat.id, f"❌ Ошибка сервера! Код: {response.status_code}")
            print(f"API Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.Timeout:
        bot.send_message(message.chat.id, "⏰ Время ожидания истекло. Попробуйте еще раз.")
        print("Timeout error")
    except Exception as e:
        bot.send_message(message.chat.id, "❌ Произошла неожиданная ошибка. Попробуйте позже.")
        print(f"Unexpected error: {e}")


@bot.message_handler(commands=['help'])
def help_command(message: Message):
    help_text = """
🤖 **Доступные команды:**

/start - Регистрация в системе
/myinfo - Показать информацию о регистрации  
/help - Показать это сообщение

📞 **Поддержка:** Если возникают проблемы, попробуйте команду /start еще раз.
    """
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message: Message):
    bot.send_message(message.chat.id, "❓ Неизвестная команда. Используйте /help для списка команд.")


if __name__ == "__main__":
    print("BEFORE POLLING")
    bot.polling(none_stop=True)
