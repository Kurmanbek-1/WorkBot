# ======================================================================================================================
from config import Director, bot

from db.db_main import ORM_main

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os


# ======================================================================================================================

async def delete_products_coming_command_by_city(message: types.Message, city: str):
    if message.from_user.id in Director:
        products = await ORM_main.sql_command_all_products_coming()
        for product in products:
            if product[5] == city:
                photo_path = os.path.abspath(product[9])

                if os.path.exists(photo_path):
                    await bot.send_photo(message.from_user.id, photo=open(photo_path, 'rb'),
                                         caption=f"Товар: {product[1]}\n"
                                                 f"Информация о товаре: {product[2]}\n"
                                                 f"Дата прихода: {product[3]}\n"
                                                 f"Цена: {product[4]}\n"
                                                 f"Город: {product[5]}\n"
                                                 f"Артикул: {product[7]}\n"
                                                 f"количество: {product[8]}\n",
                                         reply_markup=InlineKeyboardMarkup().add(
                                             InlineKeyboardButton(f"delete {product[0]}",
                                                                  callback_data=f"delete_com_pr {product[0]}")))
                else:
                    print(f"Файл не найден: {photo_path}")

    else:
        await message.answer("You not Director!")


async def delete_products_coming_command_Bish(message: types.Message):
    await delete_products_coming_command_by_city(message, 'Бишкек')


async def delete_products_coming_command_Osh(message: types.Message):
    await delete_products_coming_command_by_city(message, 'ОШ')


async def delete_products_coming_command_Moscow_1(message: types.Message):
    await delete_products_coming_command_by_city(message, 'Москва')


# ======================================================================================================================

async def complete_delete_comming_products(call: types.CallbackQuery):
    await ORM_main.sql_command_delete_coming(call.data.replace("delete_com_pr ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


# ======================================================================================================================

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(delete_products_coming_command_Bish, commands=['Удал_Прих_Bishkek'])
    dp.register_message_handler(delete_products_coming_command_Osh, commands=['Удал_Прих_Osh'])
    dp.register_message_handler(delete_products_coming_command_Moscow_1, commands=['Удал_Прих_Moscow'])
    dp.register_callback_query_handler(complete_delete_comming_products,
                                       lambda call: call.data and call.data.startswith("delete_com_pr "))
# ======================================================================================================================
