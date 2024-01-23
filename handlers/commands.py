# =================================================================================================================
from aiogram import types, Dispatcher
from config import bot, Admins, Director
import buttons

# =================================================================================================================

async def start(message: types.Message):
    if message.from_user.id in Admins or Director:
        await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                     "Этот бот для управления бизнесом!",
                               reply_markup=buttons.start_admins_markup)
    else:
        await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                     "Этот бот для управления бизнесом!",
                               reply_markup=buttons.staff_markup)


async def support(message: types.Message):
    await message.answer('Тех поддержка:\n\n'
                         'Бишкек: +996221825236n\n'
                         'Ош: +996559618881\n'
                         '')


async def info(message: types.Message):
    text = """
Для чего нужен этот бот ?
=================================
Этот бот был создан специально для компании OSOR 👕, для управления бизнесом
=================================
В этом боте сотрудники могут вводить данные о приходе и уходе товара, также записывать брони
А управляющие могут как записывать данные, так и выводить их, и этим самым контролировать как сотрудников, так и кассу
=================================
Также для удобной навигации по боту, все кнопки на русском и по названиям понятно что за что отвечает!
=================================
"""
    if message.from_user.id in Director:
        await message.answer(text + "\n‼️ Вы Директор ‼️",
                             reply_markup=buttons.start_director_markup)
    elif message.from_user.id in Admins:
        await message.answer(text + "\n‼️ Вы админ ‼️",
                             reply_markup=buttons.start_admins_markup)
    else:
        await message.answer(text + "\n‼️ Вы сотрудник ‼️",
                             reply_markup=buttons.staff_markup)


async def products_button(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer('Вы зашли в товары!', reply_markup=buttons.products_admins_markup)
    else:
        await message.answer('Вы зашли в товары!', reply_markup=buttons.products_staff_markup)


"""Только для Админов"""


async def finance_button(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer('Вы зашли в финансы!', reply_markup=buttons.ButtonForFinance_markup)
    else:
        await message.answer('Вы не админ!')


async def pull_data_staff(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer("Выберите снизу из кнопок действие ⬇", reply_markup=buttons.staff_pull_data_markup)
    else:
        await message.answer("Вы не админ")


async def pull_data(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer("Вы зашли к выводу данных товаров \n"
                             "(Внутри них есть приход, уход и брони)\n\n"
                             "Выберите действие, из кнопок снизу!\n", reply_markup=buttons.Buttons_for_categories)
    else:
        await message.answer("Вы не админ!")


async def products_coming(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Вы выбрали приход товаров!"
                             f"\n"
                             f"Внизу есть кнопки, где можно выбрать категорию!", reply_markup=buttons.CategoryButtons)
    else:
        await message.answer("Вы не админ!")


async def products_care(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Вы выбрали уход товаров!", reply_markup=buttons.CareButtons)
    else:
        await message.answer("Вы не админ!")


async def products_booking(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Вы выбрали в брони товаров!", reply_markup=buttons.Booking_Buttons)
    else:
        await message.answer("Вы не админ!")

# ====================================================================================================================

async def get_bishkek(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Вы выбрали Бишкек!", reply_markup=buttons.get_bishkek_markup)
    else:
        await message.answer("Вы не админ!")


async def get_osh(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Вы выбрали Ош!", reply_markup=buttons.get_branches_osh_markup)
    else:
        await message.answer("Вы не админ!")


async def get_moscow_1(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Вы выбрали Москву! (Первый филиал)", reply_markup=buttons.get_branches_moscow_1_markup)
    else:
        await message.answer("Вы не админ!")


async def get_Osh_2(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Вы выбрали Ош! (Второй филиал)", reply_markup=buttons.get_branches_moscow_2_markup)
    else:
        await message.answer("Вы не админ!")

# ====================================================================================================================


async def ButtonForFinance(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Выберите снизу из кнопок, что вы хотите получить! ⬇",
                             reply_markup=buttons.ButtonForFinance_markup)
    else:
        await message.answer("Вы не админ!")


async def SalaryButton(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Выберите с какого филиала! ⬇", reply_markup=buttons.SalaryStaff_markup)
    else:
        await message.answer("Вы не админ!")


async def RegularСustomerButton(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer("Вы зашли с постоянным клиентам!\n"
                             "Выберите из какого города(филиала) хотите вывести!"
                             "Из какого филиала ?! ⬇", reply_markup=buttons.RegularСustomer_markup)
    else:
        await message.answer("Вы не админ!")


async def controlchecout(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer(f"Вы зашли в контроль кассы!\n"
                             f"Снизу расписаны отчеты за дни и месяца!", reply_markup=buttons.control_markup)
    else:
        await message.answer("Вы не админ!")


# --------------------------------------------------

async def staff_button(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer('Вы зашли к сотрудникам!', reply_markup=buttons.staff_admins_markup)
    else:
        await message.answer("Вы не админ!")


async def get_staff_buttons(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer("Выберите снизу из кнопок ⬇", reply_markup=buttons.data_recording_staff_markup)
    else:
        await message.answer("Вы не админ!")


# --------------------------------------------------

async def back_for_admins(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=buttons.start_admins_markup)


"""----------"""

"""Только для Директора"""


async def DeleteButton(message: types.Message):
    if message.from_user.id in Director:
        await message.answer(f"Снизу можете выбрать где удалить данные! ⬇", reply_markup=buttons.Delete_markup)
    else:
        await message.answer("Эта команда вам недоступна!")


async def Bish_delete_button(message: types.Message):
    await message.answer("Выберите снизу из кнопок ⬇", reply_markup=buttons.Bish_delete_markup)


async def Osh_delete_button(message: types.Message):
    await message.answer("Выберите снизу из кнопок ⬇", reply_markup=buttons.Osh_delete_markup)


async def Moscow_1_delete_button(message: types.Message):
    await message.answer("Выберите снизу из кнопок ⬇", reply_markup=buttons.moscow_1_delete_markup)


async def Osh_2_delete_button(message: types.Message):
    await message.answer("Выберите снизу из кнопок ⬇", reply_markup=buttons.Osh_2_delete_markup)


"""----------"""


async def back_for_staff(message: types.Message):
    if message.from_user.id in Admins or Director:
        await message.answer('Вы возвратились назад!', reply_markup=buttons.start_admins_markup)
    else:
        await message.answer('Вы возвратились назад!', reply_markup=buttons.staff_markup)


async def data_recording(message: types.Message):
    await message.answer('Выберите действие, из кнопок снизу!', reply_markup=buttons.data_recording_markup)


async def back_for_director(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=buttons.start_admins_markup)


# =================================================================================================================

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(support, commands=['support'])

    dp.register_message_handler(info, commands=['Информация', 'info'])

    dp.register_message_handler(data_recording, commands=['запись_данных_товара'])
    dp.register_message_handler(pull_data, commands=['вывести_данные_товара'])

    dp.register_message_handler(get_staff_buttons, commands=['запись_данных_сотрудников'])
    dp.register_message_handler(pull_data_staff, commands=['вывести_данные_сотрудников'])

    dp.register_message_handler(products_button, commands=['Товары'])
    dp.register_message_handler(staff_button, commands=['Сотрудники'])
    dp.register_message_handler(finance_button, commands=['Финансы'])

    dp.register_message_handler(SalaryButton, commands=['Зарплаты'])
    dp.register_message_handler(RegularСustomerButton, commands=['Постоянные_клиенты'])
    dp.register_message_handler(controlchecout, commands=['Контроль_кассы'])

# ====================================================================================================================
    dp.register_message_handler(get_bishkek, commands=['Бишкек'])
    dp.register_message_handler(get_osh, commands=['Ош'])
    dp.register_message_handler(get_moscow_1, commands=['Москва_1'])
    dp.register_message_handler(get_Osh_2, commands=['Ош_2'])
# ====================================================================================================================

    dp.register_message_handler(DeleteButton, commands=['Удаление_из_базы'])
    dp.register_message_handler(back_for_director, commands=['<--назад'])
    dp.register_message_handler(Bish_delete_button, commands=["Бишкек_удаление"])
    dp.register_message_handler(Osh_delete_button, commands=["Ош_удаление"])
    dp.register_message_handler(Moscow_1_delete_button, commands=["Москва_1_удаление"])
    dp.register_message_handler(Osh_2_delete_button, commands=["Ош_2_удаление"])

    dp.register_message_handler(back_for_staff, commands=['<-назад'])
    dp.register_message_handler(back_for_admins, commands=['<назад'])

    dp.register_message_handler(products_care, commands=['Проданные_товары'])
    dp.register_message_handler(products_booking, commands=['Товары_на_брони'])