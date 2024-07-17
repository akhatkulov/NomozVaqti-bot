import telebot
from helper import *
from parts import *

bot = telebot.TeleBot("7059689609:AAEsegMf79BvadYNnnEmv0aoHpZrAPQMa3I") #bot token
admin_id = 6521895096 #admin_id


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
    


def join_key():
  keyboard = types.InlineKeyboardMarkup(row_width=1)
  keyboard.add(
      types.InlineKeyboardButton('1️⃣ - kanal', url=str(get_kanal_1())),
      types.InlineKeyboardButton('2️⃣ - kanal', url=str(get_kanal_2())),
      types.InlineKeyboardButton('✅ Tasdiqlash', callback_data="member")
  )
  return keyboard


@bot.message_handler(chat_types=['private'])
def home(message):
    text = message.text
    chat_id = message.chat.id 

    if text == "/start" and join(chat_id):
        
        create_user(cid=message.chat.id)
        bot.send_message(chat_id=chat_id,text=f"<b>Assalomu alaykum o'zingizga kerakli bo'lgan bo'limni tanlang </b>",parse_mode="HTML",reply_markup=home_key())


    if text == "⏰Nomoz vaqti":
        if get_location(int(chat_id)) == "0":
            bot.send_message(chat_id=chat_id,text="Manzilingizni sozlash. U uchun /set_location deb yozing")
        else:
            bot.send_message(chat_id=chat_id,text=f"{pray_time(db.get_location(int(message.chat.id)))}",parse_mode="HTML")
    if text == "/set_location":
        bot.send_message(chat_id=chat_id,text="Manzilingizni tanlang",reply_markup=location_keys())
    if text == "📖Qo'llanma":
        bot.send_message(chat_id=chat_id,text="sss")
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

print(bot.get_me())
bot.polling()
