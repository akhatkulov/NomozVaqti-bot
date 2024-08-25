import requests
from bs4 import BeautifulSoup
from helper.others import all_locations
def pray_time(city):
    url = f"https://namozvaqti.uz/shahar/{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    def get_prayer_time(id):
        element = soup.find("p", {"id": id})
        return element.text.strip() if element else "N/A"
    
    bomdod = get_prayer_time("bomdod")
    quyosh = get_prayer_time("quyosh")
    peshin = get_prayer_time("peshin")
    asr = get_prayer_time("asr")
    shom = get_prayer_time("shom")
    xufton = get_prayer_time("hufton")
    city = [key for key, value in all_locations.items() if value == city]
    
    message = (
        f"🕌<b>{city[0].capitalize()} namoz vaqtlari</b>\n"
        f"🌙<b>Bomdod:</b> {bomdod}\n"
        f"🌝<b>Quyosh:</b> {quyosh}\n"
        f"🌇<b>Peshin:</b> {peshin}\n"
        f"🌅<b>Asr:</b> {asr}\n"
        f"🌄<b>Shom:</b> {shom}\n"
        f"🌘<b>Xufton:</b> {xufton}"
    )
    print(message)
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

def api_connector(a):
    x = pray_time(str(a))
    return x

print("Bomdod: ",get_time()['bomdod'])
print("Peshin: ",get_time()['peshin'])
print("Shom: ",get_time()['shom'])
print("Xufton: ",get_time()['xufton'])
print("Quyosh: ",get_time()['quyosh'])
