import telebot
from telebot import types
import os

token = "7709944368:AAE17SNQaZnxRmLyhwhgP7iWcVwj8-9Tb7o"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['file'])
def read_file(message):
    try:
        with open('bot.txt') as file:
            info = file.read()
    except FileNotFoundError:
        with open('bot.txt', 'w') as file:
            file.write('')


    bot.send_message(message.chat.id, info)


@bot.message_handler(commands_types=['text'])
def read_file(message):
    file.write(message)
    bot.send_message(message.chat.id, '1')


if __name__ == '__main__':
    bot.polling()