import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Токен бота Telegram
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Настройки MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_NAME = os.getenv('MONGODB_NAME')

# URL веб-приложения
#WEB_APP_URL = os.getenv('WEB_APP_URL')

# Настройки сервера
#SERVER_IP = os.getenv('SERVER_IP')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')

# ID администратора
ADMIN_ID = int(os.getenv('ADMIN_ID'))