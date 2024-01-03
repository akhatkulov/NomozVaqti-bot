import schedule
import time
import telebot 
from api import *
bot = telebot.TeleBot("6709370621:AAGs70M4tdROjUD6o3PbSbA54rg_u8O3YVU")
from helper import *

db_gr = Database_gr(path_to_db="data/group.db")
db = Database(path_to_db="data/main.db")

def time_calc(timer):
    a = timer

    b = list(a.split(":"))
    c = b[1]
    b[1] = int(b[1]) - 5
    if b[1]>=0:

	    return str(b[0])+":"+str(b[1]).zfill(2)
    else:
	    return str(int(b[0])-1).zfill(2)+":"+str(str(60-abs(b[1])).zfill(2))

def bomdod():
    users = db_gr.select_all_users()
    for user in users:
        user_id = user[0]


        bot.send_message(chat_id=user_id,text=f"""
Бомдод вақтига оз қолди.
Бомдод вақти: {time_calc(get_time())} (Тошкент вақти)

Тошкентдан бошқа шаҳарлардаги вақт фарқи⏰

Аввал:⏪
(-1)     -   Чимкент
(-5)     -   Конибодом
(-6)     -   Хўжанд
(-7)     -   Қўқон
(-7)     -   Жамбул
(-10)   -   Наманган
(-10)   -   Фарғона
(-10)   -   Марғилон
(-11)   -   Андижон
(-14)   -   Ўш
(-15)   -   Жалолобод
(-21)   -   Бишкек
(-21)   -   Олма Ота

Кейин:⏩
(+4)     -   Бекобод
(+4)     -   Туркистон
(+6)     -   Жиззах
(+7)     -   Гулистон
(+7)     -   Денов
(+7)     -   Жомбой
(+9)     -   Самарқанд
(+10)   -   Шаҳрисабз
(+12)   -   Каттақўрғон
(+12)   -   Қарши
(+14)   -   Нурота
(+19)   -   Навоий
(+21)   -   Бухоро
(+35)   -   Хива
(+42)   -   Нукус

Батафсил маълумот олиш учун: @PrayingTime_bot
""")



schedule.every().day.at(time_calc(get_time())).do(bomdod)
schedule.every().day.at(time_calc(get_time())).do(bomdod)
schedule.every().day.at(time_calc(get_time())).do(bomdod)
schedule.every().day.at(time_calc(get_time())).do(bomdod)
schedule.every().day.at(time_calc(get_time())).do(xufton)

while True:
    schedule.run_pending()
    time.sleep(1)