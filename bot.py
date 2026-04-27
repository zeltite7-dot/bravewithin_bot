import os
import telebot
from telebot import types

# ============================
#   TOKEN & BOT INITIALIZĀCIJA
# ============================

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN is missing!")

bot = telebot.TeleBot(TOKEN)


# ============================
#        RĪTA CIKLS
# ============================

def morning_text():
    return (
        "🌅 *Rīta maigais sākums*\n\n"
        "Labrīt. Ieelpo. Ļauj sev pamosties lēni.\n\n"
        "Šodienas nodoms: *“Es izvēlos būt klātesoša sev.”*\n\n"
        "Pajautā sev: kā jūtas mani pleci, mana sirds, mana elpa?"
    )

def morning_breath():
    return (
        "🌬 Rīta elpa\n\n"
        "Ieelpa 4… pauze 2… izelpa 6…\n"
        "Atkārto 3 reizes, ļoti lēni."
    )

def morning_task():
    return (
        "💛 Dienas uzdevums\n\n"
        "Šodien pamēģini 2 minūtes vienkārši būt klātesoša savā ķermenī.\n"
        "Bez vērtēšanas. Tikai klātbūtne."
    )


# ============================
#        VAKARA CIKLS
# ============================

def evening_text():
    return (
        "🌙 *Vakara noslēgums*\n\n"
        "Tu esi nonākusi līdz dienas beigām.\n"
        "Tev nav jābūt perfektai. Tu drīksti atlaist.\n\n"
        "Pajautā sev: kur manī šobrīd ir visvairāk miera?"
    )

def evening_breath():
    return (
        "🌬 Vakara elpa\n\n"
        "Ieelpa 4… izelpa 8…\n"
        "Ļauj sev noslīdēt mierā, kā vilnim, kas atgriežas jūrā."
    )

def evening_task():
    return (
        "💛 Vakara uzdevums\n\n"
        "Šovakar pamēģini 1 minūti vienkārši sēdēt klusumā.\n"
        "Bez telefona, bez pienākumiem. Tikai tu."
    )


# ============================
#        STARTA KOMANDA
# ============================

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "Sveika, Anda 🌿\n"
        "Šis ir tavs maigais stūrītis.\n"
        "Izvēlies, ko vēlies šobrīd:"
    )

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_morning = types.KeyboardButton("🌅 Rīta cikls")
    btn_evening = types.KeyboardButton("🌙 Vakara cikls")
    btn_task = types.KeyboardButton("💛 Dienas uzdevums")
    btn_breath = types.KeyboardButton("🌬 Elpošanas vingrinājums")

    keyboard.add(btn_morning, btn_evening)
    keyboard.add(btn_task, btn_breath)

    bot.send_message(message.chat.id, text, reply_markup=keyboard)


# ============================
#     SLEPENĀ KOMANDA /anda
# ============================

@bot.message_handler(commands=['anda'])
def secret(message):
    bot.send_message(
        message.chat.id,
        "🌙 Tavs slepenais maigais brīdis.\n\n"
        "Tu esi drošībā. Tu drīksti atlaist visu, kas šobrīd ir par daudz.\n"
        "Ieelpo lēni… un ļauj sev būt tieši tā, kā tu esi.\n\n"
        "Tu esi pietiekama."
    )


# ============================
#     POGU APSTRĀDE
# ============================

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    text = message.text.strip()

    if text == "🌅 Rīta cikls":
        bot.send_message(message.chat.id, morning_text(), parse_mode="Markdown")
        bot.send_message(message.chat.id, morning_breath())
        bot.send_message(message.chat.id, morning_task())

    elif text == "🌙 Vakara cikls":
        bot.send_message(message.chat.id, evening_text(), parse_mode="Markdown")
        bot.send_message(message.chat.id, evening_breath())
        bot.send_message(message.chat.id, evening_task())

    elif text == "💛 Dienas uzdevums":
        bot.send_message(message.chat.id, morning_task())

    elif text == "🌬 Elpošanas vingrinājums":
        bot.send_message(message.chat.id, morning_breath())

    else:
        bot.reply_to(message, "Es tevi dzirdu. 🌿 Var izvēlēties kādu no pogām zemāk.")


# ============================
#       BOTA PALAIŠANA
# ============================

print("Bot is running...")
bot.infinity_polling()



