import telebot

TOKEN = "7706743761:AAHO3-x0EZ-TTETMq5obr-OhKRzQhjqkFY0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func = lambda
message: True)

def reply_yes(message):
    bot.reply_to(message, "ИДИ НАХУЙ")

bot.infinity_polling()