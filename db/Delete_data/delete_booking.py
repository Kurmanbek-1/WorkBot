# ======================================================================================================================
from config import Director, bot

from db.db_main import ORM_main

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ======================================================================================================================

async def delete_booking_by_city(message: types.Message, city: str):
    if message.from_user.id in Director:
        bookings = await ORM_main.sql_command_all_booking()
        for booking in bookings:
            if booking[10] == city:
                await bot.send_photo(message.from_user.id, photo=booking[11], caption=f"Товар: {booking[0]}\n"
                                                                                      f"Дата началда брони: {booking[1]}\n"
                                                                                      f"Дата конца брони: {booking[2]}\n"
                                                                                      f"Имя заказчика: {booking[3]}\n"
                                                                                      f"Номер тел заказчика: {booking[4]}\n"
                                                                                      f"Продавец: {booking[5]}\n"
                                                                                      f"Номер телефона продавца: {booking[6]}\n"
                                                                                      f"Цена(без скидки): {booking[7]}\n"
                                                                                      f"Скидка: {booking[8]}\n"
                                                                                      f"Итоговая цена: {booking[9]}\n"
                                                                                      f"Город: {booking[10]}",
                                     reply_markup=InlineKeyboardMarkup().add(
                                         InlineKeyboardButton(f"delete {booking[0]}", callback_data=f"delete {booking[0]}")))

    else:
        await message.answer("Вы не директор!")


async def delete_booking_bish(message: types.Message):
    await delete_booking_by_city(message, 'Бишкек')


async def delete_booking_osh(message: types.Message):
    await delete_booking_by_city(message, 'Ош')


async def delete_booking_Moscow_1(message: types.Message):
    await delete_booking_by_city(message, 'Москва_1')


async def delete_booking_Moscow_2(message: types.Message):
    await delete_booking_by_city(message, 'Москва_2')



# ======================================================================================================================

async def complete_delete(call: types.CallbackQuery):
    await ORM_main.sql_command_delete_booking(call.data.replace("Удалить ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


# ======================================================================================================================

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(delete_booking_bish, commagnds=['Удал_Броней_Bishkek'])
    dp.register_message_handler(delete_booking_osh, commands=['Удал_Броней_Osh'])
    dp.register_message_handler(delete_booking_Moscow_1, commands=['Удал_Броней_Moscow_1'])
    dp.register_message_handler(delete_booking_Moscow_2, commands=['Удал_Броней_Moscow_2'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith("Удалить "))
