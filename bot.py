import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN is missing!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Sveika, Anda! Tavs bots ir dzīvs 🌿")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"Tu uzrakstīji: {message.text}")

print("Bot is running...")
bot.infinity_polling()

