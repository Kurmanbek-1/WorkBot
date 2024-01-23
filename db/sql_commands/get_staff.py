# ====================================================================================================================
from aiogram import types, Dispatcher
from config import bot, Admins, Director, POSTGRES_URL
import asyncpg


# ====================================================================================================================

async def sql_command_staff(message: types.Message, city_query: str, connection):
    async with connection.transaction():
        employees = await connection.fetch(f"SELECT * FROM staff WHERE city_staff = '{city_query}'")

        if message.from_user.id in Admins or Director:
            for staff in employees:
                await bot.send_photo(message.from_user.id, photo=staff[6], caption=f"Имя: {staff[1]}\n"
                                                                                   f"Номер тел: {staff[2]}\n"
                                                                                   f"Информация о сотруднике: {staff[3]}\n"
                                                                                   f"График: {staff[4]}\n"
                                                                                   f"Филиал: {staff[5]}")
        else:
            await message.answer("Вы не админ!")


async def staff_moscow_1(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_staff(message, 'Москва_1', connection)


async def staff_Osh_2(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_staff(message, 'Ош_2', connection)


async def staff_bishkek(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_staff(message, 'Бишкек', connection)



async def staff_osh(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_command_staff(message, 'ОШ', connection)


def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(staff_moscow_1, commands=['Сотрудники_Москва_1'])
    dp.register_message_handler(staff_Osh_2, commands=['Сотрудники_Ош_2'])
    dp.register_message_handler(staff_bishkek, commands=['Сотрудники_Бишкек'])
    dp.register_message_handler(staff_osh, commands=['Сотрудники_Ош'])