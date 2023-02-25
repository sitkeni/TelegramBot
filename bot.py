import telebot

bot = telebot.TeleBot('6235950931:AAEqaoZ5MVzXuVy-HKZIFmrAsWPzzpBT0HU')
bot.message_handler(content_types=['start'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == '/help':
        bot.send_message(message.from_user.id,"не понимэ")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
