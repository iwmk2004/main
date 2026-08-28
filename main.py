import os
import requests
import telebot

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
STEAM_ID = os.getenv("STEAM_ID")

ranks = [
    "Unranked",
    "Herald",
    "Guardian",
    "Crusader",
    "Archon",
    "Legend",
    "Ancient",
    "Divine",
    "Immortal"
]

@bot.message_handler(commands=["MMR", "mmr"])
def get_mmr(message):
    try:
        data = requests.get(
            f"https://api.opendota.com/api/players/{STEAM_ID}",
            timeout=10
        ).json()

        tier = data.get("rank_tier")

        if not tier:
            bot.reply_to(message, "Ранг не найден")
            return

        rank = tier // 10
        stars = tier % 10

        if rank >= 8:
            text = "Immortal"
        else:
            text = f"{ranks[rank]} {stars}"

        bot.reply_to(message, text)

    except Exception as e:
        bot.reply_to(message, "Ошибка получения ранга")

bot.infinity_polling()
