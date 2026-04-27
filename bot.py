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
@bot.message_handler(commands=['anda'])
def secret(message):
    bot.send_message(
        message.chat.id,
        "🌙 Tavs slepenais maigais brīdis.\n\n"
        "Tu esi drošībā. Tu drīksti atlaist visu, kas šobrīd ir par daudz.\n"
        "Ieelpo lēni… un ļauj sev būt tieši tā, kā tu esi.\n\n"
        "Tu esi pietiekama."
    )
print("Bot is running...")
bot.infinity_polling()


