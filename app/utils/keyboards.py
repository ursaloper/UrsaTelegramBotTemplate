from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton #WebAppInfo #ReplyKeyboardMarkup, KeyboardButton
#from config import WEB_APP_URL

def get_main_menu_keyboard(is_admin):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Кнопочка1', callback_data='button1'))

    # Для администраторов добавляем специальную кнопку
    if is_admin:
        keyboard.add(InlineKeyboardButton('🤖 Админ меню', callback_data='start_admin_panel'))

    return keyboard

def get_admin_registration_request_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('✅ Разрешить', callback_data='adm_rgstr_accept'), 
                 InlineKeyboardButton('🙅‍♂️ Запретить', callback_data='adm_rgstr_decline'))

    return keyboard