# ====================================================================================================================
from aiogram import types, Dispatcher
from config import bot, Admins, Director, POSTGRES_URL
import asyncpg

# ====================================================================================================================

async def sql_command_booking(message: types.Message, city: str, connection):
    async with connection.transaction():
        bookings = await connection.fetch(f"SELECT * FROM booking WHERE city = '{city}'")

        for booking in bookings:
            if message.from_user.id in Admins or Director:
                with open(f"{booking[12]}", "rb") as photo:
                    await bot.send_photo(message.from_user.id, photo=photo, caption=f"Товар: {booking[1]}\n"
                                                                                          f"Дата началда брони: {booking[2]}\n"
                                                                                          f"Дата конца брони: {booking[3]}\n"
                                                                                          f"Имя заказчика: {booking[4]}\n"
                                                                                          f"Номер тел заказчика: {booking[5]}\n"
                                                                                          f"Продавец: {booking[6]}\n"
                                                                                          f"Номер телефона продавца: {booking[7]}\n"
                                                                                          f"Цена(без скидки): {booking[8]}\n"
                                                                                          f"Скидка: {booking[9]}\n"
                                                                                          f"Итоговая цена: {booking[10]}\n"
                                                                                          f"Город: {booking[11]}")
            else:
                await message.answer('Вы не админ!')


async def sql_command_booking_bishkek(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_booking(message, 'Бишкек', connection)


async def sql_command_booking_osh(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_booking(message, 'ОШ', connection)


async def sql_command_booking_moscow_1(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_booking(message, 'Москва_1', connection)


async def sql_command_booking_Osh_2(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_booking(message, 'Ош 2-филиал', connection)


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_booking_bishkek, commands=['Брони_Бишкек'])
    dp.register_message_handler(sql_command_booking_osh, commands=['Брони_Ош'])
    dp.register_message_handler(sql_command_booking_moscow_1, commands=['Брони_Москва_1'])
    dp.register_message_handler(sql_command_booking_Osh_2, commands=['Брони_Ош_2'])
