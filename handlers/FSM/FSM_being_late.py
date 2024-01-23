# =======================================================================================================================
from datetime import date

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import buttons

from db.db_main.ORM_main import sql_being_late_insert


# =======================================================================================================================

class fsm_control(StatesGroup):
    full_name = State()
    date = State()
    time = State()
    city = State()
    submit = State()


async def fsm_start(message: types.Message):
    await fsm_control.full_name.set()
    await message.answer('ФИО сотрудника?', reply_markup=buttons.cancel_markup)


async def load_full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text
    await fsm_control.next()
    await message.answer("Дата?\n"
                         "Образец: 12 августа")


async def load_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_coming'] = message.text
    await fsm_control.next()
    await message.answer('Время прихода?\n'
                         'Образец: 9:34')


async def load_time(message: types.Message, state: FSMContext):
    # Вот здесь прописать логику, если челик опоздал, то отправить ему сообщение
    # Либо для всех установить одно время и, если он опоздал, то сказать что он опоздал
    async with state.proxy() as data:
        data['time'] = message.text
    await fsm_control.next()
    await message.answer('Город?\n'
                         'Если Москва, то указать какой филиал!\n'
                         'Выберите снизу по кнопкам, какой город!',
                         reply_markup=buttons.city_markup)


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        data['date'] = date.today()
        await message.answer(f'Данные: \n'
                             f'ФИО: {data["full_name"]}\n'
                             f'Дата: {data["date"]}\n'
                             f'Время прибытия: {data["time"]}\n'
                             f'Город: {data["city"]}')

    await fsm_control.next()
    await message.answer('Всё верно?', reply_markup=buttons.submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            await sql_being_late_insert(state)
            await message.answer('Готово!', reply_markup=buttons.start_admins_markup)
            await state.finish()

        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=buttons.start_admins_markup)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start_admins_markup)


# =======================================================================================================================

def register_control(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='/Cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['контроль_сотрудников'])
    dp.register_message_handler(load_full_name, state=fsm_control.full_name)
    dp.register_message_handler(load_data, state=fsm_control.date)
    dp.register_message_handler(load_time, state=fsm_control.time)
    dp.register_message_handler(load_city, state=fsm_control.city)

    dp.register_message_handler(load_submit, state=fsm_control.submit)
