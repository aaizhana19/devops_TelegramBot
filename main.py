import telebot

bot = telebot.TeleBot("5785707050:AAG0lbLcERao0xx-bq0JG0i6KuNxChpwQuc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	bot.send_message(message.chat.id,"Bot by Aizhan Tazhibay")

	if "crush" in message.text:
		g = 5/0

bot.infinity_polling()