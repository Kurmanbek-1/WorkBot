from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()

TOKEN = "6044276837:AAGhVb_j6ODq0zFMZjCLopMIcFM3NZ3SF4A"


Director = [6451475162, 1738805992, 995712956, ]

Admins = [995712956, 1000541805, 958938518, 6127093234, ]

Developers = [995712956, ]


bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

POSTGRES_URL = "postgresql://postgres:123@postgres_compass:5432/osor_tg_bot"


DESTINATION = "/app/media"
data_b = Database(POSTGRES_URL)



