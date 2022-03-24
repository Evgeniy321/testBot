import telebot

token=''

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(content_types=['text'])
def new_message(message):
    pass

bot.polling(none_stop = True)