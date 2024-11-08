from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio as ao

api = "7432996332:AAGbCX_guIoB9ZARz_4M9yVz-7TxxCFJ_VA" # Вставьте токен своего бота!
bot = Bot(token = api)
dp = Dispatcher(bot = bot, storage = MemoryStorage())


class UserState(StatesGroup):
    age = State() #возраст
    growth = State()# рост
    weight = State()# вес
    gender = State()# пол

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью, введите Calories.')

@dp.message_handler(text = "Calories")
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

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
            await message.answer(f"Ваша норма калорий: {10 * weight + 6.25 * growth - 4.92 * age + 5}")
        elif data['gender'].lower() == "женский":
            await message.answer(f"Ваша норма калорий: {10 * weight + 6.25 * growth - 4.92 * age - 161}")
        else:
            await message.answer("Неверно введен пол, попробуйте снова, введя 'Calories'")
    except:
        await message.answer("Неверно введены данные, попробуйте снова, введя 'Calories'")
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start или Calories, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



