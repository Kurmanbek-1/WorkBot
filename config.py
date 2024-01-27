from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database


storage = MemoryStorage()

TOKEN = "6044276837:AAGhVb_j6ODq0zFMZjCLopMIcFM3NZ3SF4A"

Admins = [995712956, ]

Director = [6451475162, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)


# ip = config('ip')
# PostgresUser = config('PostgresUser')
# PostgresPassword = config('PostgresPassword')
# DATABASE = config('DATABASE')

user = config("POSTGRES_USER")
password = config("POSTGRES_PASSWORD")
hostname = config("POSTGRES_HOST")
database_name = config("POSTGRES_DB")
port = config("POSTGRES_PORT")

POSTGRES_URL = f"postgresql://{user}:{password}@{hostname}:{port}/{database_name}"
DESTINATION = config('DESTINATION')
data_b = Database(POSTGRES_URL)

