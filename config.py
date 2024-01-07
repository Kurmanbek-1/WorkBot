from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()

TOKEN = "6044276837:AAGhVb_j6ODq0zFMZjCLopMIcFM3NZ3SF4A"

Admins = [908379438, 995712956, 1000541805]

Director = [1738805992, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

host = config('ip')
user = config('PostgresUser')
password = config('PostgresPassword')
DATABASE = config('DATABASE')
port = config('port')

# POSTGRES_URL = "postgresql://postgres:123@0.0.0.0:5432/osor_tg_bot"
POSTGRES_URL = f"postgresql://{user}:{password}@{host}:{port}/{DATABASE}"
DESTINATION = config('DESTINATION')
data_b = Database(POSTGRES_URL)
