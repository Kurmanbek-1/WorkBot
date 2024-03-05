# ======================================================================================================================
from config import Director, bot

from db.db_main import ORM_main

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ======================================================================================================================

async def delete_staff_by_city(message: types.Message, city: str):
    if message.from_user.id in Director:
        employees = await ORM_main.sql_command_all_staff()
        for staff in employees:
            if staff[5] == city:
                with open(f"{staff[6]}", "rb") as photo:
                    await bot.send_photo(message.from_user.id, photo=photo, caption=f"Имя: {staff[1]}\n"
                                                                                       f"Номер тел: {staff[2]}\n"
                                                                                       f"Информация о сотруднике: {staff[3]}\n"
                                                                                       f"График: {staff[4]}\n"
                                                                                       f"Филиал: {staff[5]}",
                                         reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {staff[0]}",
                                                                                                      callback_data=f"delete_staff {staff[0]}")))

    else:
        await message.answer("Вы не директор!")


async def delete_staff_bish(message: types.Message):
    await delete_staff_by_city(message, 'Бишкек')


async def delete_staff_osh(message: types.Message):
    await delete_staff_by_city(message, 'Ош')


async def delete_staff_Mescow_1(message: types.Message):
    await delete_staff_by_city(message, 'Москва')


# ======================================================================================================================

async def complete_delete_staff(call: types.CallbackQuery):
    await ORM_main.sql_command_delete_staff(call.data.replace("delete_staff ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


# ======================================================================================================================

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(delete_staff_bish, commands=['Удал_Сотруд_Bishkek'])
    dp.register_message_handler(delete_staff_osh, commands=['Удал_Сотруд_Osh'])
    dp.register_message_handler(delete_staff_Mescow_1, commands=['Удал_Сотруд_Moscow'])
    dp.register_callback_query_handler(complete_delete_staff,
                                       lambda call: call.data and call.data.startswith("delete_staff "))
