import requests
from bs4 import BeautifulSoup

def pray_time(city):
    try:
        url = f"https://namozvaqti.uz/shahar/{city}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        bomdod = soup.find("p", {"id": "bomdod"}).text.strip()
        quyosh = soup.find("p", {"id": "quyosh"}).text.strip()
        peshin = soup.find("p", {"id": "peshin"}).text.strip()
        asr = soup.find("p", {"id": "asr"}).text.strip()
        shom = soup.find("p", {"id": "shom"}).text.strip()
        xufton = soup.find("p", {"id": "hufton"}).text.strip()

        message = f"🕌{city} namoz vaqtlari\n🌙Bomdod: {bomdod}\n🌝Quyosh: {quyosh}\n🌇Peshin: {peshin}\n🌅Asr: {asr}\n🌄Shom: {shom}\n🌘Xufton: {xufton}"
        return message
    except:
        return "mavjud emas"

while True:
    a = input("Shaharni kiriting: ")
    print(pray_time(a))