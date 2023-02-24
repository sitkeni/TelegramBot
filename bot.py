from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
TOKEN = "6235950931:AAEqaoZ5MVzXuVy-HKZIFmrAsWPzzpBT0HU"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['/start', '/help'])
async def send_welcom(msg: types.message):
    await msg.reply_to_message(f'Я бот .привет, {msg.from_user.first_name}')
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Не понимаю')
if __name__ == '__name__':
    executor.start_polling(dp)
