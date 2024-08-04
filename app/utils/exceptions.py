from telebot.async_telebot import ExceptionHandler
import logging

class MyExceptionHandler(ExceptionHandler):
    def __init__(self, logger):
        self.logger = logger

    async def handle(self, exception):
        self.logger.error(f"Произошла ошибка: {str(exception)}", exc_info=True)

        # Здесь вы можете добавить дополнительную логику обработки ошибок
        # Например, отправку уведомления администратору или запись в базу данных

        # Пример отправки уведомления администратору (раскомментируйте и настройте при необходимости)
        # admin_id = your_admin_id_here
        # await bot.send_message(admin_id, f"Произошла ошибка в боте: {str(exception)}")
