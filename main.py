import telebot
from telebot import types

token = '7709944368:AAE17SNQaZnxRmLyhwhgP7iWcVwj8-9Tb7o'

bot = telebot.TeleBot(token)


#@bot.message_handler(commands=['/b'])


@bot.message_handler(commands=['tato', 'mama', 'b'])
def bot_comands(message):
     mes = ''

     if message.text =='/tato':
         mes = 'Иди па плачь'
     elif message.text == '/mama':
         mes = 'ти пакакал'
     elif message.text == '/b':
         bot_buttons(message)
         return True

     bot.send_message(message.chat.id, mes)




@bot.message_handler(content_types=['text'])
def bot_message(message):
    mes = message.text + ' - Максимка скорей в укритие ани стреляют тваражком!'
    bot.send_message(message.chat.id, mes)
def bot_buttons(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    button_1 = types.KeyboardButton(text='/mama')
    button_2 = types.KeyboardButton(text='/tato')
    button_3 = types.KeyboardButton(text='КНОПКА 3')
    button_4 = types.KeyboardButton(text='КНОПКА 4')

    keyboard.add(button_1, button_2, button_3, button_4)

    msg = bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    bot.register_next_step_handler(msg, button_if)

def bot_button_if(message):
    pass

bot.polling()
