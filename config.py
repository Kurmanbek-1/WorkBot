from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

TOKEN = "6570711981:AAGo0p436G80I_ziI24xTQblz3Z-LhPnM5w"

storage = MemoryStorage()
# TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


Director = [6451475162, 1738805992, 995712956, ]

Admins = [995712956, 1000541805, 958938518, 6127093234, ]

Developers = [995712956, ]


ip = config('ip')
PostgresUser = config('PostgresUser')
PostgresPassword = config('PostgresPassword')
DATABASE = config('DATABASE')

POSTGRES_URL = f"postgresql://{PostgresUser}:{PostgresPassword}@{ip}/{DATABASE}"
# POSTGRES_URL = "postgresql://postgres:123@postgres_compass:5432/osor_tg_bot"
DESTINATION = "/app/media"
data_b = Database(POSTGRES_URL)
