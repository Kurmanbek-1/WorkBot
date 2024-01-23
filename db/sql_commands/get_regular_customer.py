from config import POSTGRES_URL, Director, Admins
from aiogram import types, Dispatcher
import asyncpg

# ====================================================================================================================

# global connection
# connection = asyncpg.connect(POSTGRES_URL)

async def handle_super_customer(message: types.Message, city_query: str, connection):
    async with connection.transaction():
        customers = await connection.fetch(f"SELECT phone_customer, name_customer FROM products_care WHERE city = '{city_query}'")
        results = {}

        if message.from_user.id in Admins or Director:
            for customer in customers:
                phone = customer[0]
                if phone not in results:
                    total_price = await connection.fetchval("SELECT SUM(total_price) FROM products_care WHERE phone_customer = $1 AND city = $2",
                                                           phone, city_query)
                    if total_price > 10000:
                        results[phone] = total_price
                        vip_photo = open("media/vip_card.png", "rb")
                        await message.answer_photo(photo=vip_photo, caption=f"Имя - {customer[1]}\n"
                                                                            f"Номер телефона - {phone}\n"
                                                                            f"Общая сумма покупок - {total_price}")
        else:
            await message.answer("Вы не админ!")


async def super_customer_moscow_1(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await handle_super_customer(message, 'Москва_1', connection)


async def super_customer_Osh_2(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await handle_super_customer(message, 'Ош_2', connection)


async def super_customer_bishkek(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await handle_super_customer(message, 'Бишкек', connection)


async def super_customer_osh(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await handle_super_customer(message, 'ОШ', connection)


def register_super_customers(dp: Dispatcher):
    dp.register_message_handler(super_customer_moscow_1, commands=['Клиенты_Москва_1'])
    dp.register_message_handler(super_customer_Osh_2, commands=['Клиенты_Ош_2'])
    dp.register_message_handler(super_customer_bishkek, commands=['Клиенты_Бишкек'])
    dp.register_message_handler(super_customer_osh, commands=['Клиенты_Ош'])
