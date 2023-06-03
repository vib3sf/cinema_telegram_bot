import telebot
from get_random_film import get_random_film

token = '6085899633:AAFOEflDKHI4vF1JM22cjZjKQeggnK89wtw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def get_film(message):
    bot.send_message(message.chat.id, get_random_film())


if __name__ == '__main__':
    bot.infinity_polling()

