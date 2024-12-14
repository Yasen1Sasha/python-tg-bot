import telebot
from telebot import types
from urllib3 import request

token = "7709944368:AAE17SNQaZnxRmLyhwhgP7iWcVwj8-9Tb7o"
bot = telebot.TeleBot(token)

def isInt(value):
    try:
        int(value)
        return True
    finally:
        return False



@bot.message_handler(content_types=['text', 'photo'])
def handler_content_type(message):
    with open('f1.txt', 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, "ok!")



if __name__ == '__main__':
    bot.polling()
