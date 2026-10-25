import os
import telebot
from yt_dlp import YoutubeDL

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "All Video Saver yana aiki! Turo link")

@bot.message_handler(func=lambda m: True)
def download_video(m):
    url = m.text
    if "http" not in url:
        return
    bot.send_message(m.chat.id, "Ina saukewa...")
    try:
        ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4', 'quiet': True}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        with open('video.mp4', 'rb') as v:
            bot.send_video(m.chat.id, v)
    except:
        bot.reply_to(m, "Ban iya saukewa ba")

bot.polling()
