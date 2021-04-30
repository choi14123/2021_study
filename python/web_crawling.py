import requests
from bs4 import BeautifulSoup

request = requests.get('https://music.bugs.co.kr/chart')
html = request.text
soup = BeautifulSoup(html, 'html.parser')
songs = soup.findAll('p', {'class': 'title'})

for i in range(100):
    print('{}위 : {} '.format(i + 1, songs[i].text.strip()))
