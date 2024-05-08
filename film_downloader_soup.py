import requests
from bs4 import BeautifulSoup

def user_url():
    url = 'https://www.film2movie.asia/108539/%d8%af%d8%a7%d9%86%d9%84%d9%88%d8%af-%d8%b3%d8%b1%db%8c%d8%a7%d9%84-star-wars-the-bad-batch/'
    return url

def user_quality():
    quality = input('Enter the video quality [480p,720p,1080p,1080hq,online]: ')
    quality = '480p'
    return quality

def episode():
    ep = input('Enter the episode number: ')
    return ep

def get_links(url):
    quality_list = ['480p','720p','1080p','1080hq','online']
    data = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    video_id = soup.select('a[href^="https://film2movie.upera.tv/"]')
    c =0
    for i in range(1,6):
        for a in range(5):
            data[f'{i}-{quality_list[a]}'] = video_id[c].get('href')
            c += 1
    return data

def download(data ,quality,ep):
    link = data[f'{ep}-{quality}']
    with requests.get(link, stream=True) as r:
        with open(f'{ep}_{quality}.mp4','wb') as f:
            for video in r.iter_content(chunk_size=1024):
                f.write(video)

download(get_links(user_url()),user_quality(),episode())