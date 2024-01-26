# ====================================================================================================================
from aiogram import types, Dispatcher
from config import Admins, bot, Director, POSTGRES_URL
import asyncpg


# ====================================================================================================================
async def sql_command_products(message: types.Message, city_name: str, connection):
    async with connection.transaction():
        products = await connection.fetch(f"SELECT * FROM products_care WHERE city = '{city_name}'")

        if message.from_user.id in Admins or Director:
            for product in products:
                with open(f"{product[12]}", "rb") as photo:
                    await bot.send_photo(chat_id=message.from_user.id,
                                         photo=photo,
                                         caption=f"Товар: {product[13]}\n"
                                                 f"Информация о товаре: {product[14]}\n"
                                                 f"Дата ухода: {product[1]}\n"
                                                 f"Имя заказчика: {product[2]}\n"
                                                 f"Номер тел заказчика: {product[3]}\n"
                                                 f"Продавец: {product[4]}\n"
                                                 f"Номер телефона продавца: {product[5]}\n"
                                                 f"Цена(без скидки): {product[6]}\n"
                                                 f"Скидка: {product[7]}\n"
                                                 f"Итоговая цена: {product[8]}\n"
                                                 f"Город: {product[9]}\n"
                                                 f"Артикул: {product[10]}\n"
                                                 f"Количество: {product[11]}\n"
                                         )
        else:
            await message.answer("Вы не админ!")


async def sql_command_products_bish(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_products(message, 'Бишкек', connection)


async def sql_command_products_osh(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_products(message, 'ОШ', connection)


async def sql_command_products_moscow_1(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_products(message, 'Москва_1', connection)


async def sql_command_products_Osh_2(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_products(message, 'Ош 2-филиал', connection)


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_products_bish, commands=['Товары_Биш(Проданные)', ])
    dp.register_message_handler(sql_command_products_osh, commands=['Товары_Ош(Проданные)'])
    dp.register_message_handler(sql_command_products_moscow_1, commands=['Товары_М1(Проданные)'])
    dp.register_message_handler(sql_command_products_Osh_2, commands=['Товары_Ош2(Проданные)'])
