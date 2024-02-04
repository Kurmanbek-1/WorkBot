from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()

TOKEN = config("TOKEN")

Admins = [659106628, ]

Director = [659106628, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

POSTGRES_URL = "postgresql://postgres:123@postgres_compass:5432/osor_tg_bot"


DESTINATION = "/app/media"
data_b = Database(POSTGRES_URL)
