import telebot
from helper import *
from parts import *

bot = telebot.TeleBot("6709370621:AAGs70M4tdROjUD6o3PbSbA54rg_u8O3YVU")
admin_id = 6778990003824873

@bot.message_handler(chat_types=['private'])
def home(message):
    text = message.text
    chat_id = message.chat.id 
    if text == "/start":
        add_user(chat_id)
        bot.send_message(chat_id=chat_id,text="<b>Assalomu alaykum o'zingizga kerakli bo'lgan bo'limni tanlang </b>",parse_mode="HTML",reply_markup=home_key())


    if text == "⏰Nomoz vaqti":
        if get_location(chat_id) == "home":
            bot.send_message(chat_id=chat_id,text="Manzilingizni sozlash. U uchun /set_location deb yozing")
        else:
            bot.send_message(chat_id=chat_id,text=f"{pray_time(get_location())}")
    if text == "/set_loaction":
        bot.send_message(chat_id=chat_id,text="Manzilingizni tanlang",reply_markup=location_keys())
    if text == "📖Qo'llanma":
        bot.send_message(chat_id=chat_id,text="sss")
    if text == "💬Bog'lanish":
        bot.send_message(chat_id=chat_id,text="<b>Admin: @ADmin </b> \n<b>Dasturchi: @Akhatkulov </b>",parse_mode="HTML")
    
    if text == "/admin" and chat_id == admin_id:
        bot.send_message(chat_id=admin_id,text='tanlang',reply_markup=admin_keys)
    if text == "Stat":
        bot.send_message(chat_id=admin_id,text=f"Statistika: {get_stat()}")
    
    if message.text == "Send User" and message.chat.id == admin_id:
        adver = bot.send_message(chat_id=admin_id,text="Send User | <b>✍️ Xabar matnini kiritng !</b>")
        bot.register_next_step_handler(adver, ads_send_user)
    if message.text == "Send Group" and message.chat.id == admin_id:
        adver = bot.send_message(chat_id=admin_id,text="Send User | <b>✍️ Xabar matnini kiritng !</b>")
        bot.register_next_step_handler(adver, ads_send_group)

    
    if message.text == "Forward User" and message.chat.id == admin_id:
        adver = bot.send_message(chat_id=admin_id,text="user |<b>✍️ Xabar matnini kiritng !</b>")
        bot.register_next_step_handler(adver, for_send_user)
    if message.text == "Forward Group" and message.chat.id == admin_id:
        adver = bot.send_message(chat_id=admin_id,text="Group |<b>✍️ Xabar matnini kiritng !</b>")
        bot.register_next_step_handler(adver, for_send_group)

@bot.callback_query_handler(func= lambda callback : callback.data)
def locations(callback):
    chat_id = callback.message.chat.id
    data = callback.data
    if data == "andijon":
        add_location(int(chat_id),"andijon")
        bot.send_message(chat_id=chat_id,text="Manzilingiz Andijon sifatida sozlandi✅")
print(bot.get_me())
bot.polling()