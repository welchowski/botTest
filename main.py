import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("старт команда!")


@dp.message_handler(commands=['plus'])
async def plus(message: types.Message):
    await message.answer(message.text*2)


if __name__ == '__main__':

    executor.start_polling(dp)
