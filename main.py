import telebot

token = '7577622624:AAFwA-REaztaByFKllR0MHbUHX1azrY6T_c'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def botmessage(message):
    mes = message.text + ' - Це написав класний хлопець!'
    bot.send_message(message.chat.id, mes)


bot.polling()
