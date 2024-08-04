from telebot.asyncio_handler_backends import State, StatesGroup
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.async_telebot import AsyncTeleBot

from database.mongodb import get_all_users
from utils.excel_export import export_users_to_excel, remove_excel_file

class AdminStates(StatesGroup):
    admin_menu = State()

def register_handlers(bot: AsyncTeleBot):
    @bot.callback_query_handler(func=lambda call: call.data == "start_admin_panel")
    async def handle_admin_menu(call):
        """
        Обработчик для отображения меню администратору.
        """
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📚 Работа с базой данных", callback_data="adm_work_with_db"))
        # Здесь можно добавить дополнительные кнопки для других функций админ-панели, если потребуется.

        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(
            call.message.chat.id,
            "🚪 Вы перешли в панель администратора",
            reply_markup=markup
        )
        await bot.set_state(call.message.from_user.id, AdminStates.admin_menu, call.message.chat.id)

    # Если в будущем потребуется добавить другие функции, можно раскомментировать и использовать:
    # @bot.callback_query_handler(func=lambda call: call.data == "adm_work_with_db")
    # async def handle_work_with_db(call):
    #     markup = InlineKeyboardMarkup()
    #     markup.add(InlineKeyboardButton("📊 Выгрузить базу данных", callback_data="adm_export_db"))
    #
    #     await bot.send_message(
    #         call.message.chat.id,
    #         "📚 Выберите нужную опцию:",
    #         reply_markup=markup
    #     )
    #
    # @bot.callback_query_handler(func=lambda call: call.data == "adm_export_db")
    # async def handle_export_db(call):
    #    await bot.answer_callback_query(call.id, "☑️ Начинаю выгрузку...")
    #    await bot.send_message(call.message.chat.id, "⏳ Выгружаю базу данных, пожалуйста, подождите...")
    #    
    #    users = await get_all_users()
    #    filename = await export_users_to_excel(users)
    #    
    #    if filename:
    #        try:
    #            with open(filename, 'rb') as file:
    #                await bot.send_document(call.message.chat.id, file, caption="ℹ️ Вот информация о всех пользователях")
    #            await remove_excel_file(filename)
    #        except Exception as e:
    #            await bot.send_message(call.message.chat.id, f"❌ Произошла ошибка при отправке файла: {str(e)}")
    #    else:
    #        await bot.send_message(call.message.chat.id, "❌ Произошла ошибка при экспорте базы данных.")