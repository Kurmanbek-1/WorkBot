from aiogram import Dispatcher, types
from config import bot
from config import Admins, Director, POSTGRES_URL
import asyncpg


async def control_day(message: types.Message, city: str, connection):
    async with connection.transaction():
        products = await connection.fetch(f"SELECT * FROM products_care WHERE DATE(creation_time) = DATE('now') AND city = '{city}'")
        total_sum_day = []
        if message.from_user.id in Admins or Director:
            for product in products:
                total_sum_day.append(product[8])
                with open(f"{product[12]}", "rb") as photo:
                    await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[13]}\n"
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
                                                                                          f"количество: {product[11]}\n")
            await message.answer(f"Проданная сумма за сегодня - {sum(total_sum_day)}\n"
                                 f"кол-во проданных товаров за сегодня - {len(total_sum_day)}")
        else:
            await message.answer("Вы не админ!")


async def control_month(message: types.Message, city: str, connection):
    async with connection.transaction():
        products = await connection.fetch(
            f"SELECT * FROM products_care WHERE EXTRACT(YEAR FROM creation_time) = EXTRACT(YEAR FROM CURRENT_DATE) "
            f"AND EXTRACT(MONTH FROM creation_time) = EXTRACT(MONTH FROM CURRENT_DATE) AND city = '{city}'"
        )
        total_sum_mon = []
        if message.from_user.id in Admins or Director:
            for product in products:
                total_sum_mon.append(product[8])
                with open(f"{product[12]}", "rb") as photo:
                    await bot.send_photo(message.from_user.id, photo=photo, caption=f"Товар: {product[13]}\n"
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
                                                                                          f"количество: {product[11]}\n")


            await message.answer(f"Проданная сумма за месяц - {sum(total_sum_mon)}\n"
                                 f"кол-во проданных товаров за месяц - {len(total_sum_mon)}")
        else:
            await message.answer("Вы не админ!")


async def control_day_bish(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_day(message, 'Бишкек', connection)



async def control_bishkek_month(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_month(message, 'Бишкек', connection)


async def control_day_osh(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_day(message, 'ОШ', connection)


async def control_osh_month(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_month(message, 'ОШ', connection)


async def control_day_moscow_1(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_day(message, 'Москва_1', connection)


async def control_moscow_1_month(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_month(message, 'Москва_1', connection)


async def control_day_Osh_2(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_day(message, 'Ош 2-филиал', connection)


async def control_Osh_2_month(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_month(message, 'Ош 2-филиал', connection)



# ===================================================================================================
""" Отчет за неделю """
async def control_week(message: types.Message, city: str, connection):
    async with connection.transaction():
        products = await connection.fetch(
            f"SELECT * FROM products_care WHERE creation_time >= CURRENT_DATE - INTERVAL '7 days' AND city = '{city}'"
        )
        total_sum_week = []
        if message.from_user.id in Admins or Director:
            for product in products:
                total_sum_week.append(product[8])
                with open(f"{product[12]}", "rb") as photo:
                    await bot.send_photo(message.from_user.id, photo=photo, caption=f"Товар: {product[13]}\n"
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
                                                                                          f"количество: {product[11]}\n")

            await message.answer(f"Проданная сумма за неделю - {sum(total_sum_week)}\n"
                                 f"кол-во проданных товаров за неделю - {len(total_sum_week)}")
        else:
            await message.answer("Вы не админ!")


async def control_week_bish(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_week(message, 'Бишкек', connection)


async def control_week_osh(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_week(message, 'ОШ', connection)


async def control_week_moscow_1(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_week(message, 'Москва_1', connection)


async def control_week_Osh_2(message: types.Message):
    connection = await asyncpg.connect(POSTGRES_URL)
    await control_week(message, 'Ош 2-филиал', connection)



def register_control(dp: Dispatcher):
    dp.register_message_handler(control_bishkek_month, commands=["Отчет_за_месяц_Б"])
    dp.register_message_handler(control_day_bish, commands=["Отчет_за_день_Б"])

    dp.register_message_handler(control_osh_month, commands=['Отчет_за_месяц_Ош'])
    dp.register_message_handler(control_day_osh, commands=["Отчет_за_день_Ош"])

    dp.register_message_handler(control_moscow_1_month, commands=['Отчет_за_месяц_М_1'])
    dp.register_message_handler(control_day_moscow_1, commands=["Отчет_за_день_М_1"])

    dp.register_message_handler(control_Osh_2_month, commands=['Отчет_за_месяц_Ош_2'])
    dp.register_message_handler(control_day_Osh_2, commands=["Отчет_за_день_Ош_2"])

    dp.register_message_handler(control_week_bish, commands=['Отчет_за_неделю_Б'])
    dp.register_message_handler(control_week_osh, commands=['Отчет_за_неделю_Ош'])
    dp.register_message_handler(control_week_moscow_1, commands=['Отчет_за_неделю_М_1'])
    dp.register_message_handler(control_week_Osh_2, commands=['Отчет_за_неделю_Ош_2'])
