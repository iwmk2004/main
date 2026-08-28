import os
import requests
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
STEAM_ID = os.getenv("STEAM_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["last"])
def last_game(message):
    try:
        url = f"https://api.opendota.com/api/players/{STEAM_ID}/recentMatches"
        games = requests.get(url, timeout=10).json()

        if not games:
            bot.reply_to(message, "Игр не найдено")
            return

        game = games[0]

        result = "Победа" if game["player_slot"] < 128 and game["radiant_win"] else \
                 "Поражение" if game["player_slot"] < 128 else \
                 "Поражение" if game["radiant_win"] else "Победа"

        minutes = game["duration"] // 60
        seconds = game["duration"] % 60

        text = (
            f"Последняя катка\n\n"
            f"{result}\n"
            f"Hero ID: {game['hero_id']}\n"
            f"K/D/A: {game['kills']}/{game['deaths']}/{game['assists']}\n"
            f"Длительность: {minutes}:{seconds:02d}\n"
            f"Match ID: {game['match_id']}"
        )

        bot.reply_to(message, text)

    except Exception as e:
        bot.reply_to(message, "Ошибка получения игры")

bot.infinity_polling()
