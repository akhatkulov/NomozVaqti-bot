import telebot
from helper import *
from parts import *

bot = telebot.TeleBot("token")
admin_id = 6778990003824873

@bot.message_handler(chat_types=['privet'])
def home(message):
    text = message.text
    chat_id = message.chat.id 
    if text == "/start":
        add_user(chat_id)
        bot.send_message(chat_id=chat_id,text="<b>Assalomu alaykum o'zingizga kerakli bo'lgan bo'limni tanlang </b>",parse_mode="HTML",reply_markup=home_key())

    if text == "⏰Nomoz vaqti":
        bot.send_message(chat_id=chat_id,text="O'z manzilingizni tanlang",reply_markup=pray_time())
    if text == "📖Qo'llanma":
        bot.send_message(chat_id=chat_id,text="sss")
    if text == "💬Bog'lanish":
        bot.send_message(chat_id=chat_id,text="<b>Admin: </b \n <b>Dasturchi: @Akhatkulov </b",parse_mode="HTML")
    
    if text == "/admin" and chat_id == admin_id:
        bot.send_message(chat_id=admin_id,text='tanlang',reply_markup=admin_keys)
    if text == ""