from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio




API_TOKEN = '7897509856:AAGzyktr7yNuVXHVsofX0Hj_mEMVJn_RvRE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):

    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
