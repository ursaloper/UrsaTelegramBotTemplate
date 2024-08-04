import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_filters
from telebot.util import update_types

from app.bot.handlers import register_all_handlers
from app.utils.logger import setup_logger
from app.utils.exceptions import MyExceptionHandler
from config import BOT_TOKEN
from app.database.mongodb import ensure_indexes  # Импортируем функцию для создания индексов

# Настройка логирования
logger = setup_logger('bot_logger', 'logs/bot.log')

# Инициализация асинхронного бота
bot = AsyncTeleBot(BOT_TOKEN, exception_handler=MyExceptionHandler(logger))

# Регистрация фильтров бота
bot.add_custom_filter(asyncio_filters.StateFilter(bot))

async def start_bot(bot: AsyncTeleBot):
    # Создание необходимых индексов в базе данных
    # или другая работа с БД (SQLAlchemy)
    await ensure_indexes()

    # Регистрация обработчиков команд
    register_all_handlers(bot)
    
    # Удаляем веб-хук, если он был установлен
    await bot.remove_webhook()
    logger.info("Веб-хук Telegram удален.")

    # Запуск поллинга
    await bot.infinity_polling(timeout=20, allowed_updates=update_types)

if __name__ == '__main__':
    asyncio.run(start_bot(bot))
