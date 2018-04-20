import urllib.request
from bs4 import BeautifulSoup
import re, sys
# str = '<span class="nPR"><b>م<font color="red">صالح</font>ه</b>: سازش  - آشتی  - سازگاری  - کنارآمدن     </span>'
# match = re.findall('[:].*', str)
# print(match)


if len(sys.argv)-1 < 1:
    inp_word = input("واژه ی بیگانه: ")
else :
    inp_word = sys.argv
    if inp_word[1]=="-h" or inp_word[1]=="--help":
        print("این برنامه داده های خود را از تارنمای\n",
        "http://beparsi.com\n",
        "دریافت می‌کند.")
        exit()
    else:
        inp_word = str(inp_word[1])

inp_word = inp_word.replace(" ", "%20")
url = 'http://www.beparsi.com/'
values = {'find' : str(inp_word)}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read().decode('utf-8')
# print (respData)

soup = BeautifulSoup(respData, "lxml")
div = soup.findAll("span", {"class": "nPR"})
if len(div) == 0:
    print ("not found!!")
    exit()

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)

count = 0
for value in div:
    if count == 0:
        pass
    elif count == 1:
        value = str(value)
        value = remove_tags(value)
        match = re.search('[:].*', value)
        found = match.group(0)
        found = re.findall('\w+', found)
        worlds = ""
        for word in found:
            worlds += word + "، "

        worlds = worlds[:-2]
        print(worlds)
        break

    count += 1
