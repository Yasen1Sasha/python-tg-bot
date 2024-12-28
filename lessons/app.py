import telebot
from telebot import types
import os

token = "7709944368:AAE17SNQaZnxRmLyhwhgP7iWcVwj8-9Tb7o"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, ' Start!')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    mes = message.text + 'Довжина рядка' + str(len(message.text)) + 'сантиметрів'
    bot.send_message(message.chat.id, mes)


if __name__ == '__main__':
    bot.polling()


