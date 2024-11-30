import telebot
from telebot import types

token = '7709944368:AAE17SNQaZnxRmLyhwhgP7iWcVwj8-9Tb7o'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 'Komanda start')


#@bot.message_handler(commands=['stop'])
def command_stop(message):
    bot.send_message(message.chat.id, 'Komanda stop')


@bot.message_handler(commands=['open', 'close'])
def bot_comands(message):
     mes = ''

     if message.text =='/open':
         mes = 'Open'
     elif message.text == '/close':
         mes = 'Close'


     bot.send_message(message.chat.id, mes)

@bot.message_handler(commands=['key'])
def key_go(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='/start')
    button_2 = types.KeyboardButton(text='/stop')
    button_3 = types.KeyboardButton(text='/close')
    button_4 = types.KeyboardButton(text='/open')

    keyboard.add(button_1, button_2, button_3, button_4)

    bot.send_message(message.chat.id, 'Keyboard', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text =='knopka1')
def handle_button_1(message):
    bot.send_message(message.chat.id, 'Ви натиснули кнопку 1.')


@bot.message_handler(commands=['sticker'])
def handle_sticker(message):
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji

    bot.reply_to(message, f"Ви надіслали стікер з емоджі{emoji} (ID:{sticker_id})" )





def bot_button_if(message):
    pass

bot.polling()
