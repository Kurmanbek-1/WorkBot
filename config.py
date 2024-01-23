from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database


storage = MemoryStorage()

TOKEN = "6044276837:AAGhVb_j6ODq0zFMZjCLopMIcFM3NZ3SF4A"

Admins = [995712956,]

Director = [995712956, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)


# ip = config('ip')
# PostgresUser = config('PostgresUser')
# PostgresPassword = config('PostgresPassword')
# DATABASE = config('DATABASE')

POSTGRES_URL = "postgresql://postgres:123@127.0.0.1:5432/osor_tg_bot"
DESTINATION = config('DESTINATION')
data_b = Database(POSTGRES_URL)

