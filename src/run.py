from time import sleep
import telebot
import random

TOKEN = '*'
bot = telebot.TeleBot(TOKEN)


# command /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, I new your a friend')


# random_num

@bot.message_handler(commands=['random_num'])
def random_num(message):
    num = random.randint(0, 100)
    bot.send_message(message.chat.id, str(num))  # чтобы бот мог отправлять сообщения приводим всё к строке str()


# text
@bot.message_handler(content_types=['text'])
def text(message):
    # lower() register
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello, world')
    if message.text == 'Viva':
        bot.send_message(message.chat.id, 'Hello, Vova')


bot.polling()
