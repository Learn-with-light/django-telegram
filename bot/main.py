import telebot

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=["start"])
def startFunc(message):
    bot.reply_to(message, "HELLO")

bot.infinity_polling()