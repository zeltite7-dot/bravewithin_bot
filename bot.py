import os
import telebot
from telebot import types
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
rituali = {
    1: {
        "rits": """🌅 *1. dienas rīts*

*Sveiciens*
Labrīt. Šis ir tavs maigais sākums. Ieelpo lēni… ļauj pleciem noslīdēt. Šis brīdis ir tikai tev.

*Maigs teksts*
Šodien nav jāsteidzas. Tu vari ienākt dienā kā silta gaisma, kas lēnām piepilda telpu. Tu vari atļaut sev būt lēnai, maigai, klātesošai.

*Nodoms*
Es izvēlos būt klātesoša sev un savam ķermenim.

*Sajūtu pārbaude*
Kā jūtas mani pleci? Mana sirds? Mana elpa?

*Elpošana*
Veic 10 dziļas, ritmiskas ieelpas un izelpas.
Ieelpo caur degunu, ļaujot vēderam pacelties.
Izelpo caur muti, ļaujot ķermenim kļūt mīkstam.
Pēc 10 elpām izdari dziļu ieelpu un lēnu izelpu.
Pēc izelpas apstājies uz 5–10 sekundēm.
Tad ieelpo dziļi un aizturi elpu 5 sekundes.
Atlaid. Ienāc savā dienā ar vieglumu.

*Dienas uzdevums*
2 minūtes vienkārši jūti savu ķermeni.
""",

        "vakars": """🌙 *1. dienas vakars*

*Sveiciens*
Labvakar. Tu esi nonākusi līdz dienas noslēgumam.

*Maigs teksts*
Tu esi darījusi pietiekami. Tu esi bijusi pietiekama. Šovakar tu vari nolikt malā pienākumus un atļaut sev būt cilvēkam, kurš ir pelnījis mieru.

*Pateicība*
Paldies manai dienai. Paldies manam ķermenim. Paldies manai elpai.

*Sajūtu noslēgums*
Kur manī šobrīd ir visvairāk miera?

*Elpošana*
Veic 15 lēnas, dziļas elpas.
Ieelpo caur degunu, piepildot vēderu un krūtis.
Izelpo caur muti, atbrīvojot dienas smagumu.
Pēc pēdējās izelpas apstājies uz 5–8 sekundēm.
Tad ieelpo dziļi un aizturi elpu 3–5 sekundes.
Izelpo lēni kā vilnis, kas atgriežas jūrā.

*Vakara uzdevums*
1 minūti sēdi klusumā.
"""
    },

    2: {
        "rits": """🌅 *2. dienas rīts*

*Sveiciens*
Labrīt. Šodien tu vari sākt ar maigumu pret sevi.

*Maigs teksts*
Tu neesi spiesta steigties. Tu vari ienākt dienā ar vieglumu un klātbūtni.

*Nodoms*
Es izvēlos vieglumu.

*Sajūtu pārbaude*
Kā jūtas mana mugura? Vai es turu spriedzi?

*Elpošana*
Veic 12 dziļas ieelpas un izelpas.
Ieelpo caur degunu, vēders paceļas.
Izelpo caur muti, ķermenis mīkstinās.
Pēc 12 elpām dziļa ieelpa, lēna izelpa.
Pēc izelpas pauze 8–12 sekundes.
Tad dziļa ieelpa un aizture 5–7 sekundes.

*Dienas uzdevums*
Šodien pajautā sev: “Ko es šobrīd jūtu?”
""",

        "vakars": """🌙 *2. dienas vakars*

*Sveiciens*
Labvakar. Tu esi paveikusi pietiekami.

*Maigs teksts*
Šovakar tu vari atlaist visu, kas vairs nav jānes.

*Pateicība*
Paldies manai elpai par klātbūtni.

*Sajūtu noslēgums*
Kā jūtas manas kājas?

*Elpošana*
Veic 15 lēnas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc pēdējās izelpas pauze 6–10 sekundes.
Tad dziļa ieelpa un aizture 4–6 sekundes.

*Vakara uzdevums*
Pasaki sev vienu maigu frāzi.
"""
    },

    3: {
        "rits": """🌅 *3. dienas rīts*

*Sveiciens*
Labrīt. Tu vari ienākt šajā dienā lēni.

*Maigs teksts*
Šodien tu drīksti izvēlēties mieru.

*Nodoms*
Es izvēlos iekšējo telpu.

*Sajūtu pārbaude*
Kā jūtas mans vēders?

*Elpošana*
Veic 15 dziļas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc 15 elpām dziļa ieelpa, lēna izelpa.
Pēc izelpas pauze 10–15 sekundes.
Tad dziļa ieelpa un aizture 6–8 sekundes.

*Dienas uzdevums*
30 sekundes klausies savu elpu.
""",

        "vakars": """🌙 *3. dienas vakars*

*Sveiciens*
Labvakar. Tu vari ienākt mierā.

*Maigs teksts*
Šis ir tavs drošais vakara stūrītis.

*Pateicība*
Paldies manai sirdij par izturību.

*Sajūtu noslēgums*
Kā jūtas mana krūtis?

*Elpošana*
Veic 20 lēnas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc pēdējās izelpas pauze 8–12 sekundes.
Tad dziļa ieelpa un aizture 5–7 sekundes.

*Vakara uzdevums*
Atlaid plecus.
"""
    },
}
    4: {
        "rits": """🌅 *4. dienas rīts*

*Sveiciens*
Labrīt. Šodien tu vari sākt ar maigumu un klusu pateicību.

*Maigs teksts*
Tu neesi viena. Tu esi daļa no pasaules, kas mostas kopā ar tevi. Tu vari ienākt dienā ar siltumu, ar klusu iekšēju mieru, ar sajūtu, ka tev nav jāsteidzas.

*Nodoms*
Es izvēlos siltumu un klātbūtni.

*Sajūtu pārbaude*
Kā jūtas manas rokas? Vai tās ir saspringtas? Kā jūtas mana kakla aizmugure?

*Elpošana*
Veic 15 dziļas, ritmiskas ieelpas un izelpas.
Ieelpo caur degunu, ļaujot vēderam pacelties.
Izelpo caur muti, ļaujot ķermenim kļūt mīkstam.
Pēc 15 elpām dziļa ieelpa, lēna izelpa.
Pēc izelpas pauze 10–15 sekundes.
Tad dziļa ieelpa un aizture 6–8 sekundes.

*Dienas uzdevums*
1 minūti jūti savas rokas — to siltumu, smagumu, klātbūtni.
""",

        "vakars": """🌙 *4. dienas vakars*

*Sveiciens*
Labvakar. Dienas ritējums ir noslēdzies.

*Maigs teksts*
Tu vari atlaist visu, kas šodien bija smags. Tu vari atļaut sev nosēsties kā smiltīm, kas lēnām ieguļas vietā.

*Pateicība*
Paldies manam ķermenim par spēku. Paldies manai elpai par klātbūtni.

*Sajūtu noslēgums*
Kā jūtas mana mugura? Vai tā vēlas atbalstu?

*Elpošana*
Veic 20 lēnas, dziļas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc pēdējās izelpas pauze 8–12 sekundes.
Tad dziļa ieelpa un aizture 5–7 sekundes.

*Vakara uzdevums*
Atbalsti muguru pret sienu vai spilvenu un jūti, kā tā atslābst.
"""
    },

    5: {
        "rits": """🌅 *5. dienas rīts*

*Sveiciens*
Labrīt. Šodien tu vari ienākt dienā kā maigā vēja brāzma.

*Maigs teksts*
Tu vari atļaut sev būt vieglai. Tu vari atļaut sev būt cilvēkam, kurš jūt un elpo.

*Nodoms*
Es izvēlos vieglumu savā ķermenī.

*Sajūtu pārbaude*
Kā jūtas mana seja? Vai žoklis ir sasprindzis?

*Elpošana*
Veic 12 dziļas ieelpas un izelpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc 12 elpām dziļa ieelpa, lēna izelpa.
Pēc izelpas pauze 8–12 sekundes.
Tad dziļa ieelpa un aizture 5–7 sekundes.

*Dienas uzdevums*
10 sekundes atslābini žokli.
""",

        "vakars": """🌙 *5. dienas vakars*

*Sveiciens*
Labvakar. Tu esi paveikusi pietiekami.

*Maigs teksts*
Šovakar tu vari atlaist visas domas, kas tev vairs nekalpo.

*Pateicība*
Paldies manam prātam par centību.

*Sajūtu noslēgums*
Kā jūtas mana galva? Vai tā ir smaga?

*Elpošana*
Veic 20 lēnas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc pēdējās izelpas pauze 8–12 sekundes.
Tad dziļa ieelpa un aizture 5–7 sekundes.

*Vakara uzdevums*
Jūti, kā galva atbalstās uz spilvena.
"""
    },

    6: {
        "rits": """🌅 *6. dienas rīts*

*Sveiciens*
Labrīt. Šis rīts ir kā klusa telpa, kurā tu vari ienākt ar maigumu.

*Maigs teksts*
Tu neesi spiesta būt ātra. Tu vari ienākt dienā kā cilvēks, kurš jūt un elpo.

*Nodoms*
Es izvēlos būt klātesoša savā ķermenī.

*Sajūtu pārbaude*
Kā jūtas mani pleci? Kā jūtas mana kakla priekšpuse?

*Elpošana*
Veic 15 dziļas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc 15 elpām dziļa ieelpa, lēna izelpa.
Pēc izelpas pauze 10–15 sekundes.
Tad dziļa ieelpa un aizture 6–8 sekundes.

*Dienas uzdevums*
1 minūti jūti savu kaklu — tā maigumu, tā atbalstu.
""",

        "vakars": """🌙 *6. dienas vakars*

*Sveiciens*
Labvakar. Tu esi paveikusi pietiekami.

*Maigs teksts*
Tu vari atļaut sev nosēsties kā ūdenim, kas kļūst mierīgs.

*Pateicība*
Paldies manam ķermenim par izturību.

*Sajūtu noslēgums*
Kā jūtas mana kakla aizmugure?

*Elpošana*
Veic 20 lēnas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc pēdējās izelpas pauze 8–12 sekundes.
Tad dziļa ieelpa un aizture 5–7 sekundes.

*Vakara uzdevums*
30 sekundes jūti kakla aizmuguri un ļauj tai atslābt.
"""
    },
    7: {
        "rits": """🌅 *7. dienas rīts*

*Sveiciens*
Labrīt. Šis rīts ir kā jauns sākums. Ieelpo… ļauj sev ienākt dienā ar maigumu.

*Maigs teksts*
Tu vari atļaut sev ienākt dienā kā cilvēkam, kurš jūt. Tu vari atļaut sev būt lēnai, klātesošai, maigai.

*Nodoms*
Es izvēlos mieru savā prātā.

*Sajūtu pārbaude*
Kā jūtas mana galva? Vai tā ir smaga?

*Elpošana*
Veic 20 dziļas, ritmiskas ieelpas un izelpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc 20 elpām dziļa ieelpa, lēna izelpa.
Pēc izelpas pauze 10–15 sekundes.
Tad dziļa ieelpa un aizture 6–8 sekundes.

*Dienas uzdevums*
30 sekundes jūti savu galvu — tās smagumu, tās klātbūtni.
""",

        "vakars": """🌙 *7. dienas vakars*

*Sveiciens*
Labvakar. Tu vari atļaut sev noslēgt šo dienu ar mieru.

*Maigs teksts*
Tu vari atlaist visas domas, kas tev vairs nekalpo. Tu vari atļaut sev būt cilvēkam, kurš ir pelnījis atpūtu.

*Pateicība*
Paldies manam prātam par centību.

*Sajūtu noslēgums*
Kā jūtas mana piere? Vai tā ir saspringta?

*Elpošana*
Veic 20 lēnas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc pēdējās izelpas pauze 8–12 sekundes.
Tad dziļa ieelpa un aizture 5–7 sekundes.

*Vakara uzdevums*
30 sekundes jūti savu pieri un ļauj tai atslābt.
"""
    },

    8: {
        "rits": """🌅 *8. dienas rīts*

*Sveiciens*
Labrīt. Šis rīts ir kā klusa telpa, kurā tu vari ienākt ar maigumu.

*Maigs teksts*
Tu vari atļaut sev būt lēnai. Tu vari atļaut sev būt klātesošai.

*Nodoms*
Es izvēlos būt klātesoša savā elpā.

*Sajūtu pārbaude*
Kā jūtas mana krūtis? Vai tā ir saspringta?

*Elpošana*
Veic 20 dziļas, ritmiskas ieelpas un izelpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc 20 elpām dziļa ieelpa, lēna izelpa.
Pēc izelpas pauze 10–15 sekundes.
Tad dziļa ieelpa un aizture 6–8 sekundes.

*Dienas uzdevums*
1 minūti jūti savu krūtis — tās kustību, tās siltumu.
""",

        "vakars": """🌙 *8. dienas vakars*

*Sveiciens*
Labvakar. Tu vari atļaut sev noslēgt šo dienu ar mieru.

*Maigs teksts*
Tu vari atlaist visas domas, kas tev vairs nekalpo.

*Pateicība*
Paldies manai krūtīm par elpu.

*Sajūtu noslēgums*
Kā jūtas mana krūtis? Vai tā ir saspringta?

*Elpošana*
Veic 20 lēnas elpas.
Ieelpa caur degunu, izelpa caur muti.
Pēc pēdējās izelpas pauze 8–12 sekundes.
Tad dziļa ieelpa un aizture 5–7 sekundes.

*Vakara uzdevums*
30 sekundes jūti savu krūtis un ļauj tai atslābt.
"""
    },

# ============================
#   RITUĀLI (šeit ieliec visu savu rituali = {...})
# ============================

rituali = {
    # <-- ŠEIT IELIEC VISAS 1.–10. DIENAS, KO MĒS UZRAKSTĪJĀM -->
}

# ============================
#   DIENAS NOTEIKŠANA
# ============================

def get_day():
    day = datetime.now().day % 10
    return 10 if day == 0 else day

# ============================
#   INLINE POGAS
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
        types.InlineKeyboardButton("✨ Maigs teikums", callback_data="teikums")
    )
    return keyboard

# ============================
#   STARTA KOMANDA
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
        text = rituali[day]["rits"].split("*Nodoms*")[1].split("*")[0].strip()
        bot.send_message(call.message.chat.id, f"💛 *Šodienas nodoms:*\n{text}", parse_mode="Markdown")

    elif call.data == "elpa":
        text = rituali[day]["rits"].split("*Elpošana*")[1].split("*")[0].strip()
        bot.send_message(call.message.chat.id, f"🌬 *Elpošanas vingrinājums:*\n{text}", parse_mode="Markdown")

    elif call.data == "teikums":
        bot.send_message(call.message.chat.id, "✨ Šis ir tavs maigais brīdis.")

# ============================
#   AUTOMĀTISKĀ SŪTĪŠANA
# ============================

CHAT_ID = 941689479   # <-- Tavs chat ID

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

    



