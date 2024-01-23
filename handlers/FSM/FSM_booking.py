# =======================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import buttons

from db.db_main.ORM_main import sql_booking_insert
from datetime import datetime


# =======================================================================================================
class fsm_booking_coming(StatesGroup):
    name_product = State()  # Название товара
    start_booking = State()  # Дата началы брони
    care_booking = State()  # Дата началы брони
    name_customer = State()  # Имя заказчика
    phone_customer = State()  # Номер телефона заказчика
    name_salesman = State()  # Имя продавца
    phone_salesman = State()  # Телефон номера продавца
    price = State()  # Цена
    discount = State()  # Скидка
    city = State()  # Итоговая цена
    photo_booking = State()  # Фотография товара
    submit = State()


async def fsm_start(message: types.Message):
    await fsm_booking_coming.name_product.set()
    await message.answer('Название товара?', reply_markup=buttons.cancel_markup)


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text
    await fsm_booking_coming.next()
    await message.answer('Начало брони?\n'
                         'Образец: 12.09.23')


async def load_start_of_armor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['start_of_armor'] = message.text
    await fsm_booking_coming.next()
    await message.answer('Конец брони?\n'
                         'Образец: 12.09.23')


async def load_end_of_armor_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['end_of_armor'] = message.text
    await fsm_booking_coming.next()
    await message.answer('Имя заказчика?')


async def load_name_customer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_customer'] = message.text
    await fsm_booking_coming.next()
    await message.answer('Номер телефона заказчика? \n'
                         'Начать нужно через "+"')


async def load_phone_customer(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone_customer'] = message.text
        await fsm_booking_coming.next()
        await message.answer('Имя продавца?')


async def load_name_salesman(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_salesman'] = message.text
    await fsm_booking_coming.next()
    await message.answer('Номер телефона продавца? \n'
                         'Начать нужно через "+"')


async def load_phone_salesman(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone_salesman'] = message.text
        await fsm_booking_coming.next()
        await message.answer('Цена?\n'
                             '(Без скидки)')


async def load_price(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['price'] = message.text
        await fsm_booking_coming.next()
        await message.answer('Скидка?\n'
                             '(Сумму скидки!)')
    else:
        await message.answer('Укажите цифрами!')


async def load_discount(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['discount'] = int(message.text)
            data['calculation'] = int(data['price']) - int(data['discount'])

        await fsm_booking_coming.next()
        await message.answer('Город?\n'
                             'Если Москва, то указать какой филиал!\n'
                             'Выберите снизу по кнопкам, какой город!',
                             reply_markup=buttons.city_markup)
    else:
        await message.answer('Укажите цифрами!')


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    await fsm_booking_coming.next()
    await message.answer('Фотография товара !?')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        data['date'] = datetime.now()
        await message.answer_photo(
            data["photo"],
            caption=f"Данные брони: \n"
                    f"Название товара: {data['name_product']}\n"
                    f"Начало брони: {data['start_of_armor']}\n"
                    f"Конец брони: {data['end_of_armor']}\n"
                    f"Заказчик: {data['name_customer']}\n"
                    f"Номер телефона заказчика: {data['phone_customer']}\n"
                    f"Продацев: {data['name_salesman']}\n"
                    f"Цена: {data['price']}\n"
                    f"Скидка: {data['discount']}\n"
                    f"Итоговая цена: {data['calculation']}\n"
                    f"Город: {data['city']}\n\n"
                    f"‼️Внимание! "
                    f"Если вы записали бронь, то после продажи вы должны его записать как проданную(Заполнить в проданных)")
    await fsm_booking_coming.next()
    await message.answer("Все верно?", reply_markup=buttons.submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':

            await sql_booking_insert(state)
            await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
            await state.finish()


        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=buttons.data_recording_markup)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.data_recording_markup)


# =======================================================================================================================

def register_booking(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='/Cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['записать_бронь'])

    dp.register_message_handler(load_name_product, state=fsm_booking_coming.name_product)
    dp.register_message_handler(load_start_of_armor, state=fsm_booking_coming.start_booking)
    dp.register_message_handler(load_end_of_armor_care, state=fsm_booking_coming.care_booking)
    dp.register_message_handler(load_name_customer, state=fsm_booking_coming.name_customer)
    dp.register_message_handler(load_phone_customer, state=fsm_booking_coming.phone_customer)
    dp.register_message_handler(load_name_salesman, state=fsm_booking_coming.name_salesman)
    dp.register_message_handler(load_phone_salesman, state=fsm_booking_coming.phone_salesman)
    dp.register_message_handler(load_price, state=fsm_booking_coming.price)
    dp.register_message_handler(load_discount, state=fsm_booking_coming.discount)
    dp.register_message_handler(load_city, state=fsm_booking_coming.city)
    dp.register_message_handler(load_photo, state=fsm_booking_coming.photo_booking, content_types=['photo'])
    dp.register_message_handler(load_submit, state=fsm_booking_coming.submit)

    # =======================================================================================================================
