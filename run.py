import random,os,sys,requests,re,json,bs4,time
from bs4 import BeautifulSoup as parser

def logo():
    print(f"""{asu}
 _____      _       _   _____            _ _    _ _   
/__   \___ | | ___ | | /__   \___   ___ | | | _(_) |_ 
  / /\/ _ \| |/ _ \| |   / /\/ _ \ / _ \| | |/ / | __|
 / / | (_) | | (_) | |  / / | (_) | (_) | |   <| | |_ 
 \/   \___/|_|\___/|_|  \/   \___/ \___/|_|_|\_\_|\__|

 {p}Created By ࿐ {bru} Christian S. {p}ಮ
                                                      
    {p}""")

def exit():
    os.system("exit")

def update():
    os.system("git pull")

class Dump_regex:
	def __init__(self):
		self.ses = requests.Session()
		self.os = os.system
	
	def login(self):
		self.os("clear")
		self.coki = input("[?] cookie : ")
		try:
			self.nama = re.search('name="primary_first_name" value="(.*?)"',str(self.ses.get("https://m.facebook.com/settings/account/?name&refresh_on_back=1&refid=70",cookies={"cookie": self.coki}).text)).group(1)
			print("[!] selamat datang %s "%(self.nama))
			open(".cookie.txt","w").write(self.coki)
		except: exit("[!] invalid")
		self.menu()
		
	def menu(self):
		self.os("clear")
		try:
			self.cok = {"cookie": open(".cookie.txt","r").read()}
			self.nama = re.search('name="primary_first_name" value="(.*?)"',str(self.ses.get("https://m.facebook.com/settings/account/?name&refresh_on_back=1&refid=70",cookies=self.cok).text)).group(1)
		except: self.login()
		apa = input(f"{logo()} \n\n 1. Dump Publik\n  2. Dump Masal\n   3. Keluar\n\n{m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}")
		print("-"*30)
		if apa in ["1","01"]:
			akun = input(" ꧁  ⁣Target : ")
			self.file = input(" ꧁⁣  Masukan Nama File Anda \n ꧁⁣  Nama : ")
			if "https" in str(akun): self.user = akun.split("/")[3]
			else: self.user = akun
			self.cek_target()
			self.info_file()
			self.dump_publik(f"https://mbasic.facebook.com/{self.user}/friends")	
		elif apa in ["2","02"]:
			xx = int(input(" ꧁⁣  Berapa Id? : "))
			self.file = input(" ꧁ ⁣ Masukan Nama File Anda \n ꧁ ⁣ Nama : ")
			self.info_file()
			for x in range(xx):
				akun = input(" ꧁ ⁣ Target : ")
				if "https" in str(akun): self.user = akun.split("/")[3]
				else: self.user = akun
				self.cek_target()
				self.dump_publik(f"https://mbasic.facebook.com/{self.user}/friends")
		elif apa in ["3","03"]: self.os("rm -rf .cookie.txt"); exit()
		else: exit()
	
	def info_file(self):
		print(f"「ཀའ」 Hasil Di : /sdcard/{self.file}.txt")
		
	def cek_target(self):
		try:
			link = self.ses.get(f"https://mbasic.facebook.com/{self.user}/friends", cookies=self.cok).text
			if "Tidak Ada Teman Untuk Ditampilkan" in link:
				exit("[!] daftar teman tidak di publikasikan")
			elif "Halaman yang Anda minta tidak ditemukan." in link:
				exit(f"[!] pengguna dengan id {self.user} tidak ditemukan")
			elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in link:
				exit("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun")
			elif "Konten Tidak Ditemukan" in link:
				exit(f"[!] Pengguna Dengan Id {self.user} tidak ditemukan")
			else: pass
		except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
			exit("[!] kesalahan pada koneksi")
	
	def dump_publik(self, url):	
		try:
			link = self.ses.get(url, headers={"Host": "mbasic.facebook.com", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "max-age=0", "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="106"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "", "ch-ua-platform": '"Android"', "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/72.4.3767.69265", "cookie": self.cok["cookie"]}).text
			data = re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',link)
			for user in data:
				if "profile.php?" in user[0]:
					mentah = re.findall("id\=(.*?)\&",user[0])[0]+"|"+user[1]
					open(f"/sdcard/{self.file}.txt","a").write(str(mentah)+"\n")
					xxx = open(f"/sdcard/{self.file}.txt","r").read().splitlines()
					print(f'\r[!] {len(xxx)} - %s        '%(user[1]),end=" ")
				else:
					mentah = re.findall("\/(.*?)\?eav",user[0])[0]+"|"+user[1]
					open(f"/sdcard/{self.file}.txt","a").write(str(mentah)+"\n")
					xxx = open(f"/sdcard/{self.file}.txt","r").read().splitlines()
					print(f'\r[!] {len(xxx)} - %s        '%(user[1]),end=" ")
				sys.stdout.flush()
			if "Lihat Teman Lain" in link:
				self.dump_publik("https://mbasic.facebook.com"+parser(link, "html.parser").find("a", string="Lihat Teman Lain").get("href"))
		except Exception as e: print(e)

p = '\033[97m'  # PUTIH
m = '\033[91m' # MERAH
h = '\033[92m'  # HIJAU
k = '\033[93m'  # KUNING
biru = '\x1b[0;34m' #BIRU +
u = '\033[95m' # UNGU
bru = '\33[1;96m' # BIRU -
asu = random.choice([k,h,u,biru])

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

update()

logo()
print(" 1. Cookies Facebook")
print(" 2. Dump Id")
print(" 3. Cek Aplikasi Terkait")
print(" 4. Convert Cookies Ke Token EAAB")
print(f'{u} └── Other Tools{p} ☂')
print("     5. Random User Agent ")
print("     6. Chekpoint Detector")
print('     7. Cek IP Address')
print('     8. Cek User Agent Kamu')
print(f'{u}     └── Special Tools{p} ☂')
print("         9. Random User Agent ")
print("         10. Chekpoint Detector")
print()
ask = input(f' {m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}')

if ask in ('1'): 
    cookies()
if ask == ('2'):
    Dump_regex().menu()  
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
