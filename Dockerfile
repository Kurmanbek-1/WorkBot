FROM python:3.10

# Создаем директории и копируем файлы
RUN mkdir -p /opt/services/bot/work-bot
WORKDIR /opt/services/bot/work-bot

COPY . /opt/services/bot/work-bot/

# Создаем отдельную директорию для зависимостей
RUN mkdir -p /opt/services/bot/work-bot/requirements
COPY requirements.txt /opt/services/bot/work-bot/requirements/

# Устанавливаем зависимости, включая asyncpg
RUN pip install --no-cache-dir -r requirements.txt

# Удаляем предыдущие переменные окружения для PostgreSQL, они теперь задаются в Docker Compose
ENV POSTGRES_DB "osor_tg_bot"
ENV POSTGRES_USER "postgres"
ENV POSTGRES_PASSWORD "123"
ENV POSTGRES_HOST "postgres_compass"
ENV POSTGRES_PORT "5432"

# Команда для запуска приложения
CMD ["python", "/opt/services/bot/work-bot/main.py"]
