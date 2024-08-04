"""
Модуль для работы с MongoDB.
"""

from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError

from config import MONGODB_URI, MONGODB_NAME
from app.utils.logger import setup_logger

logger = setup_logger('mongodb', 'logs/mongodb.log')

client = AsyncIOMotorClient(MONGODB_URI)
db = client[MONGODB_NAME]

users_collection = db['users']
mailings_collection = db['mailings']

async def ensure_indexes():
    """
    Создание необходимых индексов в базе данных.
    """
    try:
        await db.users.create_index('user_id', unique=True)
        logger.info("Индексы успешно созданы")
    except Exception as e:
        logger.error(f"Ошибка при создании индексов: {str(e)}")

async def get_user(user_id: int):
    """
    Получение пользователя по user_id.

    :param user_id: Идентификатор пользователя.
    :return: Данные пользователя или None.
    """
    try:
        return await db.users.find_one({'user_id': user_id})
    except Exception as e:
        logger.error(f"Ошибка при получении пользователя {user_id}: {str(e)}")
        return None

async def create_user(telegram_id, username, first_name, last_name, photo_id):
    """
    Создание нового пользователя.

    :param telegram_id: Идентификатор пользователя в Telegram.
    :param username: Имя пользователя в Telegram.
    :param first_name: Имя пользователя.
    :param last_name: Фамилия пользователя.
    :param photo_id: Идентификатор фото пользователя.
    :return: Данные созданного пользователя.
    """
    user_data = {
        'user_id': telegram_id,
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'user_photo_id': photo_id,
        'registration_date': datetime.now(),
        'is_admin': False,
        'is_blocked': False,
        'blocked_the_bot': False
    }
    try:
        await db.users.insert_one(user_data)
        logger.info(f"Создан новый пользователь: {telegram_id}")
        return user_data
    except DuplicateKeyError:
        logger.info(f"Пользователь {telegram_id} уже существует")
        return await get_user(telegram_id)
    except Exception as e:
        logger.error(f"Ошибка при создании пользователя {telegram_id}: {str(e)}")
        return None

async def get_all_users():
    """
    Получение всех пользователей.

    :return: Список всех пользователей.
    """
    try:
        cursor = db.users.find({})
        return await cursor.to_list(length=None)
    except Exception as e:
        logger.error(f"Ошибка при получении всех пользователей: {str(e)}")
        return []
    





#######################################################################    

async def update_user_blocked_status(user_id: int, blocked: bool):
    """
    Обновление статуса блокировки пользователя.

    :param user_id: Идентификатор пользователя.
    :param blocked: Новый статус блокировки.
    """
    await db.users.update_one({'user_id': user_id}, {'$set': {'blocked_the_bot': blocked}})

async def create_mailing(admin_id: int, admin_username: str, mailing_data: dict):
    """
    Создание новой рассылки.

    :param admin_id: Идентификатор администратора.
    :param admin_username: Имя пользователя администратора.
    :param mailing_data: Данные рассылки (текст, медиафайлы, кнопки).
    :return: ID созданной рассылки.
    """
    mailing = {
        'admin_id': admin_id,
        'admin_username': admin_username,
        'mailing_data': mailing_data,
        'created_at': datetime.now()
    }
    result = await db.mailings.insert_one(mailing)
    return result.inserted_id

async def get_mailing(mailing_id):
    """
    Получение данных рассылки по ID.

    :param mailing_id: ID рассылки.
    :return: Данные рассылки или None.
    """
    return await db.mailings.find_one({'_id': mailing_id})

async def get_all_admins():
    """
    Получение всех администраторов.

    :return: Список всех администраторов.
    """
    cursor = db.users.find({'is_admin': True})
    return await cursor.to_list(length=None)

async def add_admin(user_id: int):
    """
    Назначение пользователя администратором.

    :param user_id: Идентификатор пользователя.
    :return: True, если пользователь успешно назначен администратором, False в противном случае.
    """
    result = await db.users.update_one(
        {'user_id': user_id},
        {'$set': {'is_admin': True}}
    )
    return result.modified_count > 0

async def remove_admin(user_id: int):
    """
    Удаление пользователя из списка администраторов.

    :param user_id: Идентификатор пользователя.
    :return: True, если пользователь успешно удален из списка администраторов, False в противном случае.
    """
    result = await db.users.update_one(
        {'user_id': user_id},
        {'$set': {'is_admin': False}}
    )
    return result.modified_count > 0

async def is_admin(user_id: int):
    """
    Проверка, является ли пользователь администратором.

    :param user_id: Идентификатор пользователя.
    :return: True, если пользователь является администратором, False в противном случае.
    """
    user = await db.users.find_one({'user_id': user_id})
    return user is not None and user.get('is_admin', False)

async def remove_duplicate_users():
    """
    Удаляет дубликаты записей пользователей из базы данных,
    оставляя только первую уникальную запись по полю user_id.
    """
    pipeline = [
        {"$sort": {"registration_date": 1}},  # Сортируем по дате регистрации (по возрастанию)
        {"$group": {
            "_id": "$user_id",
            "doc_id": {"$first": "$_id"},
            "count": {"$sum": 1}
        }},
        {"$match": {"count": {"$gt": 1}}}  # Выбираем только группы с более чем одной записью
    ]
    
    duplicate_groups = await db.users.aggregate(pipeline).to_list(None)
    
    for group in duplicate_groups:
        # Удаляем все документы с данным user_id, кроме первого (с наименьшей датой регистрации)
        await db.users.delete_many({
            "user_id": group["_id"],
            "_id": {"$ne": group["doc_id"]}
        })
    
    return len(duplicate_groups)