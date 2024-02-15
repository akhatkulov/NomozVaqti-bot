import requests
from bs4 import BeautifulSoup


def pray_time(city):
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
def get_time():
    url = f"https://namozvaqti.uz/shahar/toshkent"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    bomdod = soup.find("p", {"id": "bomdod"}).text.strip()
#    quyosh = soup.find("p", {"id": "quyosh"}).text.strip()
    peshin = soup.find("p", {"id": "peshin"}).text.strip()
    asr = soup.find("p", {"id": "asr"}).text.strip()
    shom = soup.find("p", {"id": "shom"}).text.strip()
    xufton = soup.find("p", {"id": "hufton"}).text.strip()
    l = [bomdod,peshin,asr,shom,xufton]
    return list(l)

print(get_time()[0])
print(get_time()[1])
print(get_time()[2])
print(get_time()[3])
print(get_time()[4])


