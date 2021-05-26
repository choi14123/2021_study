from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
a = urlopen("https://music.bugs.co.kr/chart")
soup = BeautifulSoup(a.read(), "html.parser")
songs = soup.findAll("p", {"class" : "title"})
print(time.strftime('%Y-%m-%d', time.localtime(time.time())),"차트")
for i in range (50) :
    print("{} 위  :  {}".format(i + 1, songs[i].text.strip()))
