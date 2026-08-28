import os
import requests
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
STEAM_ID = os.getenv("STEAM_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["MMR"])
def get_mmr(message):
    data = requests.get(
        f"https://api.opendota.com/api/players/{STEAM_ID}"
    ).json()

    mmr = data["mmr_estimate"]["estimate"]
    bot.send_message(message.chat.id, f"MMR: {mmr}")

bot.infinity_polling()
