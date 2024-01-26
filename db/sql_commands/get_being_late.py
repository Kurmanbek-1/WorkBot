# ====================================================================================================================
from aiogram import types, Dispatcher
from config import Admins, Director, POSTGRES_URL
import asyncpg



# ====================================================================================================================

async def sql_being_late(message: types.Message, city: str, connection):
    async with connection.transaction():
        lateness = await connection.fetch(f"SELECT * FROM being_late WHERE city = '{city}'")

        for time in lateness:
            if message.from_user.id in Admins or Director:
                await message.answer(f'Данные: \n'
                                     f'ФИО: {time[1]}\n'
                                     f'Дата: {time[2]}\n'
                                     f'Время прибытия: {time[3]}\n'
                                     f'Город: {time[4]}')
            else:
                await message.answer('Вы не админ!')


async def sql_being_late_bishkek(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_being_late(message, 'Бишкек', connection)


async def sql_being_late_osh(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_being_late(message, 'ОШ', connection)


async def sql_being_late_moscow_1(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_being_late(message, 'Москва_1', connection)


async def sql_being_late_Osh_2(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await sql_being_late(message, 'Ош 2-филиал', connection)


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_being_late_bishkek, commands=['Контроль_Бишкек'])
    dp.register_message_handler(sql_being_late_osh, commands=['Контроль_Ош'])
    dp.register_message_handler(sql_being_late_moscow_1, commands=['Контроль_Москва_1'])
    dp.register_message_handler(sql_being_late_Osh_2, commands=['Контроль_Ош_2'])
