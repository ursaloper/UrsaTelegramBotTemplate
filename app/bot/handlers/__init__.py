"""
Модуль для регистрации всех обработчиков бота.
"""

from .start import register_handlers as register_start_handlers
from .admin import register_handlers as register_admin_handlers

def register_all_handlers(bot):
    """
    Регистрация всех обработчиков для бота.

    :param bot: Экземпляр асинхронного телеграм-бота.
    """
    register_start_handlers(bot)
    register_admin_handlers(bot)
