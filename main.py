import os
import requests
import telebot

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
STEAM_ID = os.getenv("STEAM_ID")

ranks = [
    "Herald", "Guardian", "Crusader",
    "Archon", "Legend", "Ancient",
    "Divine", "Immortal"
]

@bot.message_handler(commands=["MMR"])
def mmr(message):
    data = requests.get(
        f"https://api.opendota.com/api/players/{STEAM_ID}"
    ).json()

    tier = data.get("rank_tier", 0)

    if not tier:
        bot.reply_to(message, "Ранг не найден")
        return

    medal = (tier // 10) - 1
    stars = tier % 10

    if medal >= 7:
        rank = "Immortal"
    else:
        rank = f"{ranks[medal]} {stars}"

    bot.reply_to(message, rank)

bot.infinity_polling()
