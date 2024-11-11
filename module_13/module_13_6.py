from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio as ao
import json
api = "" # Вставьте токен своего бота!
bot = Bot(token = api)
dp = Dispatcher(bot = bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup()
but1 = KeyboardButton(text = "Рассчитать")
but2 = KeyboardButton(text = "Информация")

kb.add(but1)
kb.insert(but2)
kb.resize_keyboard = True

in_kb = InlineKeyboardMarkup()
cal = InlineKeyboardButton(text = "Рассчитать норму калорий", callback_data = "calories")
form = InlineKeyboardButton(text = "Формулы расчёта", callback_data = "formulas")
in_kb.add(cal)
in_kb.insert(form)

in_kb2 = InlineKeyboardMarkup()
M = InlineKeyboardButton(text = "Мужской", callback_data = "М")
J = InlineKeyboardButton(text = "Женский", callback_data = "Ж")
in_kb2.add(M)
in_kb2.insert(J)
class UserState(StatesGroup):
    age = State() #возраст
    growth = State()# рост
    weight = State()# вес
    gender = State()# пол

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью, выберите одно из действий!', reply_markup = kb)

@dp.message_handler(text = "Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup = in_kb)

@dp.callback_query_handler(text = "formulas")
async def get_formulas(call):
    await call.message.answer("Выберите пол:", reply_markup = in_kb2)
    await call.answer()

@dp.callback_query_handler(text = "М")
async def M(call):
    await call.message.answer("10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) + 5", reply_markup = kb)
    await call.answer()

@dp.callback_query_handler(text = "Ж")
async def J(call):
    await call.message.answer("10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161", reply_markup = kb)
    await call.answer()
@dp.callback_query_handler(text = "calories")
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()
@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def set_gender(message, state):
    await state.update_data(weight = message.text)
    await message.answer('Введите свой пол:')
    await UserState.gender.set()



@dp.message_handler(state = UserState.gender)
async def send_calories(message, state):
    await state.update_data(gender = message.text)
    try:
        data = await state.get_data()
        weight = int(data['weight'])
        growth = int(data['growth'])
        age = int(data['age'])
        if data['gender'].lower() == "мужской":
            await message.answer(f"Ваша норма калорий: {10 * weight + 6.25 * growth - 4.92 * age + 5}", reply_markup = kb)
        elif data['gender'].lower() == "женский":
            await message.answer(f"Ваша норма калорий: {10 * weight + 6.25 * growth - 4.92 * age - 161}", reply_markup = kb)
        else:
            await message.answer("Неверно введен пол, попробуйте снова!", reply_markup = kb)
    except:
        await message.answer("Неверно введены данные, попробуйте снова!", reply_markup = kb)
    await state.finish()

@dp.message_handler(text = "Информация")
async def info(message):
    await message.answer("Данная функция пока что в разработке, попробуйте другую!", reply_markup = kb)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



