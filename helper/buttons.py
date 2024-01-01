from telebot import types

def home_key():
    key = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = types.KeyboardButton(text="⏰Nomoz vaqti")
    btn2 = types.KeyboardButton(text="📖Qo'llanma")
    btn3 = types.KeyboardButton(text="💬Bog'lanish")
    key.add(btn1,btn2,btn3)
    return key

def location_keys():
    key = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn2 = types.InlineKeyboardButton(text="🌆Buxoro",data="buxoro")
    btn3 = types.InlineKeyboardButton(text="🌆Farg'ona",data="andijon")
    btn4 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn5 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn6 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn7 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn8 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn9 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn10 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn11 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    btn12 = types.InlineKeyboardButton(text="🌆Andijon",data="andijon")
    key.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12)
    return key 
def admin_keys():
    key = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = types.KeyboardButton(text="Send User")
    btn2 = types.KeyboardButton(text="Send Group")
    btn3 = types.KeyboardButton(text="Forward User")
    btn4 = types.KeyboardButton(text="Forward Group")
    btn5 = types.KeyboardButton(text="Stat")
    key.add(btn1,btn2,btn3,btn4,btn5)
    return key
