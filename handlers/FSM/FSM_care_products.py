# =======================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import buttons
import asyncpg
from config import POSTGRES_URL, DESTINATION
from db.db_main.ORM_main import sql_product_care_insert
from db.sql_commands.utils import update_product_coming_quantity, get_product_from_articul
from datetime import date

# =======================================================================================================================
global connection
connection = asyncpg.connect(POSTGRES_URL)


class FsmCareProducts(StatesGroup):
    date_care = State()  # Дата где будут записаны уходы
    name_customer = State()
    phone_customer = State()
    name_salesman = State()
    phone_salesman = State()
    price = State()
    discount = State()
    city = State()
    articul = State()
    quantity = State()
    submit = State()


async def fsm_start(message: types.Message):
    await FsmCareProducts.date_care.set()
    await message.answer('Дата ухода?', reply_markup=buttons.cancel_markup)


async def load_date_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_care'] = message.text
    await FsmCareProducts.next()
    await message.answer('Имя заказчика?')


async def load_name_customer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_customer'] = message.text
    await FsmCareProducts.next()
    await message.answer('Номер телефона заказчика? \n'
                         '+996 или +7')


async def load_phone_customer(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone_customer'] = message.text
        await FsmCareProducts.next()
        await message.answer('Имя продавца?')


async def load_name_salesman(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_salesman'] = message.text
    await FsmCareProducts.next()
    await message.answer('Номер телефона продавца? \n'
                         '+996 или +7')


async def load_phone_salesman(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone_salesman'] = message.text
        await FsmCareProducts.next()
        await message.answer('Цена?')


async def load_price(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['price'] = message.text
        await FsmCareProducts.next()
        await message.answer('Скидка?\n'
                             '(Сумму скидки!)')
    else:
        await message.answer('Укажите цифрами!')


async def load_discount(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['discount'] = int(message.text)
            data['calculation'] = int(data['price']) - int(data['discount'])

        await FsmCareProducts.next()
        await message.answer('Город?\n'
                             'Если Москва, то указать какой филиал!\n'
                             'Выберите снизу по кнопкам, какой город!',
                             reply_markup=buttons.city_markup)
    else:
        await message.answer('Укажите цифрами!')


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await FsmCareProducts.next()
    await message.answer('Артикул товара?', reply_markup=buttons.cancel_markup)


async def load_articul(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['articul'] = message.text
        async with asyncpg.create_pool(POSTGRES_URL) as pool:
            async with pool.acquire() as connection:
                global product_coming_data
                product_coming_data = await get_product_from_articul(cursor=connection, articul=data['articul'],
                                                                     city=data['city'])
        await FsmCareProducts.next()
        await message.answer('Количество товара?')
    else:
        await message.answer("Артикул должен состоять из цифр!!!")


async def load_quantity(message: types.Message, state: FSMContext):
    try:
        if message.text.isalnum():
            async with state.proxy() as data:
                data['quantity'] = int(message.text)
                data['photo'] = product_coming_data[2]
                data['name'] = product_coming_data[0]
                data['info'] = product_coming_data[1]
                data['date'] = date.today()

                # Чтение содержимого файла
                with open(f"{product_coming_data[2]}", 'rb') as photo_file:
                    data['photo_content'] = photo_file.read()

                await FsmCareProducts.next()

            await message.answer_photo(
                photo=data['photo_content'],
                caption=f"Данные товара: \n"
                        f"АРТИКУЛ: {data['articul']}\n"
                        f"Название товара: {data['name']}\n"
                        f"Информация о товаре: {data['info']}\n"
                        f"Дата ухода товара: {data['date_care']}\n"
                        f"Заказчик: {data['name_customer']}\n"
                        f"Номер телефона заказчика: {data['phone_customer']}\n"
                        f"Продацев: {data['name_salesman']}\n"
                        f"Цена: {data['price']}\n"
                        f"Скидка: {data['discount']}\n"
                        f"Итоговая цена: {data['calculation']}\n"
                        f"Город: {data['city']}")
            await message.answer("Все верно?", reply_markup=buttons.submit_markup)

        else:
            await message.answer('Вводите только числа!')

    except TypeError:
        photo = open('media/404_error-h.png', 'rb')
        await message.answer_photo(photo, caption="Упс!\n"
                                                  "Вы ввели неправильный артикул\n"
                                                  "Пожалуйста, нажмите на кнопку 'Отмена'\n"
                                                  "И заполните заново эту запись!")


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            pool = await asyncpg.create_pool(POSTGRES_URL)
            await update_product_coming_quantity(pool=pool, quantity=data['quantity'], articul=data['articul'])
            await sql_product_care_insert(state)
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

def register_products(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='/Cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['запись_ухода_товара'])

    # dp.register_message_handler(load_name, state=FsmCareProducts.name)
    # dp.register_message_handler(load_info_product, state=FsmCareProducts.info_product)
    dp.register_message_handler(load_date_care, state=FsmCareProducts.date_care)
    dp.register_message_handler(load_name_customer, state=FsmCareProducts.name_customer)
    dp.register_message_handler(load_phone_customer, state=FsmCareProducts.phone_customer)
    dp.register_message_handler(load_name_salesman, state=FsmCareProducts.name_salesman)
    dp.register_message_handler(load_phone_salesman, state=FsmCareProducts.phone_salesman)
    dp.register_message_handler(load_price, state=FsmCareProducts.price)
    dp.register_message_handler(load_discount, state=FsmCareProducts.discount)
    dp.register_message_handler(load_city, state=FsmCareProducts.city)
    dp.register_message_handler(load_articul, state=FsmCareProducts.articul)
    dp.register_message_handler(load_quantity, state=FsmCareProducts.quantity)
    dp.register_message_handler(load_submit, state=FsmCareProducts.submit)
