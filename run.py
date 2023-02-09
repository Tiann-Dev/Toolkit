import random,os,sys,requests,re,json,bs4,time
from bs4 import BeautifulSoup as parser
import fb as e

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
def clear():
	os.system("clear")
def update():
    os.system("git pull")

class Bokep:
	
	def __init__(self):
		self.a = ""
		
	def __jalan__(self, janda):
		for pepek in janda + "\n":
			sys.stdout.write(pepek)
			sys.stdout.flush()
			time.sleep(0.03)

	def __menu__(self):
		os.system("clear")
		logo()
		print(f"{p}[ {h}Welcome Pengocox Handal{p} ]\n")
		print(f"{p}1. Bokep indo ({h}not vpn{p})")
		print(f"{p}2. Bokep japan ({h}use vpn{p})")
		print(f"{p}3. Bokep english ({h}use vpn{p})")
		print(f"{p}4. Download apk {h}xnxx{p}")
		print(f"{p}5. View link bokep terbaru")
		__nanya__ = input(f"\n{p}> {m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}")
		if __nanya__ == "1" or __nanya__ == "01":self.indo()
		elif __nanya__ == "2" or __nanya__ == "02":self.japan()
		elif __nanya__ == "3" or __nanya__ == "03":self.english()
		elif __nanya__ == "4" or __nanya__ == "04":self.download()
		elif __nanya__ == "5" or __nanya__ == "05":self.lihat()
		else:Bokep().__menu__()
		
	def indo(self):
		try:
			print(f"\n\n{p}[ {h}Kumpulan Bokep Indo{p} ]\n")
			print(f"{p}1. Bokep smp ({h}hanya menonton{p})")
			print(f"{p}2. Bokep sma ({h}hanya menonton{p})")
			print(f"{p}3. Bokep remaja ({h}bisa download{p})")
			print(f"{p}4. Bokep hijab ({h}bisa download{p})")
			print(f"{p}5. Bokep colmek ({h}hanya menonton{p})")
			ask = input(f"\n{p}> {m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p} ")
			if ask == "1":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://bokepindo13.com/?s=smp");exit()
			elif ask == "2":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://bokepindo13.com/?s=sma");exit()
			elif ask == "3":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://itubokep.store/?s=abg");exit()
			elif ask == "4":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://itubokep.store/?s=hijab+");exit()
			elif ask == "5":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://linkbokep.me/?s=colmek");exit()
		except:pass

	def japan(self):
		try:
			print(f"\n\n{p}[ {h}Kumpulan Bokep Japan{p} ]\n")
			print(f"{p}1. Bokep japan school ({h}bisa download{p})")
			print(f"{p}2. Bokep japan family ({h}bisa download{p})")
			print(f"{p}3. Bokep japan random video ({h}bisa download{p})")
			ask = input(f"\n{p}> {m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}")
			if ask == "1":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xvideos.com/?k=Japanese+school+");exit()
			elif ask == "2":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xvideos.com/?k=Japanese+family");exit()
			elif ask == "3":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xvideos.com/?k=Japanese%20teacher&top");exit()
			elif ask == "4":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xvideos.com/?k=Japanese+hd");exit()
		except:pass
		
	def english(self):
		try:
			print(f"\n\n{p}[ {h}Kumpulan Bokep English{p} ]\n")
			print(f"{p}1. Bokep student & teacher ({h}bisa download{p})")
			print(f"{p}2. Bokep family sex ({h}bisa download{p})")
			print(f"{p}3. Bokep school party sex ({h}bisa download{p})")
			print(f"{p}4. Bokep public random ({h}bisa download{p})")
			print(f"{p}5. Bokep step mom ({h}bisa download{p})")
			print(f"{p}6. Bokep step sister ({h}bisa download{p})")
			ask = input(f"\n{p}> {m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}")
			if ask == "1":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/English+student");exit()
			elif ask == "2":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/English+family");exit()
			elif ask == "3":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/student+party");exit()
			elif ask == "4":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/public+agent");exit()
			elif ask == "5":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/step+mom");exit()
			elif ask == "6":
				self.__jalan__(f"\n{p}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/step%20sister?top");exit()
		except:pass
		
	def download(self):
		try:
			self.__jalan__(f"\n{p}!. Kamu akan diarahkan ke website")
			self.__jalan__(f"{p}!. Pencet Tulisan {h}Download the OFFICIAL XNXX APP (Stable){p}")
			os.system("xdg-open https://www.xnxx.net/");exit()
		except:pass

	def lihat(self):
		try:
			self.__jalan__(f"\n\n{p}[ {h}Kumpulan Link Bokep Random{p} ]\n");time.sleep(1)
			print(f"{p}> {h}https://jambulmemek.world");time.sleep(0.03)
			print(f"{p}> {h}https://ngentot.cam");time.sleep(0.03)
			print(f"{p}> {h}https://fakebokep.com");time.sleep(0.03)
			print(f"{p}> {h}https://bokepxxi.lol");time.sleep(0.03)
			print(f"{p}> {h}https://bokepviral.cam");time.sleep(0.03)
			print(f"{p}> {h}https://ngebokep.lol");time.sleep(0.03)
			print(f"{p}> {h}https://xjilbab.xyz");time.sleep(0.03)
			print(f"{p}> {h}https://agenbokep.xyz");time.sleep(0.03)
			print(f"{p}> {h}https://bokeh.top");time.sleep(0.03)
			print(f"{p}> {h}https://bokepin.pics");time.sleep(0.03)
			print(f"{p}> {h}https://bokep.pro");time.sleep(0.03)
			print(f"{p}> {h}https://xvideos.com");time.sleep(0.03)
			print(f"{p}> {h}https://playbokep.ws");time.sleep(0.03)
			print(f"{p}> {h}https://bokepep.me");time.sleep(0.03)
			print(f"{p}> {h}https://www.indo18.com");time.sleep(0.03)
			print(f"{p}> {h}https://linkbokep.cam");time.sleep(0.03)
			print(f"{p}> {h}https://vndevtop.com");time.sleep(0.03)
			print(f"{p}> {h}https://xbokepfb.com");time.sleep(0.03)
			print(f"{p}> {h}https://www.asexyporn.com");time.sleep(0.03)
			print(f"{p}> {h}https://pornkai.com");time.sleep(0.03)
			print(f"{p}> {h}https://bokepcrot.design");time.sleep(0.03)
			print(f"{p}> {h}https://m.spankbang.com");time.sleep(0.03)
			print(f"{p}> {h}https://www.eporner.com");time.sleep(0.03)
			print(f"{p}> {h}https://pornzog.com");time.sleep(0.03)
			print(f"{p}> {h}https://pestasex.cam/categories");time.sleep(0.03)
			print(f"{p}> {h}https://sangetods.net");time.sleep(0.03)
			print(f"{p}> {h}https://perawanbokep.site");time.sleep(0.03)
			print(f"{p}> {h}https://pwetan.com");time.sleep(0.03)
			print(f"{p}> {h}https://www.kontol.in");time.sleep(0.03)
			print(f"{p}> {h}https://malemjumat.lol");time.sleep(0.03)
			print(f"{p}> {h}https://brutalfucking.net/id/");time.sleep(0.03)
			print(f"{p}> {h}https://colmek.link/");time.sleep(0.03)
			self.__jalan__(f"\n{p}[ {h}Full Link Bokep Terbaru{p} ]");exit()
		except:pass

def cek_apk():
	clear();time.sleep(1)
	logo()
	try:
		kukiz = input(" Masukan Cookie : ")
		ses = requests.Session()
		url = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kukiz})
		psot = parser(url.text,"html.parser")
		fick = psot.find("form", {"method":"post"})
		game = [memek.text for memek in fick.find_all("h3")]
		if len(game) == 0:
			print("\n× Tidak Ada Aplikasi Aktif")
		else:
			for kontol in range(len(game)):
				print("\n- Mengechek Aplikasi Aktif")
				print("%s %s "%(kontol+1, game[kontol].replace(" Di akses pada ", " Di tambahkan pada")));time.sleep(1)
			link = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie":kukiz})
			post = parser(link.text,"html.parser")
			cari = post.find("form",{"method":"post"})
			game = [kontol_.text for kontol_ in cari.find_all("h3")]
			if len(game) == 0:
				print("\n× Tidak Ada Aplikasi Kadarluarsa")
			else:
				for aplikasi in range(len(game)):
					print("\n- Mengechek Aplikasi Kadarluarsa")
			print("\n%s %s"%(aplikasi+1, game[aplikasi].replace("Kadarluarsa pada","Tidak di akses pada")));time.sleep(1)
	#- Di hapus
		try:
			link = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=removed", cookies={"cookie":kukiz})
			post = parser(link.text,"html.parser")
			cari = post.find("form",{"method":"post"})
			game = [_kontol_.text for _kontol_ in cari.find_all("h3")]
			if len(game) == 0:
				print("\n× Tidak ada aplikasi di yanh hapus")
			else:
				for khamdihiXD in range(len(game)):
					print("× Mengechek aplikasi yang di hapus")
				print("\n%s %s"%(khamdihiXD+1, game[khamdihiXD].replace("Di hapus pada","Di hapus")))
		except AttributeError:
			print("× Tidak ada aplikasi yang di hapus / Cookie invalid!")
	except AttributeError:
		print(" × cokie invalid")

class Dump_regex:
	def __init__(self):
		self.ses = requests.Session()
		self.os = os.system
	
	def login(self):
		self.os("clear")
		self.coki = input(" ༒  Masukan Cookie : ")
		try:
			self.nama = re.search('name="primary_first_name" value="(.*?)"',str(self.ses.get("https://m.facebook.com/settings/account/?name&refresh_on_back=1&refid=70",cookies={"cookie": self.coki}).text)).group(1)
			print(" ꧁  selamat datang %s "%(self.nama))
			open(".cookie.txt","w").write(self.coki)
		except: exit(" ꧁ Cookies Invalid! ")
		self.menu()
		
	def menu(self):
		self.os("clear")
		try:
			self.cok = {"cookie": open(".cookie.txt","r").read()}
			self.nama = re.search('name="primary_first_name" value="(.*?)"',str(self.ses.get("https://m.facebook.com/settings/account/?name&refresh_on_back=1&refid=70",cookies=self.cok).text)).group(1)
		except: self.login()
		apa = input(f"{logo()} \n\n 1. Dump Publik\n  2. Dump Masal\n   3. Keluar {m}(Delete Cookie)\n\n{m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}")
		print("-"*30)
		if apa in ["1","01"]:
			akun = input("꧁  ⁣Target : ")
			self.file = input("꧁⁣  Masukan Nama File Anda \n꧁⁣  Nama : ")
			if "https" in str(akun): self.user = akun.split("/")[3]
			else: self.user = akun
			self.cek_target()
			self.info_file()
			self.dump_publik(f"https://mbasic.facebook.com/{self.user}/friends")	
		elif apa in ["2","02"]:
			xx = int(input("꧁⁣  Berapa Id? : "))
			self.file = input("꧁ ⁣ Masukan Nama File Anda \n꧁ ⁣ Nama : ")
			self.info_file()
			for x in range(xx):
				akun = input("꧁ ⁣ Target : ")
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
				exit(" ꧁  daftar teman tidak di publikasikan")
			elif "Halaman yang Anda minta tidak ditemukan." in link:
				exit(f" ꧁  pengguna dengan id {self.user} tidak ditemukan")
			elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in link:
				exit(" ꧁  facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun")
			elif "Konten Tidak Ditemukan" in link:
				exit(f" ꧁  Pengguna Dengan Id {self.user} tidak ditemukan")
			else: pass
		except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
			exit(" ꧁  kesalahan pada koneksi")
	
	def dump_publik(self, url):	
		try:
			link = self.ses.get(url, headers={"Host": "mbasic.facebook.com", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "max-age=0", "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="106"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "", "ch-ua-platform": '"Android"', "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/72.4.3767.69265", "cookie": self.cok["cookie"]}).text
			data = re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',link)
			for user in data:
				if "profile.php?" in user[0]:
					mentah = re.findall("id\=(.*?)\&",user[0])[0]+"|"+user[1]
					open(f"/sdcard/{self.file}.txt","a").write(str(mentah)+"\n")
					xxx = open(f"/sdcard/{self.file}.txt","r").read().splitlines()
					print(f'\r࿐ {len(xxx)} - %s        '%(user[1]),end=" ")
				else:
					mentah = re.findall("\/(.*?)\?eav",user[0])[0]+"|"+user[1]
					open(f"/sdcard/{self.file}.txt","a").write(str(mentah)+"\n")
					xxx = open(f"/sdcard/{self.file}.txt","r").read().splitlines()
					print(f'\r࿐ {len(xxx)} - %s        '%(user[1]),end=" ")
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
        url = parser(ses.get("https://mbasic.facebook.com/100032386028880/posts/674525870303608/?app=fbl").text,"html.parser")
        #url = parser(ses.get("https://mbasic.facebook.com/photo.php?fbid=549345863862686&id=100063618310179&set=a.309477517849523&eav=AfYWXx6P3rikaNUKhUa1aQI9HyITaH3Xto98Ht2qYSzRPDwLVjTXOzNUb9cgdlmzEMo&paipv=0&p=0&av=100009469942335&refid=13").text,"html.parser")
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

update();clear();logo()

print(" 1. Cookies Facebook")
print(" 2. Dump Id")
print(" 3. Cek Aplikasi Terkait")
print(" 4. Convert Cookies Ke Token EAAB")
print(f'{u} └── Other Tools{p} ☂')
print("     5. Bokep Link :v ")
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
	print(f'\n  Tunggu Sebentar ۝ঔৣ✞ ');time.sleep(2)
	Dump_regex().menu()
if ask == ('3'):
    cek_apk()
if ask == ('4'):
    print(f'Sorry, Sedang Maintance!')
if ask == ('5'): 
    Bokep().__menu__()
if ask == ('6'): 
    print(f'Sorry, Sedang Maintance!')
if ask == ('7'):
    print(f'IP Kamu :{h} {ip}')
if ask == ('8'):
    print(f'  Anda Akan Di Arahkan Ke Browser');time.sleep(2)
    ua_kamu()
if ask == ('9'): 
    e()
if ask == ('10'): 
    print(f'\nSorry, Sedang Maintance!\n')
exit()