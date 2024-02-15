from helper import *
import telebot 

bot = telebot.TeleBot("6709370621:AAH8ErEPkh9dzu7V9m4kuL7thNeHdjYeUxs")

db_gr = Database_gr(path_to_db="data/group.db")
db = Database(path_to_db="data/main.db")
admin_id = 789945598
def ads_send_group():
    users = db_gr.select_all_users()
    for user in users:
        user_id = user[0]

def ads_send_group(message):

    text = message.text
    if text=="🚫 Bekor qilish":
        bot.send_message(message.chat.id,"🚫 Xabar yuborish bekor qilindi !",reply_markup=admin_keys())
    else:
        try:
            users = db_gr.select_all_users()
            for user in users:
                chat_id = user[0]
                print(chat_id)
                bot.send_message(chat_id,message.text)
            bot.send_message(admin_id,text="<b>✅ Xabar hamma foydalanuvchiga yuborildi!</b>")
        except:
            pass

def ads_send_user(message):
    try:
        text = message.text
        if text=="🚫 Bekor qilish":
            bot.send_message(message.chat.id,text="🚫 Xabar yuborish bekor qilindi !",reply_markup=admin_keys())
        else:
            users = db.select_all_users()
            for user in users:
                chat_id = user[0]
                print(chat_id)
                bot.send_message(chat_id,message.text)
            bot.send_message(admin_id,text="<b>✅ Xabar hamma foydalanuvchiga yuborildi!</b>",reply_markup=admin_keys())
    except:
        pass

def for_send_user(message):
    
    text = message.text
    if text == "🚫 Bekor qilish":
        bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi!")
    else:
        users = db.select_all_users()
        for user in users:
            try:
                chat_id = user[0]
                print(chat_id)
                bot.forward_message(chat_id, admin_id, message.message_id)
            except Exception as e:
                print(e)
        bot.send_message(admin_id, "✅ Xabar hamma foydalanuvchiga yuborildi!")