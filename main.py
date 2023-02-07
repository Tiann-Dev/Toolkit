import random,os,sys,requests,re,json,bs4,time
from bs4 import BeautifulSoup as parser

def exit():
    os.system("exit")

p = '\033[97m'  # PUTIH
m = '\033[91m' # MERAH
h = '\033[92m'  # HIJAU
k = '\033[93m'  # KUNING
biru = '\x1b[0;34m' #BIRU +
u = '\033[95m' # UNGU
bru = '\33[1;96m' # BIRU -
asu = random.choice([k,h,u,biru])

os.system("git pull")

def logo():
    print(f"""{asu}
 _____      _       _   _____            _ _    _ _   
/__   \___ | | ___ | | /__   \___   ___ | | | _(_) |_ 
  / /\/ _ \| |/ _ \| |   / /\/ _ \ / _ \| | |/ / | __|
 / / | (_) | | (_) | |  / / | (_) | (_) | |   <| | |_ 
 \/   \___/|_|\___/|_|  \/   \___/ \___/|_|_|\_\_|\__|

 {p}Created By ࿐ {bru} Christian S. {p}ಮ
                                                      
    {p}""")
 
logo()
rr = random.randint
rc = random.choice
ip = requests.get("https://api.ipify.org").text

def cookies():
    try:
        ses=requests.Session()
        n,cok,cookie=0,[],[]
        #url = parser(ses.get("https://mbasic.facebook.com/100032386028880/posts/674525870303608/?app=fbl").text,"html.parser")
        url = parser(ses.get("https://mbasic.facebook.com/photo.php?fbid=549345863862686&id=100063618310179&set=a.309477517849523&eav=AfYWXx6P3rikaNUKhUa1aQI9HyITaH3Xto98Ht2qYSzRPDwLVjTXOzNUb9cgdlmzEMo&paipv=0&p=0&av=100009469942335&refid=13").text,"html.parser")
        for z in url("span"):
            cok.append(z.text)
        for x in "".join(cok).split("datr"):
                cok = f"datr{x}"
                if cok in cookie:
                    pass
                else:
                    if "Beranda" in cok:
                        pass
                    else:
                        n+=1
                        print()
                        cookie.append(cok)
                        print(f"{n}.{h} {cok}{p}\n")
    except:pass

def ua_kamu():
    try:
        os.system("xdg-open http://whatsmyuseragent.org/");exit()
    except:pass

print(" 1. Cookies Facebook")
print(" 2. Kalkulator")
print(" 3. Cek Aplikasi Terkait")
print(" 4. Convert Cookies Ke Token EAAB")
print(f'{u} └── Other Tools{p} ☂')
print("    5. Random User Agent ")
print("    6. Chekpoint Detector")
print('    7. Cek IP Address')
print('    8. Cek User Agent Kamu')
print()
ask = input(f' {m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}')

if ask in ('1'): 
    cookies()
if ask == ('2'):
    print(f"Hasil Dari {a} x {b} = {h}{int(a)*int(b)}")   
if ask == ('3'):
    print(f"Hasil Dari {a} : {b} = {h}{int(a)/int(b)}") 
if ask == ('4'):
    print(f"Hasil Dari {a} - {b} = {h}{int(a)-int(b)}")
if ask == ('5'): 
    print(f'User Agent :{h} ', ua)
if ask == ('6'): 
    print(f'Proxy :{h} ', prox)
if ask == ('7'):
    print(f'IP Kamu :{h} {ip}')
if ask == ('8'):
    print(f'  Anda Akan Di Arahkan Ke Browser');time.sleep(0.2)
    ua_kamu()