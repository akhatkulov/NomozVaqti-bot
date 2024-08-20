import telebot
from helper import *
from parts import *
import conf
bot = telebot.TeleBot(conf.BOT_TOKEN) #bot token
admin_id = conf.ADMIN_ID #admin_id


def join(user_id):
    try:
        xx = get_channel()
        r = 0
        for i in xx:
            res = bot.get_chat_member(f"@{i}", user_id)
            x = ['member', 'creator', 'administrator']
            if res.status in x:
                r += 1
        if r != len(xx):
            bot.send_message(user_id,
                             "<b>👋 Assalomu alaykum Botni ishga tushurish uchun kanallarga a'zo bo'ling va a'zolikni tekshirish buyrug'ini bosing.</b>",
                             parse_mode='html', reply_markup=join_key())
            return False
        else:
            return True
    except Exception as e:
        bot.send_message(chat_id=admin_id, text=f"Kanalga bot admin qilinmagan yoki xato: {str(e)}")
        return True
    


@bot.message_handler(chat_types=['private'])
def home(message):
    text = message.text
    chat_id = message.chat.id 

    if text == "/start" and join(chat_id):
        
        create_user(cid=message.chat.id)
        bot.send_message(chat_id=chat_id,text=f"<b>Assalomu alaykum o'zingizga kerakli bo'lgan bo'limni tanlang </b>",parse_mode="HTML",reply_markup=home_key())


    if text == "⏰Nomoz vaqti":
        print(get_location(int(chat_id)))
        print(get_location(int(chat_id))== "0")
        if get_location(int(chat_id)) == "0":
            bot.send_message(chat_id=chat_id,text="Manzilingizni tanlang",reply_markup=location_keys())
        else:
            bot.send_message(chat_id=chat_id,text=f"{pray_time(get_location(int(message.chat.id)))}",parse_mode="HTML")
    
    if text == "✨Ramazon bo'limi":
        bot.send_message(chat_id=chat_id,text="Kerakli menyuni tanlang",reply_markup=menu_ramadan())
    if text == "⚙️Sozlamalar":
        bot.send_message(chat_id=chat_id,text="Manzilingizni tanlang",reply_markup=location_keys())
    if text == "📖Qo'llanma":
        bot.send_message(chat_id=chat_id,text="Ushbu bot orqali osongina ibodat vaqtlaridan xabardor bo'lasiz!")
    if text == "💬Bog'lanish":
        bot.send_message(chat_id=chat_id,text="<b>Admin: @AbuYunus1988 </b> \n<b>Dasturchi: @Akhatkulov </b>",parse_mode="HTML")
    
    if text == "/admin" and chat_id == admin_id:
        bot.send_message(chat_id=admin_id,text='Tanlang',reply_markup=admin_buttons())





@bot.message_handler()
def reg_gr(message):
    if "-100" in str(message.chat.id):
        create_group(cid=message.chat.id)
    if message.text == "/start@PrayingTime_bot":
        bot.send_message(chat_id=message.chat.id,text="Ushbu bot sizni Nomoz vaqlaridan xabardor qiladi. Bot guruhda imkoniyatlari cheklangan. Botdan keng foydalanmoqchi bo'lsangiz botga kirib foydalanishingiz mumkin!")
	

@bot.callback_query_handler(func= lambda callback : callback.data)
def locations(callback):
    chat_id = callback.message.chat.id
    data = callback.data
    if data == "/start":
        bot.send_message(chat_id=chat_id,text=f"<b>Assalomu alaykum o'zingizga kerakli bo'lgan bo'limni tanlang </b>",parse_mode="HTML",reply_markup=home_key())
    if data in all_locations:
        put_location(cid=chat_id,x_location=data)
        bot.send_message()
    if data == "duolar":
        bot.send_message(chat_id=chat_id,text="""<b>✨Ro‘za tutish (saharlik, og‘iz yopish) duosi</b>

نَوَيْتُ أَنْ أَصُومَ صَوْمَ شَهْرَ رَمَضَانَ مِنَ الْفَجْرِ إِلَى الْمَغْرِبِ، خَالِصًا لِلهِ تَعَالَى أَللهُ أَكْبَرُ

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir. 

<b>✨Iftorlik (og‘iz ochish) duosi </b>

اَللَّهُمَّ لَكَ صُمْتُ وَ بِكَ آمَنْتُ وَ عَلَيْكَ تَوَكَّلْتُ وَ عَلَى رِزْقِكَ أَفْتَرْتُ، فَغْفِرْلِى مَا قَدَّمْتُ وَ مَا أَخَّرْتُ بِرَحْمَتِكَ يَا أَرْحَمَ الرَّاحِمِينَ

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.""",parse_mode="html")
    if data == "vaqtlar":
        bot.send_photo(chat_id=chat_id,photo=conf.TIME_PHOTO_URL,caption="""<b>✨Ushbu vaqt Toshkent vaqtida ko'rsatilgan.</b>

Toshkentdan boshqa shaharlardagi vaqtlar farqi (minut)

Avval: Chimkent (1), Konibodom (5), Qo‘qon (7), Jambul (7), Namangan (10), Farg‘ona (10), Marg‘ilon (10), Andijon (12), O‘sh (14), Jalolobod (15), Bishkek (21), Olma - ota (21)

Keyin: Bekobod (4), Turkiston (4), Jizzax (6), Guliston (7). Denov (7), Jonboy (7), Samarqand (9), Shahrisabz (10), Kattaqo‘rg‘on (12), Qarshi (9), Nurota (14), Navoiy (19), Buxoro (21), Xiva (35)""",parse_mode="html")
print(bot.get_me())
bot.polling()
