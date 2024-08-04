def format_profile(user_data):
    first_name = user_data.get('first_name', 'Не указано')
    last_name = user_data.get('last_name', ' ')
    username = user_data.get('username', 'None')
    registration_date = user_data.get('registration_date', 'Не указано')
    is_admin = 'Да' if user_data.get('is_admin', False) else 'Нет'
    is_blocked = 'Да' if user_data.get('is_blocked', False) else 'Нет'

    return f"""
👤 *Профиль пользователя*:

🔸 *Имя*: {first_name} {last_name}
🔸 *Ник*: @{username}
🔸 *Дата регистрации*: {registration_date}
    """

