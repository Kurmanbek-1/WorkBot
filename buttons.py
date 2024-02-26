""""Кнопки нужно доработать!"""

# ===========================================================================
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# ===========================================================================
back_admins_button = KeyboardButton('/<назад')
back_staff_button = KeyboardButton('/<-назад')
info_button = KeyboardButton("/Информация")
# ===========================================================================
start_admins_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)

finance_button = KeyboardButton("/Финансы")
products_button = KeyboardButton("/Товары")
staff_button = KeyboardButton("/Сотрудники")

start_admins_markup.add(finance_button, products_button, staff_button, info_button)

staff_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)
products_button = KeyboardButton("/Товары")

staff_markup.add(products_button, info_button)
# ===========================================================================
products_staff_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=1
)

data_recording_button = KeyboardButton('/запись_данных_товара')

products_staff_markup.add(data_recording_button, back_staff_button)

data_recording_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
products_comming_button = KeyboardButton('/запись_прихода_товаров')
products_care_button = KeyboardButton('/запись_ухода_товара')
bookings_reg_button = KeyboardButton('/записать_бронь')

data_recording_markup.add(products_comming_button, products_care_button, bookings_reg_button, back_staff_button)

products_admins_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=1
)

data_recording_button = KeyboardButton('/запись_данных_товара')
pull_data_button = KeyboardButton('/вывести_данные_товара')

products_admins_markup.add(data_recording_button, pull_data_button, back_admins_button)

# ===========================================================================

staff_admins_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=1
)

reg_staff_reg_button = KeyboardButton('/запись_данных_сотрудников')
control_reg_button = KeyboardButton('/вывести_данные_сотрудников')

staff_admins_markup.add(reg_staff_reg_button, control_reg_button, back_admins_button)

# ===========================================================================
data_recording_staff_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
reg_staff_reg_button = KeyboardButton('/регистрация_сотрудников')
control_reg_button = KeyboardButton('/контроль_сотрудников')

data_recording_staff_markup.add(reg_staff_reg_button, control_reg_button, back_admins_button)

# ===========================================================================

staff_pull_data_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

staff_get_bishkek_button = KeyboardButton('/Сотрудники_Бишкек')
staff_get_osh_button = KeyboardButton('/Сотрудники_Ош')
staff_get_moscow_1_button = KeyboardButton('/Сотрудники_Москва')

get_being_late_bishkek_button = KeyboardButton("/Контроль_Бишкек")
get_being_late_osh_button = KeyboardButton("/Контроль_Ош")
get_being_late_moscow_1_button = KeyboardButton("/Контроль_Москва")

staff_pull_data_markup.add(staff_get_bishkek_button, staff_get_osh_button, staff_get_moscow_1_button,
                           get_being_late_bishkek_button, get_being_late_osh_button,
                     get_being_late_moscow_1_button, back_admins_button)

# ====================================================================================================================

products_pull_data_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

products_get_bishkek_button = KeyboardButton('/Бишкек')
products_get_osh_button = KeyboardButton('/Ош')
products_get_moscow_1_button = KeyboardButton('/Москва')

products_pull_data_markup.add(products_get_bishkek_button, products_get_osh_button, products_get_moscow_1_button,
                              back_admins_button)


# ===========================================================================

get_staff_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_staff_bishkek_button = KeyboardButton("/Сотрудники_Бишкек")
get_staff_osh_button = KeyboardButton("/Сотрудники_Ош")
get_staff_moscow_1_button = KeyboardButton("/Сотрудники_Москва")


get_staff_markup.add(get_staff_bishkek_button, get_staff_osh_button, get_staff_moscow_1_button,
                     back_admins_button)

# ======================================================================================================================

""" Кнопки, которые будут внутри кнопки 'Финансы' """
ButtonForFinance_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=1)
SalaryStaff_button = KeyboardButton("/Зарплаты")
regular_customers_button = KeyboardButton("/Постоянные_клиенты")
CheckoutControl_button = KeyboardButton("/Контроль_кассы")

ButtonForFinance_markup.add(SalaryStaff_button, regular_customers_button, CheckoutControl_button, back_admins_button)

SalaryStaff_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

salary_staff_bishkek = KeyboardButton("/ЗП_Бишкек")
salary_staff_osh = KeyboardButton("/ЗП_Ош")
salary_staff_moscow_1 = KeyboardButton("/ЗП_Москва")

SalaryStaff_markup.add(salary_staff_bishkek, salary_staff_osh, salary_staff_moscow_1, back_admins_button)

# ==============================

RegularСustomer_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

RegularCustomer_bishkek = KeyboardButton("/Клиенты_Бишкек")
RegularCustomer_osh = KeyboardButton("/Клиенты_Ош")
RegularCustomer_moscow_1 = KeyboardButton("/Клиенты_Москва")

RegularСustomer_markup.add(RegularCustomer_bishkek, RegularCustomer_osh, RegularCustomer_moscow_1,
                           back_admins_button)

# ==============================
control_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

control_day_Bish = KeyboardButton('/Отчет_за_день_Б')
control_month_Bish = KeyboardButton('/Отчет_за_месяц_Б')
control_week_Bish = KeyboardButton('/Отчет_за_неделю_Б')

control_day_Osh = KeyboardButton('/Отчет_за_день_Ош')
control_month_OSh = KeyboardButton('/Отчет_за_месяц_Ош')
control_week_OSh = KeyboardButton('/Отчет_за_неделю_Ош')

control_day_Moscow_1 = KeyboardButton('/Отчет_за_день_М_1')
control_month_Moscow_1 = KeyboardButton('/Отчет_за_месяц_М_1')
control_week_Moscow_1 = KeyboardButton('/Отчет_за_неделю_М_1')

control_markup.add(control_day_Bish, control_month_Bish, control_day_Osh, control_month_OSh, control_day_Moscow_1,
                   control_month_Moscow_1,
                   control_week_Bish, control_week_OSh, control_week_Moscow_1,back_admins_button)

"""-------------------------"""

# ======================================================================================================================
cancel_button = KeyboardButton('/Cancel')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    ).add(cancel_button)

cancel_button_category = KeyboardButton('/сancel')
cancel_markup_category = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    ).add(cancel_button_category)

submit_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('да'),
                                          KeyboardButton('нет'))

city_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                  one_time_keyboard=True,
                                  row_width=2
                                  ).add(KeyboardButton('Бишкек'),
                                        KeyboardButton('ОШ'),
                                        KeyboardButton('Москва'))
# ===========================================================================
"""--------ДЛЯ ДИРЕКТОРА-----------------"""
start_director_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)

finance_button_director = KeyboardButton("/Финансы")
products_button_director = KeyboardButton("/Товары")
staff_button_director = KeyboardButton("/Сотрудники")
delete_button_director = KeyboardButton("/Удаление_из_базы")

start_director_markup.add(finance_button_director, products_button_director, staff_button_director,
                        delete_button_director, info_button)


back_director_button = KeyboardButton('/<--назад')


Delete_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

delete_staff = KeyboardButton("/Бишкек_удаление")
delete_booking = KeyboardButton("/Ош_удаление")
delete_products_care = KeyboardButton("/Москва_1_удаление")


Delete_markup.add(delete_products_care, delete_booking, delete_staff, back_director_button)

Bish_delete_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

bish_delete_care_button = KeyboardButton("/Удал_Прода_Bishkek")
bish_delete_coming_button = KeyboardButton("/Удал_Прих_Bishkek")
bish_delete_bookig_button = KeyboardButton("/Удал_Броней_Bishkek")
bish_delete_staff_button = KeyboardButton("/Удал_Сотруд_Bishkek")

Bish_delete_markup.add(bish_delete_bookig_button, bish_delete_staff_button, bish_delete_coming_button, bish_delete_care_button,
                       back_director_button)



Osh_delete_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

osh_delete_care_button = KeyboardButton("/Удал_Прода_Osh")
osh_delete_coming_button = KeyboardButton("/Удал_Прих_Osh")
osh_delete_bookig_button = KeyboardButton("/Удал_Броней_Osh")
osh_delete_staff_button = KeyboardButton("/Удал_Сотруд_Osh")

Osh_delete_markup.add(osh_delete_bookig_button, osh_delete_staff_button, osh_delete_coming_button, osh_delete_care_button,
                       back_director_button)

moscow_1_delete_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

moscow_1_delete_care_button = KeyboardButton("/Удал_Прода_Moscow")
moscow_1_delete_coming_button = KeyboardButton("/Удал_Прих_Moscow")
moscow_1_delete_bookig_button = KeyboardButton("/Удал_Броней_Moscow")
moscow_1_delete_staff_button = KeyboardButton("/Удал_Сотруд_Moscow")

moscow_1_delete_markup.add(moscow_1_delete_bookig_button, moscow_1_delete_staff_button, moscow_1_delete_coming_button, moscow_1_delete_care_button,
                       back_director_button)

"""-------------------------"""


CategoryButtons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

m1 = KeyboardButton('/Обувь')
m2 = KeyboardButton('/Нижнее_белье')
m3 = KeyboardButton('/Акссесуары')
m4 = KeyboardButton('/Верхняя_одежда')
m5 = KeyboardButton('/Штаны')

CategoryButtons.add(m1, m2, m3, m4, m5, cancel_button_category)

Buttons_for_categories = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

coming_button = KeyboardButton('/Пришедшие_товары')
care_button = KeyboardButton('/Проданные_товары')
booking_button = KeyboardButton('/Товары_на_брони')

Buttons_for_categories.add(coming_button, care_button, booking_button,  back_admins_button)


CareButtons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_care_bishkek_button = KeyboardButton("/Товары_Биш(Проданные)")
get_products_care_osh_button = KeyboardButton("/Товары_Ош(Проданные)")
get_products_care_moscow_1_button = KeyboardButton("/Товары_М1(Проданные)")

CareButtons.add(get_products_care_bishkek_button, get_products_care_osh_button, get_products_care_moscow_1_button,
                back_admins_button)


Booking_Buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_booking_bishkek_button = KeyboardButton("/Брони_Бишкек")
get_booking_osh_button = KeyboardButton("/Брони_Ош")
get_booking_moscow_1_button = KeyboardButton("/Брони_Москва")

Booking_Buttons.add(get_booking_bishkek_button, get_booking_osh_button, get_booking_moscow_1_button,
                    back_admins_button)

