FROM python:3.10

# Создаем директории и копируем файлы
RUN mkdir -p /opt/services/bot/work-bot
WORKDIR /opt/services/bot/work-bot

RUN mkdir -p /opt/services/bot/work-bot/requirements
ADD requirements.txt /opt/services/bot/work-bot/

COPY . /opt/services/bot/work-bot/

# Устанавливаем зависимости, включая asyncpg
RUN pip install -r requirements.txt

# Команда для запуска приложения
CMD ["python", "/opt/services/bot/work-bot/main.py"]
