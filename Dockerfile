FROM python:3.10

RUN mkdir -p /app/osor_work_bot
WORKDIR /app/osor_work_bot

COPY . .

RUN chmod -R 644 entrypoints/* && \
        chmod +x entrypoints/* && \
                    pip install -r requirements.txt