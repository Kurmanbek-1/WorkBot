# ====================================================================================================================
from aiogram import types, Dispatcher
from config import Admins, Director, POSTGRES_URL
import asyncpg


# ====================================================================================================================
async def salary_salesman(message: types.Message, connection, city_name: str):
    async with connection.transaction():
        customers = await connection.fetch(f"SELECT DISTINCT phone_salesman, name_salesman FROM products_care WHERE city = '{city_name}'")
        percentage = 4

        employees = await connection.fetch("SELECT * FROM staff")

        if message.from_user.id in Admins or Director:
            if len(customers) == 0:
                await message.answer("Здесь пока ничего нет!")
            else:
                for customer in customers:
                    phone_salesman = customer[0]
                    total_prices = await connection.fetchval("SELECT SUM(total_price) FROM products_care WHERE phone_salesman = $1",
                                                             phone_salesman)

                    salary = total_prices * (percentage / 100.0)

                    await message.answer(f"Имя сотрудника: {customer[1]}\n"
                                         f"Номер телефона сотрудника: {customer[0]}\n"
                                         f"Количество проданных товаров: {len(customers)}\n"
                                         f"Сумма на которую он продал: {total_prices}\n"
                                         f"Его ЗП: {salary}")

        else:
            await message.answer("Вы не админ!")


async def salary_salesman_bishkek(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await salary_salesman(message, connection, 'Бишкек')


async def salary_salesman_osh(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await salary_salesman(message, connection, 'ОШ')


async def salary_salesman_moscow_1(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await salary_salesman(message, connection, 'Москва_1')


async def salary_salesman_Osh_2(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await salary_salesman(message, connection, 'Ош_2')


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(salary_salesman_bishkek, commands=['ЗП_Бишкек'])
    dp.register_message_handler(salary_salesman_osh, commands=['ЗП_Ош'])
    dp.register_message_handler(salary_salesman_moscow_1, commands=['ЗП_Москва_1'])
    dp.register_message_handler(salary_salesman_Osh_2, commands=['ЗП_Ош_2'])
