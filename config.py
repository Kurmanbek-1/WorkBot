from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database


# =============================================================
# Токен для тестов
TOKEN = "6570711981:AAGo0p436G80I_ziI24xTQblz3Z-LhPnM5w"
# =============================================================


storage = MemoryStorage()
# TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


Director = [6451475162, 1738805992, ]
Admins = [995712956, ]
Developers = [995712956, ]


ip = config('ip')
PostgresUser = config('PostgresUser')
PostgresPassword = config('PostgresPassword')
DATABASE = config('DATABASE')

POSTGRES_URL = f"postgresql://{PostgresUser}:{PostgresPassword}@{ip}/{DATABASE}"
DESTINATION = "/app/media"

data_b = Database(POSTGRES_URL)
