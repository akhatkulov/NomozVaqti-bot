from telebot import types
from parts import *
from data.sqlalchemy import get_channel
def home_key():
    key = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = types.KeyboardButton(text="⏰Nomoz vaqti")
    btn2 = types.KeyboardButton(text="📖Qo'llanma")
    btn3 = types.KeyboardButton(text="💬Bog'lanish")
    btn4 = types.KeyboardButton(text="⚙️Sozlamalar")
    btn5 = types.KeyboardButton(text="✨Ramazon bo'limi")
    key.add(btn1,btn2,btn3)
    key.add(btn4,btn5)
    return key

def location_keys():
    key = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton(text="🌆Andijon",callback_data="andijon")
    btn2 = types.InlineKeyboardButton(text="🌆Angren",callback_data="angren")
    btn3 = types.InlineKeyboardButton(text="🌆Bekobod",callback_data="bekobod")
    btn4 = types.InlineKeyboardButton(text="🌆Boysun",callback_data="boysun")
    btn5 = types.InlineKeyboardButton(text="🌆Buxoro",callback_data="buxoro")
    btn6 = types.InlineKeyboardButton(text="🌆Gazli",callback_data="gazli")
    btn7 = types.InlineKeyboardButton(text="🌆Guliston",callback_data="guliston")
    btn8 = types.InlineKeyboardButton(text="🌆Denov",callback_data="denov")
    btn9 = types.InlineKeyboardButton(text="🌆Dehqonobod",callback_data="dehqonobod")
    btn10 = types.InlineKeyboardButton(text="🌆Do'stlik",callback_data="do'stlik")
    btn11 = types.InlineKeyboardButton(text="🌆Jizzax",callback_data="jizzax")
    btn12 = types.InlineKeyboardButton(text="🌆Zarafshon",callback_data="zarafshon")
    btn13 = types.InlineKeyboardButton(text="🌆Zomin",callback_data="zomin")
    btn15 = types.InlineKeyboardButton(text="🌆Konimex",callback_data="konimex")
    btn16 = types.InlineKeyboardButton(text="🌆Marg'ilon",callback_data="marg'ilon")
    btn17 = types.InlineKeyboardButton(text="🌆Mingbuloq",callback_data="mingbuloq")
    btn18 = types.InlineKeyboardButton(text="🌆Muborak",callback_data="muborak")
    btn19 = types.InlineKeyboardButton(text="🌆Mo'ynoq",callback_data="mo'ynoq")
    btn20 = types.InlineKeyboardButton(text="🌆Navoiy",callback_data="navoiy")
    btn21 = types.InlineKeyboardButton(text="🌆Namangan",callback_data="namangan")
    btn22 = types.InlineKeyboardButton(text="🌆Nukus",callback_data="nukus")
    btn23 = types.InlineKeyboardButton(text="🌆Nur ota",callback_data="nur ota")
    btn24 = types.InlineKeyboardButton(text="🌆Olti ariq",callback_data="olti ariq")
    btn25 = types.InlineKeyboardButton(text="🌆Paxta Obod",callback_data="paxta obod")
    btn26 = types.InlineKeyboardButton(text="🌆Rishton",callback_data="rishton")
    btn27 = types.InlineKeyboardButton(text="🌆Samarqand",callback_data="samarqand")
    btn28 = types.InlineKeyboardButton(text="🌆Termiz",callback_data="termiz")
    btn29 = types.InlineKeyboardButton(text="🌆Toshkent",callback_data="toshkent")
    btn30 = types.InlineKeyboardButton(text="🌆To'rt Ko'l",callback_data="to'rt ko'l")
    btn31 = types.InlineKeyboardButton(text="🌆Urganch",callback_data="urganch")
    btn32 = types.InlineKeyboardButton(text="🌆Urgut",callback_data="urgut")
    btn33 = types.InlineKeyboardButton(text="🌆Uchquduq",callback_data="uchquduq")
    btn34 = types.InlineKeyboardButton(text="🌆Uchqo'rg'on",callback_data="uchqo'rg'on")
    btn35 = types.InlineKeyboardButton(text="🌆Farg'ona",callback_data="farg'ona")
    btn36 = types.InlineKeyboardButton(text="🌆Xiva",callback_data="xiva")
    btn37 = types.InlineKeyboardButton(text="🌆Xonobod",callback_data="xonobod")
    btn38 = types.InlineKeyboardButton(text="🌆Xonqa",callback_data="xonqa")
    btn39 = types.InlineKeyboardButton(text="🌆Xo'ja Obod",callback_data="xo'ja obod")
    btn40 = types.InlineKeyboardButton(text="🌆Chortoq",callback_data="chortoq")
    btn41 = types.InlineKeyboardButton(text="🌆Chust",callback_data="chust")
    btn42 = types.InlineKeyboardButton(text="🌆Shahrixon",callback_data="shahrixon")
    btn43 = types.InlineKeyboardButton(text="🌆Sherobod",callback_data="sherobod")
    btn45 = types.InlineKeyboardButton(text="🌆Yangi bozor",callback_data="yangi bozor")
    btn46 = types.InlineKeyboardButton(text="🌆G'allaorol",callback_data="g'alla orol")
    btn47 = types.InlineKeyboardButton(text="🌆Qarshi",callback_data="qarshi")
    btn48 = types.InlineKeyboardButton(text="🌆Qorako'l",callback_data="qora ko'l")
    btn49 = types.InlineKeyboardButton(text="🌆Quva",callback_data="quva")
    btn50 = types.InlineKeyboardButton(text="🌆Qo'ng'irot",callback_data="qo'ng'irot")
    btn51 = types.InlineKeyboardButton(text="🌆Qo'qon",callback_data="qo'qon")

    key.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn15,btn16,btn17,btn18,btn19,btn20,btn21,btn22,btn23,btn24,btn25,btn26,btn27,btn28,btn29,btn30,btn31,btn32,btn33,btn34,btn35,btn36,btn37,btn38,btn39,btn40,btn41,btn42,btn43,btn45,btn46,btn47,btn48,btn49,btn50,btn51)
    return key 

def abort_button():
    key = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    btn1 = types.KeyboardButton(text="🚫 Bekor qilish")
    key.add(btn1)
    return key

def admin_buttons():
    x = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Statistika", callback_data="stat")
    btn2 = types.InlineKeyboardButton(text="Xabar yuborish", callback_data="send")
    btn3 = types.InlineKeyboardButton(text="Kanallarni sozlash", callback_data="channels")
    x.add(btn1, btn2, btn3)
    return x

def join_key():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    x = get_channel()
    r = 1
    for i in x:
        keyboard.add(
            types.InlineKeyboardButton(f"〽️ {r}-kanal", url=f"https://t.me/{i}")
        )
        r += 1
    keyboard.add(types.InlineKeyboardButton('✅ Tasdiqlash', callback_data='/start'))
    return keyboard

def menu_ramadan():
    x = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="🤲Duolar",callback_data="duolar")
    btn2 = types.InlineKeyboardButton(text="🕔Vaqtlar",callback_data="vaqtlar")
    x.add(btn1,btn2)
    return x

def channel_control():
    x = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="➕Kanal qo'shish", callback_data="channel_add")
    btn2 = types.InlineKeyboardButton(text="➖Kanalni olib tashlash", callback_data="channel_del")
    x.add(btn1, btn2)
    return x
