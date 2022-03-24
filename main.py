import telebot

token=''

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == "привет":
        bot.send_message(message.chat.id, "И тебе привет!")
    elif message.text == "как дела":
        bot.send_message(message.chat.id, "Отлично! А у тебя?")
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понимаю")

bot.polling(none_stop = True)