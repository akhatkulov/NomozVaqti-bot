import sqlite3 
import telebot 

db = sqlite3.connect('data/database.db',check_same_thread=False,isolation_level=None)
cursor = db.cursor()

bot = telebot.TeleBot("6709370621:AAGs70M4tdROjUD6o3PbSbA54rg_u8O3YVU")

db.execute("""CREATE TABLE IF NOT EXISTS users(
    CID INT UNIQUE NOT NULL,
    MANZIL TEXT DEFAULT "home")""")
db.execute("CREATE TABLE IF NOT EXISTS gr(CID INT UNIQUE NOT NULL)")

def add_user(cid):
    try:
        db.execute(f"INSERT INTO users(CID) VALUES(?)",(cid))
    except:
        pass
    db.commit()

def add_location(cid,manzil):
    db.execute(f"UPDATE users SET manzil=? WHERE cid=?",(str(manzil),int(cid)))
    print("--{}--")
    db.commit()

def get_location(cid):
    x = db.cursor(f"SELECT manzil FROM users WHERE cid=?",(cid))
    return x
    print("++++")

def add_gr(cid):
    try:
        db.execute("""INSERT INTO gr(CID)
            VALUES(?)""",(cid))
        db.commit()
    except:
        pass
    

def ads_send_users(message):
    try:
        text = message.text
        if text=="🚫 Bekor qilish":
            bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi !")
        else:
            cursor.execute("SELECT cid FROM users")
            rows = cursor.fetchall()
            for i in rows:
                chat_id = i[0]
                print(chat_id)
                bot.send_message(chat_id,message.text)
            bot.send_photo(admin_id,photo="https://t.me/the_solodest/178",caption="<b>✅ Xabar hamma foydalanuvchiga yuborildi!</b>")
    except:
        pass
def ads_send_group(message):
    try:
        text = message.text
        if text=="🚫 Bekor qilish":
            bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi !")
        else:
            cursor.execute("SELECT cid FROM gr")
            rows = cursor.fetchall()
            for i in rows:
                chat_id = i[0]
                print(chat_id)
                bot.send_message(chat_id,message.text)
            bot.send_photo(admin_id,photo="https://t.me/the_solodest/178",caption="<b>✅ Xabar hamma foydalanuvchiga yuborildi!</b>")
    except:
        pass
def get_stat_user():
    cursor.execute("SELECT COUNT(CID) FROM users")
    rows = cursor.fetchall()
    return rows[0][0]
def get_stat_group():
    cursor.execute("SELECT COUNT(CID) FROM gr")
    rows = cursor.fetchall()
    return rows[0][0]
def get_stat():
    x = get_stat_user()
    y = get_stat_group()
    res = "odamlar: " +  x
    res1 = "Guruhlar: " + x 
    return res + "\n" + res1

def for_send_user(message):
    text = message.text
    if text == "🚫 Bekor qilish":
        bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi!")
    else:
        cursor.execute("SELECT cid FROM users")
        rows = cursor.fetchall()
        for row in rows:
            try:
                chat_id = row[0]
                print(chat_id)
                bot.forward_message(chat_id, admin_id, message.message_id)
            except Exception as e:
                print(e)
        bot.send_message(admin_id, "✅ Xabar hamma foydalanuvchiga yuborildi!")

def for_send_group(message):
    text = message.text
    if text == "🚫 Bekor qilish":
        bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi!")
    else:
        cursor.execute("SELECT cid FROM gr")
        rows = cursor.fetchall()
        for row in rows:
            try:
                chat_id = row[0]
                print(chat_id)
                bot.forward_message(chat_id, admin_id, message.message_id)
            except Exception as e:
                print(e)
        bot.send_message(admin_id, "✅ Xabar hamma guruhlarga yuborildi!")

cursor.close()
db.close()

