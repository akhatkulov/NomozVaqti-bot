import telebot
from helper import *
from parts import *
import requests
from bs4 import BeautifulSoup
from mailer import *

bot = telebot.TeleBot("6709370621:AAGs70M4tdROjUD6o3PbSbA54rg_u8O3YVU")
admin_id = 789945598
db = Database(path_to_db="data/main.db")
db_gr = Database_gr(path_to_db="data/group.db")

try:
    db.create_table_users()
except:
    print("--{xato sql create}--")
try:
    db.create_table_users()
except:
    print("--xato gruppa--")

def join_key():
  keyboard = types.InlineKeyboardMarkup(row_width=1)
  keyboard.add(
      types.InlineKeyboardButton('1️⃣ - kanal', url=str(get_kanal_1())),
      types.InlineKeyboardButton('2️⃣ - kanal', url=str(get_kanal_2())),
      types.InlineKeyboardButton('✅ Tasdiqlash', callback_data="member")
  )
  return keyboard


@bot.message_handler(chat_types=['group'])
def reg_gr(message):
    print(17)
    if message.text == "/start@PrayingTime_bot":
        db_gr.add_user(chat_id)
        bot.send_message(chat_id=message.chat.id,text="Ushbu bot sizni Nomoz vaqlaridan xabardor qiladi. Bot guruhda imkoniyatlari cheklangan. Botdan keng foydalanmoqchi bo'lsangiz botga kirib foydalanishingiz mumkin!")
	
@bot.message_handler(chat_types=['private'])
def home(message):
    text = message.text
    chat_id = message.chat.id 

    if text == "/start" and join(chat_id):
        
        db.add_user(int(message.chat.id))
        bot.send_message(chat_id=chat_id,text=f"<b>Assalomu alaykum o'zingizga kerakli bo'lgan bo'limni tanlang </b>",parse_mode="HTML",reply_markup=home_key())


    if text == "⏰Nomoz vaqti":
        if db.get_location(int(chat_id)) == "home":
            bot.send_message(chat_id=chat_id,text="Manzilingizni sozlash. U uchun /set_location deb yozing")
        else:
            bot.send_message(chat_id=chat_id,text=f"{pray_time(db.get_location(int(message.chat.id)))}",parse_mode="HTML")
    if text == "/set_location":
        bot.send_message(chat_id=chat_id,text="Manzilingizni tanlang",reply_markup=location_keys())
    if text == "📖Qo'llanma":
        bot.send_message(chat_id=chat_id,text="sss")
    if text == "💬Bog'lanish":
        bot.send_message(chat_id=chat_id,text="<b>Admin: @ADmin </b> \n<b>Dasturchi: @Akhatkulov </b>",parse_mode="HTML")
    

    if text=="Stat" or  text == "/stat" and chat_id == admin_id:
        try:
            bot.send_message(chat_id=admin_id,text=f"Guruhlar:  {db_gr.gr_info()} Odamlar: {db.member_info()}")
        except:
            bot.send_message(chat_id=admin_id,text="Malumotlar yetarli emas")
    if text == "/admin" and chat_id == admin_id:
        bot.send_message(chat_id=admin_id,text='tanlang',reply_markup=admin_keys())

    
    if message.text == "Send User" and message.chat.id == admin_id:
        adver = bot.send_message(chat_id=admin_id,text="Send User | <b>✍️ Xabar matnini kiritng !</b>",reply_markup=abort_button(),parse_mode="HTML")
        bot.register_next_step_handler(adver, ads_send_user)
    if message.text == "Send Group" and message.chat.id == admin_id:
        adver = bot.send_message(chat_id=admin_id,text="Send User | <b>✍️ Xabar matnini kiritng !</b>",reply_markup=abort_button(),parse_mode="HTML")
        bot.register_next_step_handler(adver, ads_send_group)

    
    if message.text == "Forward User" and message.chat.id == admin_id:
        adver = bot.send_message(chat_id=admin_id,text="user |<b>✍️ Xabar matnini kiritng !</b>",reply_markup=abort_button(),parse_mode="HTML")
        bot.register_next_step_handler(adver, for_send_user)
    if message.text == "Forward Group" and message.chat.id == admin_id:
        adver = bot.send_message(chat_id=admin_id,text="Group |<b>✍️ Xabar matnini kiritng !</b>",reply_markup=abort_button(),parse_mode="HTML")
        bot.register_next_step_handler(adver, for_send_group)
    if message.text == "/set_kanal_1" and message.chat.id == admin_id:
        x = bot.send_message(chat_id=admin_id,text="Kanal linkini yuboring",parse_mode="HTML")
        bot.register_next_step_handler(x,change_kanal_1)
    if message.text == "/set_kanal_2" and message.chat.id == admin_id:
        x = bot.send_message(chat_id=admin_id,text="Kanali linkini yuboring",parse_mode="HTML")
        bot.register_next_step_handler(x,change_kanal_2)
    if message.text == "/set_main" and message.chat.id == admin_id:
        x = bot.send_message(chat_id=admin_id,text="Kanal kalit kiriting",parse_mode='HTML')
        bot.register_next_step_handler(x,change_main) 
def change_kanal_1(msg):
    set_kanal_1(msg.text)
    bot.send_message(chat_id=msg.chat.id,text="Sozlandi")
def change_kanal_2(msg):
    set_kanal_2(msg.text)
    bot.send_message(chat_id=msg.chat.id,text="Sozlandi")

def change_main(msg):
    set_main(msg.text)
    bot.send_message(chat_id=msg.chat.id,text="Sozlandi")


def join(user_id):
    x = get_main()
    member = bot.get_chat_member(x, user_id)
    member1 = bot.get_chat_member(x, user_id)
    # except:
    #     bot.send_message(chat_id=user_id,text="<b>👋 Assalomu alaykum Botni ishga tushurish uchun kanallarga a'zo bo'ling va a'zolikni tekshirish buyrug'ini bosing.</b>",parse_mode='html',reply_markup=join_key())

    x = ['member', 'creator', 'administrator']
    if member.status not in x or member1.status not in x:
        bot.send_message(chat_id=user_id,text="<b>👋 Assalomu alaykum Botni ishga tushurish uchun kanallarga a'zo bo'ling va a'zolikni tekshirish buyrug'ini bosing.</b>",parse_mode='html',reply_markup=join_key())
        return False
    else:
        return True




@bot.callback_query_handler(func= lambda callback : callback.data)
def locations(callback):
    chat_id = callback.message.chat.id
    data = callback.data
    if data == "member":
        bot.send_message(chat_id=chat_id,text=f"<b>Assalomu alaykum o'zingizga kerakli bo'lgan bo'limni tanlang </b>",parse_mode="HTML",reply_markup=home_key())
    if data == "andijon":
        db.add_location(int(chat_id),"andijon")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Andijon sifatida sozlandi✅")
    if data == "angren":
        db.add_location(int(chat_id),"angren")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Angren sifatida sozlandi✅")
    if data == "bekobod":
        db.add_location(int(chat_id),"bekobod")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Bekobod sifatida sozlandi✅")
    if data == "boysun":
        db.add_location(int(chat_id),"boysun")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Boysun sifatida sozlandi✅")
    if data == "buxoro":
        db.add_location(int(chat_id),"buxoro")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Buxoro sifatida sozlandi✅")
    if data == "gazli":
        db.add_location(int(chat_id),"gazli")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Gazli sifatida sozlandi✅")
    if data == "guliston":
        db.add_location(int(chat_id),"guliston")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Guliston sifatida sozlandi✅")
    if data == "denov":
        db.add_location(int(chat_id),"denov")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Denov sifatida sozlandi✅")
    if data == "dehqonobod":
        db.add_location(int(chat_id),"dehqonobod")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Dehqonobod sifatida sozlandi✅")
    if data == "dostlik":
        db.add_location(int(chat_id),"dostlik")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Do'stlik sifatida sozlandi✅")
    if data == "jizzax":
        db.add_location(int(chat_id),"jizzax")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Jizzax sifatida sozlandi✅")
    if data == "zarafshon":
        db.add_location(int(chat_id),"zarafshon")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Zarafshon sifatida sozlandi✅")
    if data == "zomin":
        db.add_location(int(chat_id),"zomin")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Zomin sifatida sozlandi✅")
    if data == "kattaqurgon":
        db.add_location(int(chat_id),"kattaqurgon")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Katta Qo'rg'on sifatida sozlandi✅")
    if data == "konimex":
        db.add_location(int(chat_id),"konimex")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Konimex sifatida sozlandi✅")
    if data == "margilon":
        db.add_location(int(chat_id),"margilon")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Marg'ilon sifatida sozlandi✅")
    if data == "mingbuloq":
        db.add_location(int(chat_id),"mingbuloq")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Mingbuloq sifatida sozlandi✅")
    if data == "muborak":
        db.add_location(int(chat_id),"muborak")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Muborak sifatida sozlandi✅")
    if data == "moynoq":
        db.add_location(int(chat_id),"moynoq")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Mo'ynoq sifatida sozlandi✅")
    if data == "navoiy":
        db.add_location(int(chat_id),"navoiy")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Navoiy sifatida sozlandi✅")
    if data == "namangan":
        db.add_location(int(chat_id),"namangan")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Namangan sifatida sozlandi✅")
    if data == "nukus":
        db.add_location(int(chat_id),"nukus")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Nukus sifatida sozlandi✅")
    if data == "nurota":
        db.add_location(int(chat_id),"nurota")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Nur Ota sifatida sozlandi✅")
    if data == "oltiariq":
        db.add_location(int(chat_id),"oltiariq")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Olti Ariq sifatida sozlandi✅")
    if data == "paxtaobod":
        db.add_location(int(chat_id),"paxtaobod")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Paxta Obod sifatida sozlandi✅")
    if data == "rishton":
        db.add_location(int(chat_id),"rishton")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Rishton sifatida sozlandi✅")
    if data == "samarqand":
        db.add_location(int(chat_id),"samarqand")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Samarqand sifatida sozlandi✅")
    if data == "termiz":
        db.add_location(int(chat_id),"termiz")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Termiz sifatida sozlandi✅")
    if data == "toshkent":
        db.add_location(int(chat_id),"toshkent")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Toshkent sifatida sozlandi✅")
    if data == "tortkol":
        db.add_location(int(chat_id),"tortkol")
        bot.send_message(chat_id=chat_id,text="Manzilingiz To'rt Ko'l sifatida sozlandi✅")
    if data == "urganch":
        db.add_location(int(chat_id),"urganch")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Urganch sifatida sozlandi✅")
    if data == "urgut":
        db.add_location(int(chat_id),"urgut")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Urgut sifatida sozlandi✅")
    if data == "uchquduq":
        db.add_location(int(chat_id),"uchquduq")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Uchquduq sifatida sozlandi✅")
    if data == "uchqorgon":
        db.add_location(int(chat_id),"uchqorgon")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Uch Qo'rg'on sifatida sozlandi✅")
    if data == "fargona":
        db.add_location(int(chat_id),"fargona")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Farg'ona sifatida sozlandi✅")
    if data == "xiva":
        db.add_location(int(chat_id),"xiva")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Xiva sifatida sozlandi✅")
    if data == "xonobod":
        db.add_location(int(chat_id),"xonobod")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Xonobod sifatida sozlandi✅")
    if data == "xonqa":
        db.add_location(int(chat_id),"xonqa")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Xonqa sifatida sozlandi✅")
    if data == "xojaobod":
        db.add_location(int(chat_id),"xojaobod")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Xo'ja Obod sifatida sozlandi✅")
    if data == "chortoq":
        db.add_location(int(chat_id),"chortoq")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Chortoq sifatida sozlandi✅")
    if data == "chust":
        db.add_location(int(chat_id),"chust")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Chust sifatida sozlandi✅")
    if data == "shahrixon":
        db.add_location(int(chat_id),"shahrixon")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Shaxrihon sifatida sozlandi✅")
    if data == "sherobod":
        db.add_location(int(chat_id),"sherobod")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Sherobod sifatida sozlandi✅")
    if data == "shovat":
        db.add_location(int(chat_id),"shovat")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Shovat sifatida sozlandi✅")
    if data == "yangibozor":
        db.add_location(int(chat_id),"yangibozor")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Yangi Bozor sifatida sozlandi✅")
    if data == "gallaorol":
        db.add_location(int(chat_id),"gallaorol")
        bot.send_message(chat_id=chat_id,text="Manzilingiz G'alla Orol sifatida sozlandi✅")
    if data == "qarshi":
        db.add_location(int(chat_id),"qarshi")
        bot.send_message(chat_id=chat_id,text="Manzilingiz qarshi sifatida sozlandi✅")
    if data == "qorakol":
        db.add_location(int(chat_id),"qorakol")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Qorakol sifatida sozlandi✅")
    if data == "quva":
        db.add_location(int(chat_id),"quva")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Quva sifatida sozlandi✅")
    if data == "qongirot":
        db.add_location(int(chat_id),"qongirot")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Qo'ngirot sifatida sozlandi✅")
    if data == "qoqon":
        db.add_location(int(chat_id),"qoqon")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Qo'qon sifatida sozlandi✅")


print(bot.get_me())
bot.polling()
