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
    quyosh = soup.find("p", {"id": "quyosh"}).text.strip()
    peshin = soup.find("p", {"id": "peshin"}).text.strip()
    asr = soup.find("p", {"id": "asr"}).text.strip()
    shom = soup.find("p", {"id": "shom"}).text.strip()
    xufton = soup.find("p", {"id": "hufton"}).text.strip()
    l = {"bomdod":bomdod,
    "peshin":peshin,
    "asr":asr,
    "shom":shom,
    "xufton":xufton,
    "quyosh":quyosh}
    return l

print("Bomdod: ",get_time()['bomdod'])
print("Peshin: ",get_time()['Peshin'])
print("Shom: ",get_time()['Shom'])
print("Xufton: ",get_time()['Xufton'])
print("Quyosh: ",get_time()['Quyosh'])


print(pray_time("samarqand"))