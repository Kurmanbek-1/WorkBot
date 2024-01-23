from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from aiogram.dispatcher.filters import Text
from db.sql_commands.utils import get_product_from_category
import os
import asyncpg
from config import POSTGRES_URL, DESTINATION

cities = ['Бишкек', 'ОШ', 'Москва 1-филиал', 'Ош 2-филиал']
categories = ["/Обувь", "/Нижнее_белье", "/Акссесуары", "/Верхняя_одежда", "/Штаны"]


# Создаем единый глобальный пул соединений
db_pool = None


class AllProductsForCategoryFSM(StatesGroup):
    city = State()
    category = State()


async def fsm_start(message: types.Message):
    await AllProductsForCategoryFSM.city.set()
    await message.answer('Филиал? ⬇', reply_markup=buttons.city_markup)


async def load_city(message: types.Message, state: FSMContext):
    if message.text in cities:
        async with state.proxy() as data_category:
            data_category['city'] = message.text
        await AllProductsForCategoryFSM.next()
        await message.answer('Категория?', reply_markup=buttons.CategoryButtons)  # Добавить кнопку с категориями

    else:
        await message.answer('Вы ввели не тот филиал!')


async def get_db_pool():
    global db_pool
    if db_pool is None:
        db_pool = await asyncpg.create_pool(POSTGRES_URL)
    return db_pool


# Модифицируем функцию load_category
async def load_category(message: types.Message, state: FSMContext):
    pool = await get_db_pool()

    async with state.proxy() as data_category:
        if message.text in categories:
            city = data_category['city']
            category = message.text.replace("/", "")

            if city == "Бишкек":
                products = await get_product_from_category(pool=pool, category=category, city=city)
            elif city == "ОШ":
                products = await get_product_from_category(pool=pool, category=category, city=city)
            elif city == "Москва 1-филиал":
                products = await get_product_from_category(pool=pool, category=category, city=city)
            elif city == "Ош 2-филиал":
                products = await get_product_from_category(pool=pool, category=category, city=city)

            for product in products:
                photo_path = product[9]

                # Проверка существования файла
                if not os.path.exists(photo_path):
                    print(f"Файл не найден: {photo_path}")
                    continue  # Продолжить с следующим товаром

                # Попытка открыть файл изображения
                try:
                    with open(photo_path, 'rb') as photo:
                        await message.answer_photo(photo=photo, caption=f"Товар: {product[1]}\n"
                                                                        f"Информация о товаре: {product[2]}\n"
                                                                        f"Дата прихода: {product[3]}\n"
                                                                        f"Цена: {product[4]}\n"
                                                                        f"Город: {product[5]}\n"
                                                                        f"Категория: {product[6]}\n"
                                                                        f"Артикул: {product[7]}\n"
                                                                        f"Количество: {product[8]}\n",
                                                   reply_markup=buttons.CategoryButtons)
                except Exception as e:
                    print(f"Ошибка при открытии файла {photo_path}: {e}")
                    continue  # Продолжить с следующим товаром
        else:
            await message.answer("Филиал не выбран. Выберите филиал сначала.")


async def cancel_reg_category(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start_admins_markup)


def register_fsm_comitCategory(dp: Dispatcher):
    dp.register_message_handler(cancel_reg_category, Text(equals='/сancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['Пришедшие_товары'])

    dp.register_message_handler(load_city, state=AllProductsForCategoryFSM.city)
    dp.register_message_handler(load_category, state=AllProductsForCategoryFSM.category)
