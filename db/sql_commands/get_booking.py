# ====================================================================================================================
from aiogram import types, Dispatcher
from config import bot

from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2


# ====================================================================================================================

async def sql_command_booking_bishkek(message: types.Message):
    bookings = cursor_bish.execute("SELECT * FROM booking")

    for booking in bookings:
        await bot.send_photo(message.from_user.id, photo=booking[10], caption=f"Товар: {booking[0]}\n"
                                                                              f"Дата прихода: {booking[1]}\n"
                                                                              f"Дата ухода: {booking[2]}\n"
                                                                              f"Имя заказчика: {booking[3]}\n"
                                                                              f"Номер тел заказчика: {booking[4]}\n"
                                                                              f"Продавец: {booking[5]}\n"
                                                                              f"Цена(без скидки): {booking[6]}\n"
                                                                              f"Скидка: {booking[7]}\n"
                                                                              f"Итоговая цена: {booking[8]}\n"
                                                                              f"Город: {booking[9]}")


async def sql_command_booking_osh(message: types.Message):
    bookings = cursor_osh.execute("SELECT * FROM booking")

    for booking in bookings:
        await bot.send_photo(message.from_user.id, photo=booking[10], caption=f"Товар: {booking[0]}\n"
                                                                              f"Дата прихода: {booking[1]}\n"
                                                                              f"Дата ухода: {booking[2]}\n"
                                                                              f"Имя заказчика: {booking[3]}\n"
                                                                              f"Номер тел заказчика: {booking[4]}\n"
                                                                              f"Продавец: {booking[5]}\n"
                                                                              f"Цена(без скидки): {booking[6]}\n"
                                                                              f"Скидка: {booking[7]}\n"
                                                                              f"Итоговая цена: {booking[8]}\n"
                                                                              f"Город: {booking[9]}")


async def sql_command_booking_moscow_1(message: types.Message):
    bookings = cursor_moscow_1.execute("SELECT * FROM booking")

    for booking in bookings:
        await bot.send_photo(message.from_user.id, photo=booking[10], caption=f"Товар: {booking[0]}\n"
                                                                              f"Дата прихода: {booking[1]}\n"
                                                                              f"Дата ухода: {booking[2]}\n"
                                                                              f"Имя заказчика: {booking[3]}\n"
                                                                              f"Номер тел заказчика: {booking[4]}\n"
                                                                              f"Продавец: {booking[5]}\n"
                                                                              f"Цена(без скидки): {booking[6]}\n"
                                                                              f"Скидка: {booking[7]}\n"
                                                                              f"Итоговая цена: {booking[8]}\n"
                                                                              f"Город: {booking[9]}")


async def sql_command_booking_moscow_2(message: types.Message):
    bookings = cursor_moscow_2.execute("SELECT * FROM booking")

    for booking in bookings:
        await bot.send_photo(message.from_user.id, photo=booking[10], caption=f"Товар: {booking[0]}\n"
                                                                              f"Дата прихода: {booking[1]}\n"
                                                                              f"Дата ухода: {booking[2]}\n"
                                                                              f"Имя заказчика: {booking[3]}\n"
                                                                              f"Номер тел заказчика: {booking[4]}\n"
                                                                              f"Продавец: {booking[5]}\n"
                                                                              f"Цена(без скидки): {booking[6]}\n"
                                                                              f"Скидка: {booking[7]}\n"
                                                                              f"Итоговая цена: {booking[8]}\n"
                                                                              f"Город: {booking[9]}")


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_booking_bishkek, commands=['Брони_Бишкек'])
    dp.register_message_handler(sql_command_booking_osh, commands=['Брони_Ош'])
    dp.register_message_handler(sql_command_booking_moscow_1, commands=['Брони_Москва_1'])
    dp.register_message_handler(sql_command_booking_moscow_2, commands=['Брони_Москва_2'])