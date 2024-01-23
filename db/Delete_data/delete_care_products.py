# ======================================================================================================================
from config import Director, bot

from db.db_main import ORM_main

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ======================================================================================================================

async def delete_products_care_command_by_city(message: types.Message, city: str):
    if message.from_user.id in Director:
        products = await ORM_main.sql_command_all_products_care()
        for product in products:
            if product[9] == city:
                await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[13]}\n"
                                                                                      f"Информация о товаре: {product[14]}\n"
                                                                                      f"Дата прихода: {product[1]}\n"
                                                                                      f"Имя заказчика: {product[2]}\n"
                                                                                      f"Номер тел заказчика: {product[3]}\n"
                                                                                      f"Продавец: {product[4]}\n"
                                                                                      f"Номер телефона продавца: {product[5]}\n"
                                                                                      f"Цена(без скидки): {product[6]}\n"
                                                                                      f"Скидка: {product[7]}\n"
                                                                                      f"Итоговая цена: {product[8]}\n"
                                                                                      f"Город: {product[9]}\n"
                                                                                      f"Артикул: {product[10]}\n"
                                                                                      f"количество: {product[11]}\n",
                                     reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
                                                                                                  callback_data=f"delete_care_pr {product[0]}")))

    else:
        await message.answer("You not Director!")


async def delete_products_care_command_bish(message: types.Message):
    await delete_products_care_command_by_city(message, 'Бишкек')


async def delete_products_care_command_osh(message: types.Message):
    await delete_products_care_command_by_city(message, 'ОШ')


async def delete_products_care_command_moscow_1(message: types.Message):
    await delete_products_care_command_by_city(message, 'Москва_1')


async def delete_products_care_command_Osh_2(message: types.Message):
    await delete_products_care_command_by_city(message, 'Ош_2')


# ======================================================================================================================

async def complete_delete_care_products(call: types.CallbackQuery):
    await ORM_main.sql_command_delete_care(call.data.replace("delete_care_pr ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


# ======================================================================================================================

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(delete_products_care_command_bish, commands=['Удал_Прода_Bishkek'])
    dp.register_message_handler(delete_products_care_command_osh, commands=['Удал_Прода_Osh'])
    dp.register_message_handler(delete_products_care_command_moscow_1, commands=['Удал_Прода_Moscow_1'])
    dp.register_message_handler(delete_products_care_command_Osh_2, commands=['Удал_Прода_Osh_2'])
    dp.register_callback_query_handler(complete_delete_care_products,
                                       lambda call: call.data and call.data.startswith("delete_care_pr "))

