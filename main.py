import random,os,sys,requests,re,json,bs4
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

def logo():
    print(f"""{asu}
 _____      _       _   _____            _ _    _ _   
/__   \___ | | ___ | | /__   \___   ___ | | | _(_) |_ 
  / /\/ _ \| |/ _ \| |   / /\/ _ \ / _ \| | |/ / | __|
 / / | (_) | | (_) | |  / / | (_) | (_) | |   <| | |_ 
 \/   \___/|_|\___/|_|  \/   \___/ \___/|_|_|\_\_|\__|

 {p}Created By ࿐ {bru} Christian S.
                                                      
    {p}""")
 
logo()
rr = random.randint
rc = random.choice
ip = requests.get("https://api.ipify.org").text
user = open('user-agents_oppo-browser.txt','r').read().splitlines()
ua = rc(user)
proxy = open('proxy.txt','r').read().splitlines()
prox = rc(proxy)
ugent = requests.get("https://www.yayanxd.my.id/server/ua/").text

print("1. Free Cookies Facebook")
print("2. Kalikan")
print("3. Bagikan")
print("4. Jumlahkan")
print()
print(f'{u}└── Other Tools {p}')
print("    5. Random User Agent ")
print("    6. Random Proxy")
print('    7. Cek IP Address')
print('    8. Cek User Agent Kamu')
print()
ask = input(f'{m}Pi{k}li{h}h -> {p}')

if ask in ('1'):
    print()
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
        ses=requests.Session()
n,cok,cookie=0,[],[]
url = parser(ses.get("https://mbasic.facebook.com/100032386028880/posts/674525870303608/?app=fbl").text,"html.parser")
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
			cookie.append(cok)
			print(f"{n}. {cok}\n")
   