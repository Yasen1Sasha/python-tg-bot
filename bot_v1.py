import telebot
from telebot import types
from urllib3 import request

token = "7709944368:AAE17SNQaZnxRmLyhwhgP7iWcVwj8-9Tb7o"
bot = telebot.TeleBot(token)



@bot.message_handler(content_types=['text', 'photo'])
def handler_content_type(message):
    if message.text == '1':
        request = 'Один'
    elif message.text == '2':
        request = 'Два'
    elif message.text == '3':
        request = 'Три'
    elif message.text == '4':
        request = 'Чотири'
    elif message.text == '5':
        request = 'Пять'
    else:
        request = 'Не ЗНАЙДЕНО'

    bot.send_message(message.chat.id, request)


if __name__ == '__main__':
    bot.polling()

