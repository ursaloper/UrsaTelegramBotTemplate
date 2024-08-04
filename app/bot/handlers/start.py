"""
Модуль обработчиков для команды /start.
"""

import os
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, ReplyKeyboardRemove
from database.mongodb import get_user, create_user
from utils.keyboards import get_main_menu_keyboard, get_admin_registration_request_keyboard
from config import ADMIN_ID

def register_handlers(bot: AsyncTeleBot):
    """
    Регистрация обработчиков сообщений для бота.
    
    :param bot: Экземпляр асинхронного телеграм-бота.
    """
    @bot.message_handler(commands=['start'])
    async def handle_start(message: Message):
        """
        Обработчик команды /start.

        :param message: Сообщение с командой /start.
        """
        if message.chat.type == 'private':
            user_id = message.from_user.id
            chat_id = message.chat.id

            # Удаление клавиатуры (если нужно)
            # remove_keyboard = ReplyKeyboardRemove()
            # await bot.send_message(user_id, f'Клавиатура удалена', reply_markup=remove_keyboard)

            user = await get_user(user_id)  # Асинхронный вызов функции из базы данных

            # Версия 1: Автоматическая регистрация пользователя
            """
            if user:
                if chat_id == ADMIN_ID:
                    text = "Калькулятор размера позиции и прибыли\n\n[ПРАВА АДМИНИСТРАТОРА]"
                    keyboard = get_main_menu_keyboard(True)
                else:
                    text = "Калькулятор размера позиции и прибыли"
                    keyboard = get_main_menu_keyboard(user['is_admin'])
            else:
                # Создание нового пользователя
                user_photo = await fetch_user_photo(bot, user_id)
                user = await create_user(
                    user_id,
                    message.from_user.username,
                    message.from_user.first_name,
                    message.from_user.last_name,
                    user_photo
                )
                keyboard = get_main_menu_keyboard(user['is_admin'])
                text = "Калькулятор размера позиции и прибыли"
            """

            # Версия 2: Запрос на подтверждение от администратора
            if user:
                if chat_id == ADMIN_ID:
                    text = "Калькулятор размера позиции и прибыли\n\n[ПРАВА АДМИНИСТРАТОРА]"
                    keyboard = get_main_menu_keyboard(True)
                else:
                    text = "Калькулятор размера позиции и прибыли"
                    keyboard = get_main_menu_keyboard(user['is_admin'])
            else:
                # Уведомление администратора о новой регистрации
                await bot.send_message(ADMIN_ID, f"Пользователь {message.from_user.first_name} ({user_id}) запрашивает доступ к боту.", reply_markup=get_admin_registration_request_keyboard())
                await bot.send_message(chat_id, "Ваш запрос на доступ к боту отправлен администратору. Ожидайте подтверждения.")

                # Завершение функции, так как пользователь не зарегистрирован
                return

            # Отправка изображения с подписью
            image_path = os.path.join('static', 'images', 'start_image.png')
            with open(image_path, 'rb') as photo:
                await bot.send_photo(chat_id, photo, caption=text, reply_markup=keyboard)

async def fetch_user_photo(bot, user_id):
    """
    Получение фото профиля пользователя.

    :param bot: Экземпляр асинхронного телеграм-бота.
    :param user_id: Идентификатор пользователя.
    :return: Идентификатор файла фото профиля или None в случае ошибки.
    """
    try:
        user_profile_photos = await bot.get_user_profile_photos(user_id, limit=1)
        if user_profile_photos.total_count > 0:
            return user_profile_photos.photos[0][-1].file_id
    except Exception as e:
        print(f"Не удалось получить фото профиля пользователя: {str(e)}")
    return None
