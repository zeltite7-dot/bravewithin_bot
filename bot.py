import os
import random
import telebot
from telebot import types
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# ============================
#   BOT INIT
# ============================

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

# ============================
#   RITUĀLI — ŠEIT IELIEC SAVAS 1.–10. DIENAS
# ============================

rituali = {
    # ⬇⬇⬇ ŠEIT IELIEC VISAS SAVAS DIENAS ⬇⬇⬇

    # 1: {
    #     "rits": """...""",
    #     "vakars": """..."""
    # },

    # ... līdz 10. dienai ...

    # ⬆⬆⬆ TIKAI ŠO DAĻU AIZPILDI ⬆⬆⬆
}

# ============================
#   DIENAS NOTEIKŠANA
# ============================

def get_day():
    day = datetime.now().day % 10
    return 10 if day == 0 else day

# ============================
#   RANDOM IEDVESMAS TEIKUMI
# ============================

iedvesmas = [
    "Tu esi maigāka nekā tu domā.",
    "Šodien nav jābūt perfektai — pietiek būt klātesošai.",
    "Tava elpa ir tavs drošais pamats.",
    "Tu drīksti atpūsties.",
    "Tu esi pietiekama tieši tāda, kāda esi.",
    "Miers sākas ar vienu ieelpu.",
    "Tu drīksti būt lēna.",
    "Tu esi drošībā savā ķermenī."
]

# ============================
#   GALVENĀS INLINE POGAS
# ============================

def main_menu():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("🌅 Šodienas rīts", callback_data="rits"),
        types.InlineKeyboardButton("🌙 Šodienas vakars", callback_data="vakars")
    )
    keyboard.add(
        types.InlineKeyboardButton("💛 Dienas nodoms", callback_data="nodoms"),
        types.InlineKeyboardButton("🌬 Elpošana", callback_data="elpa")
    )
    keyboard.add(
        types.InlineKeyboardButton("✨ Random iedvesma", callback_data="iedvesma"),
        types.InlineKeyboardButton("📈 Dienas progress", callback_data="progress")
    )
    keyboard.add(
        types.InlineKeyboardButton("🧘‍♀️ Ķermeņa skenēšana", callback_data="skens"),
        types.InlineKeyboardButton("💬 Emociju check‑in", callback_data="emocijas")
    )
    keyboard.add(
        types.InlineKeyboardButton("🎤 Balss ziņa", callback_data="balss")
    )
    return keyboard

# ============================
#   /start KOMANDA
# ============================

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Sveika, Anda 🌿\nIzvēlies, ko vēlies saņemt:",
        reply_markup=main_menu()
    )

# ============================
#   INLINE POGU APSTRĀDE
# ============================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    day = get_day()

    if call.data == "rits":
        bot.send_message(call.message.chat.id, rituali[day]["rits"], parse_mode="Markdown")

    elif call.data == "vakars":
        bot.send_message(call.message.chat.id, rituali[day]["vakars"], parse_mode="Markdown")

    elif call.data == "nodoms":
        try:
            text = rituali[day]["rits"].split("*Nodoms*")[1].split("*")[0].strip()
            bot.send_message(call.message.chat.id, f"💛 *Šodienas nodoms:*\n{text}", parse_mode="Markdown")
        except:
            bot.send_message(call.message.chat.id, "💛 Nodoms nav atrasts.")

    elif call.data == "elpa":
        try:
            text = rituali[day]["rits"].split("*Elpošana*")[1].split("*")[0].strip()
            bot.send_message(call.message.chat.id, f"🌬 *Elpošanas vingrinājums:*\n{text}", parse_mode="Markdown")
        except:
            bot.send_message(call.message.chat.id, "🌬 Elpošanas apraksts nav atrasts.")

    elif call.data == "iedvesma":
        bot.send_message(call.message.chat.id, "✨ " + random.choice(iedvesmas))

    elif call.data == "progress":
        bot.send_message(
            call.message.chat.id,
            f"📈 *Tavs progress*\nŠodien ir *{day}. diena* no 10.\nTu ej ļoti skaistu ceļu.",
            parse_mode="Markdown"
        )

    elif call.data == "skens":
        text = """🧘‍♀️ *Ķermeņa skenēšana*

Aizver acis uz brīdi.

1. Sajūti pēdas.
2. Sajūti kājas.
3. Sajūti gurnus.
4. Sajūti vēderu.
5. Sajūti krūtis.
6. Sajūti plecus.
7. Sajūti kaklu.
8. Sajūti seju.

Ieelpo lēni. Izelpo vēl lēnāk."""
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

    elif call.data == "emocijas":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("😊 Labi", callback_data="emo_labi"),
            types.InlineKeyboardButton("😐 Neitrāli", callback_data="emo_ok"),
            types.InlineKeyboardButton("😔 Grūti", callback_data="emo_gruti")
        )
        bot.send_message(call.message.chat.id, "💬 Kā tu jūties šobrīd?", reply_markup=keyboard)

    elif call.data == "emo_labi":
        bot.send_message(call.message.chat.id, "😊 Prieks dzirdēt. Saglabā šo sajūtu sevī.")

    elif call.data == "emo_ok":
        bot.send_message(call.message.chat.id, "😐 Neitrāli ir labi. Tu esi klātesoša.")

    elif call.data == "emo_gruti":
        bot.send_message(call.message.chat.id, "😔 Es esmu ar tevi. Ieelpo lēni. Tu neesi viena.")

    elif call.data == "balss":
        bot.send_message(
            call.message.chat.id,
            "🎤 Tu vari man nosūtīt balss ziņu.\nEs to saņemšu un maigi atbildēšu tekstā."
        )

# ============================
#   BALSS ZIŅU APSTRĀDE
# ============================

@bot.message_handler(content_types=['voice'])
def voice_reply(message):
    bot.send_message(
        message.chat.id,
        "🎤 Es saņēmu tavu balss ziņu.\nPaldies, ka dalies.\nTu vari man rakstīt vai nospiest kādu no pogām."
    )

# ============================
#   AUTOMĀTISKĀ SŪTĪŠANA
# ============================

CHAT_ID = 941689479  # <-- nomaini, ja vajag

def send_morning():
    day = get_day()
    bot.send_message(CHAT_ID, rituali[day]["rits"], parse_mode="Markdown")

def send_evening():
    day = get_day()
    bot.send_message(CHAT_ID, rituali[day]["vakars"], parse_mode="Markdown")

scheduler = BackgroundScheduler()
scheduler.add_job(send_morning, 'cron', hour=8, minute=0)
scheduler.add_job(send_evening, 'cron', hour=20, minute=0)
scheduler.start()

# ============================
#   PALAIŠANA
# ============================

bot.infinity_polling()
