import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank_number = 1

for music in musics:
    # movie 안에 a 가 있으면,
    music_title= music.select_one('td.info>a.title')
    music_artist = music.select_one('td.info>a.artist')

    if music_title is not None:
        # print(music_artist.text.strip())

        print("순위:"+str(rank_number)+"등")
        print("제목: "+music_title.text.strip())
        print("아티스트:"+music_artist.text.strip())
        print(" ")
        rank_number += 1
