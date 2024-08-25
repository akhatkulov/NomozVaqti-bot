import telebot
from helper import *
from parts import *
from data.sqlalchemy import *
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
################ for users ##################################
    if text == "/start" and join(chat_id):
        
        create_user(cid=message.chat.id)
        bot.send_message(chat_id=chat_id,text=f"<b>Assalomu alaykum o'zingizga kerakli bo'lgan bo'limni tanlang </b>",parse_mode="HTML",reply_markup=home_key())


    if text == "⏰Nomoz vaqti" and join(chat_id):
        users_location = get_location(int(chat_id))
        if users_location == "0":
            bot.send_message(chat_id=chat_id,text="Manzilingizni tanlang",reply_markup=location_keys())
        else:
            result = pray_time(users_location)
            if "N/A" in result:
                bot.send_message(chat_id=chat_id,text="<b> Xatolik! Iltimos adminlarga xabar qiling!\n\nTexnik: @Akhatkulov </b>",parse_mode="html")
            else:
                bot.send_message(chat_id=chat_id, text=result, parse_mode="HTML")

    
    if text == "✨Ramazon bo'limi" and join(chat_id):
        bot.send_message(chat_id=chat_id,text="Kerakli menyuni tanlang",reply_markup=menu_ramadan())
    if text == "⚙️Sozlamalar" and join(chat_id):
        bot.send_message(chat_id=chat_id,text="Manzilingizni tanlang",reply_markup=location_keys())
    if text == "📖Qo'llanma" and join(chat_id):
        bot.send_message(chat_id=chat_id,text="Ushbu bot orqali osongina ibodat vaqtlaridan xabardor bo'lasiz!")
    if text == "💬Bog'lanish" and join(chat_id):
        bot.send_message(chat_id=chat_id,text="<b>Admin: @AbuYunus1988 </b> \n<b>Dasturchi: @Akhatkulov </b>",parse_mode="HTML")
    

#################### admin panel ##########################################
    if message.text == "/admin" and message.chat.id == admin_id:
        bot.send_message(chat_id=admin_id, text="Salom, Admin", reply_markup=admin_buttons())
        put_step(cid=message.chat.id, step="!!!")

    if get_step(message.chat.id) == "channel_del" and message.text != "/start" and message.text != "/admin":
        x = int(message.text)
        if delete_channel(ch_id=x):
            bot.send_message(chat_id=message.chat.id, text="Kanal olib tashlandi")
            put_step(cid=message.chat.id, step="!!!")
        else:
            bot.send_message(chat_id=message.chat.id, text="Xatolik! IDni to'g'ri kiritdingizmi tekshiring!")

    if get_step(message.chat.id) == "add_channel" and message.text != "/start" and message.text != "/admin":
        if put_channel(message.text):
            bot.send_message(chat_id=message.chat.id, text=f"{message.text} kanali qabul qilindi!")
            put_step(cid=int(admin_id), step="!!!")
        else:
            bot.send_message(chat_id=message.chat.id,
                             text="Xatolik! Bu kanal oldin qo'shilgan bo'lishi mumkin yoki boshqa xatolik, iltimos tekshiring")
            put_step(cid=int(admin_id), step="!!!")
    
    if get_step(message.chat.id) == 'send':
        text = message.text
        mid = message.id
        bot.send_message(chat_id=message.chat.id, text="Xabar yuborish boshlandi")
        try:
            for i in get_all_user():
                try:
                    bot.forward_message(chat_id=i, from_chat_id=admin_id, message_id=mid)
                except Exception as e:
                    print(f"Error sending message to user {i}: {str(e)}")
            bot.send_message(chat_id=message.chat.id, text="Tarqatish yakunlandi")
            put_step(cid=int(admin_id), step="!!!")
        except Exception as e:
            bot.send_message(chat_id=message.chat.id, text=f"Xabar yuborishda muammo bo'ldi: {str(e)}")





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
        print(data)
        user_location = all_locations[data]
        put_location(cid=chat_id,x_location=user_location)
        result = pray_time(get_location(int(callback.message.chat.id)))
        if "N/A" in result:
            bot.send_message(chat_id=chat_id,text="<b> Xatolik! Iltimos adminlarga xabar qiling!\n\nTexnik: @Akhatkulov </b>",parse_mode="html")
        else:
            bot.send_message(chat_id=chat_id, text=result, parse_mode="HTML")

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

<b>Toshkentdan boshqa shaharlardagi vaqtlar farqi (minut) </b>

<b>Avval:</b> Chimkent (1), Konibodom (5), Qo‘qon (7), Jambul (7), Namangan (10), Farg‘ona (10), Marg‘ilon (10), Andijon (12), O‘sh (14), Jalolobod (15), Bishkek (21), Olma - ota (21)

<b>Keyin:</b> Bekobod (4), Turkiston (4), Jizzax (6), Guliston (7). Denov (7), Jonboy (7), Samarqand (9), Shahrisabz (10), Kattaqo‘rg‘on (12), Qarshi (9), Nurota (14), Navoiy (19), Buxoro (21), Xiva (35)""",parse_mode="html")
    call = callback
    if call.data == "stat" and str(call.message.chat.id) == str(admin_id):
        bot.send_message(chat_id=call.message.chat.id, text=f"Foydalanuvchilar soni: {user_count()}")
    if call.data == "send" and str(call.message.chat.id) == str(admin_id):
        put_step(cid=call.message.chat.id, step="send")
        bot.send_message(chat_id=call.message.chat.id, text="Forward xabaringizni yuboring")
    if call.data == "channels" and str(call.message.chat.id) == str(admin_id):
        r = get_channel_with_id()
        bot.send_message(chat_id=call.message.chat.id, text=f"Kanallar ro'yxati:{r}", reply_markup=channel_control())
    if call.data == "channel_add" and str(call.message.chat.id) == str(admin_id):
        put_step(cid=call.message.chat.id, step="add_channel")
        bot.send_message(chat_id=call.message.chat.id, text="Kanali linkini yuboring! bekor qilish uchun /start !")
    if call.data == "channel_del" and str(call.message.chat.id) == str(admin_id):
        put_step(cid=call.message.chat.id, step="channel_del")
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"{get_channel_with_id()}\n⚠️O'chirmoqchi bo'lgan kanalingiz IDsini bering, bekor qilish uchun /start yoki /admin deng!")

print(bot.get_me())
bot.polling()
