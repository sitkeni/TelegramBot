
from telebot import TeleBot


TOKEN = "6235950931:AAEqaoZ5MVzXuVy-HKZIFmrAsWPzzpBT0HU"
bot = TeleBot(token=TOKEN)
bot.message_handler(commands=['start', 'help'])
async def start(message):
    await msg.reply_to_message(f'Я бот .привет')
bot.message_handler(content_types=['text'])
async def start2(message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Не понимаю')
if __name__ == '__name__':
    executor.start_polling(dp)
    bot.polling(none_stop=True)
