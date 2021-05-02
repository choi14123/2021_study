from urllib.request import urlopen
from bs4 import BeautifulSoup

a = urlopen("https://music.bugs.co.kr/chart")
soup = BeautifulSoup(a.read(), "html.parser")
songs = soup.findAll("p", {"class" : "title"})
for i in range (100) :
    print("{} 위  :  {}".format(i + 1, songs[i].text.strip()))
