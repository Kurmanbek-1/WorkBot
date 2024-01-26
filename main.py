from aiogram.utils import executor
import logging

from config import dp, bot, Admins
from handlers import commands
from handlers.FSM import (FSM_coming_products, FSM_care_products, FSM_booking, FSM_reg_staff, FSM_being_late)
from db.sql_commands import Products_Coming_Category

from db.db_main.ORM_main import create_tables
from db.Delete_data import delete_care_products, delete_coming_products, delete_booking, delete_staff
from db.sql_commands import (get_booking, get_staff,
                             get_salary_staff, get_products_care, get_regular_customer, get_being_late)
from db.checkout_control import get_info_ForControl

import buttons
from config import data_b


# ===========================================================================
async def on_startup(_):
    for i in Admins:
        await bot.send_message(chat_id=i, text="Бот запущен!", reply_markup=buttons.start_admins_markup)
    # await bot.send_message(chat_id=Director[0], text="Бот запущен!", reply_markup=buttons.start_director_markup)
    await data_b.connect()
    await create_tables()


# async def on_shutdown(_):
#     await data_b.close()


# ===========================================================================
commands.register_commands(dp)

FSM_coming_products.register_products(dp)
FSM_care_products.register_products(dp)
FSM_booking.register_booking(dp)
FSM_reg_staff.register_staff(dp)
FSM_being_late.register_control(dp)

Products_Coming_Category.register_fsm_comitCategory(dp)

# =====================================================
get_products_care.register_sql_commands(dp)
get_booking.register_sql_commands(dp)
get_staff.register_sql_commands(dp)
get_salary_staff.register_sql_commands(dp)
get_regular_customer.register_super_customers(dp)
get_being_late.register_sql_commands(dp)
# ===========================================================================
get_info_ForControl.register_control(dp)
# ===========================================================================
delete_care_products.register_handler_admin(dp)
delete_coming_products.register_handler_admin(dp)
delete_booking.register_handler_admin(dp)
delete_staff.register_handler_admin(dp)
# ===========================================================================
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
