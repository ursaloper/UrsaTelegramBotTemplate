
# UrsaTelegramBotTemplate

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-4.0%2B-green)
![Лицензия](https://img.shields.io/badge/Лицензия-MIT-yellow)

Универсальный и гибкий шаблон для создания Telegram-ботов на Python.

## 🌟 Особенности

- **Асинхронная архитектура**: Построен на `asyncio` для высокой производительности и масштабируемости.
- **Гибкость базы данных**: Изначально настроен для MongoDB, но адаптируем к другим базам данных.
- **Модульная структура**: Легко расширяемая и поддерживаемая кодовая база.
- **Поддержка Docker**: Контейнеризация для стабильной среды разработки и развертывания.
- **Интернационализация**: Встроенная поддержка нескольких языков.
- **Интеграция веб-приложений**: Легкая интеграция с веб-приложениями.
- **Продвинутое логирование**: Комплексная система логирования для удобной отладки и мониторинга.

## 📋 Содержание

- [Требования](#-требования)
- [Установка](#-установка)
- [Структура проекта](#-структура-проекта)
- [Конфигурация](#-конфигурация)
- [Использование](#-использование)
- [Запуск с Docker](#-запуск-с-docker)
- [Тестирование](#-тестирование)
- [Содействие проекту](#-содействие-проекту)
- [Лицензия](#-лицензия)

## 🔧 Требования

- Python
- MongoDB (база данных по умолчанию, возможна интеграция других)
- Docker (опционально)

## 🚀 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ursaloper/UrsaTelegramBotTemplate.git
   cd UrsaTelegramBotTemplate
   ```

2. Создайте и настройте файл `.env`:
   ```bash
   cp .env.example .env
   # Отредактируйте .env, указав вашу конфигурацию
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## 📂 Структура проекта

```
UrsaTelegramBotTemplate/
├── main.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
├── .env.example
├── app/
│   ├── __init__.py
│   ├── bot/
│   ├── database/
│   ├── utils/
│   ├── services/
│   └── webapp/
├── static/
├── locales/
├── logs/
├── tests/
└── scripts/
```

## ⚙️ Конфигурация

Настройте вашего бота в `config.py` и установите переменные окружения в файле `.env`. Ключевые настройки включают:

- `BOT_TOKEN`: Ваш токен Telegram Bot API
- `MONGODB_URI`: URI подключения к MongoDB
- `MONGODB_NAME`: Имя вашей базы данных MongoDB
- `WEB_APP_URL`: URL вашего веб-приложения (если применимо)
- `ADMIN_ID`: Telegram ID администратора бота

## 🖥️ Использование

1. Запустите бота:
   ```bash
   python main.py
   ```

2. Взаимодействуйте с вашим ботом в Telegram, используя реализованные команды и функции.

## 🐳 Запуск с Docker

1. Соберите Docker образ:
   ```bash
   docker build -t ursa-telegram-bot .
   ```

2. Запустите контейнер:
   ```bash
   docker run --env-file .env ursa-telegram-bot
   ```

Альтернативно, используйте Docker Compose:
```bash
docker-compose up --build
```

## 🧪 Тестирование

Запустите набор тестов:
```bash
python -m pytest tests/
```

## 🤝 Содействие проекту

Мы приветствуем вклад в проект! Пожалуйста, не стесняйтесь создавать Pull Request.

## 📄 Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. в файле [LICENSE](LICENSE).

---

## 🌐 Интеграция других баз данных

Хотя этот шаблон изначально настроен для MongoDB, он разработан для гибкости. Вы можете легко интегрировать другие базы данных:

1. Установите соответствующий Python-драйвер для выбранной базы данных.
2. Создайте новый файл в `app/database/` (например, `postgresql.py`) для обработки подключений и операций с базой данных.
3. Обновите `config.py` необходимыми настройками для новой базы данных.
4. Измените функции работы с базой данных в `app/utils/` для работы с новой базой данных.

Пример для PostgreSQL:

1. Установите `asyncpg`:
   ```bash
   pip install asyncpg
   ```

2. Создайте `app/database/postgresql.py`:
   ```python
   import asyncpg
   from config import POSTGRESQL_URI

   async def init_postgresql():
       conn = await asyncpg.connect(POSTGRESQL_URI)
       return conn

   # Добавьте другие функции для работы с PostgreSQL здесь
   ```

3. Обновите ваши модели и сервисы для использования новых функций базы данных.

## 🔄 Асинхронная архитектура

Этот шаблон использует `asyncio` Python для асинхронного программирования:

- **Эффективные операции ввода-вывода**: Обрабатывает множество обновлений Telegram одновременно.
- **Неблокирующие запросы к базе данных**: Использует асинхронные драйверы баз данных для улучшения производительности.
- **Масштабируемость**: Легко справляется с большим количеством одновременных пользователей.
- **Интеграция с асинхронными веб-фреймворками**: Легко работает с фреймворками типа FastAPI или aiohttp для веб-приложений.

Для использования асинхронных функций:

- Используйте синтаксис `async`/`await` в ваших функциях-обработчиках.
- Применяйте асинхронные библиотеки для внешних API-вызовов и операций с базой данных.
- Реализуйте одновременные задачи для фоновой обработки.

Эта архитектура обеспечивает отзывчивость и эффективность вашего бота даже при высокой нагрузке.




## English Version:
# UrsaTelegramBotTemplate

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-4.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A comprehensive and flexible template for building Telegram bots using Python.

## 🌟 Features

- **Asynchronous Architecture**: Built with `asyncio` for high performance and scalability.
- **Database Flexibility**: Primarily configured for MongoDB, but adaptable to other databases.
- **Modular Structure**: Easy to extend and maintain with a well-organized codebase.
- **Docker Support**: Containerization for consistent development and deployment environments.
- **Internationalization**: Built-in support for multiple languages.
- **Web Application Integration**: Seamless integration with web applications.
- **Advanced Logging**: Comprehensive logging system for easier debugging and monitoring.

## 📋 Table of Contents

- [Requirements](#-requirements)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Running with Docker](#-running-with-docker)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)

## 🔧 Requirements

- Python
- MongoDB (default database, others can be integrated)
- Docker (optional)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ursaloper/UrsaTelegramBotTemplate.git
   cd UrsaTelegramBotTemplate
   ```

2. Create and configure the `.env` file:
   ```bash
   cp .env.example .env
   # Edit .env with your specific configuration
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📂 Project Structure

```
UrsaTelegramBotTemplate/
├── main.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
├── .env.example
├── app/
│   ├── __init__.py
│   ├── bot/
│   ├── database/
│   ├── utils/
│   ├── services/
│   └── webapp/
├── static/
├── locales/
├── logs/
├── tests/
└── scripts/
```

## ⚙️ Configuration

Configure your bot in `config.py` and set environment variables in the `.env` file. Key configurations include:

- `BOT_TOKEN`: Your Telegram Bot API token
- `MONGODB_URI`: MongoDB connection URI
- `MONGODB_NAME`: Name of your MongoDB database
- `WEB_APP_URL`: URL of your web application (if applicable)
- `ADMIN_ID`: Telegram user ID of the bot administrator

## 🖥️ Usage

1. Start the bot:
   ```bash
   python main.py
   ```

2. Interact with your bot on Telegram using the implemented commands and features.

## 🐳 Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t ursa-telegram-bot .
   ```

2. Run the container:
   ```bash
   docker run --env-file .env ursa-telegram-bot
   ```

Alternatively, use Docker Compose:
```bash
docker-compose up --build
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌐 Integrating Other Databases

While this template is configured for MongoDB by default, it's designed to be flexible. You can easily integrate other databases:

1. Install the appropriate Python driver for your chosen database.
2. Create a new file in `app/database/` (e.g., `postgresql.py`) to handle database connections and operations.
3. Update `config.py` with the necessary configuration for your new database.
4. Modify the database utility functions in `app/utils/` to work with your new database.

Example for PostgreSQL:

1. Install `asyncpg`:
   ```bash
   pip install asyncpg
   ```

2. Create `app/database/postgresql.py`:
   ```python
   import asyncpg
   from config import POSTGRESQL_URI

   async def init_postgresql():
       conn = await asyncpg.connect(POSTGRESQL_URI)
       return conn

   # Add other PostgreSQL-specific functions here
   ```

3. Update your models and services to use the new database functions.

## 🔄 Asynchronous Architecture

This template leverages Python's `asyncio` for asynchronous programming:

- **Efficient I/O Operations**: Handles multiple Telegram updates concurrently.
- **Non-Blocking Database Queries**: Uses asynchronous database drivers for improved performance.
- **Scalability**: Easily handles a large number of simultaneous users.
- **Integration with Asynchronous Web Frameworks**: Seamlessly works with frameworks like FastAPI or aiohttp for web applications.

To utilize the asynchronous features:

- Use `async`/`await` syntax in your handler functions.
- Employ asynchronous libraries for external API calls and database operations.
- Implement concurrent tasks for background processing.

This architecture ensures your bot remains responsive and efficient, even under high load.
