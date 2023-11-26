from icrawler.builtin import GoogleImageCrawler,GoogleFeeder,ImageDownloader
from icrawler import Parser,Crawler
from bs4 import BeautifulSoup
import json
import types
alt = open("alts.txt",'r+')
funcType = types.MethodType



def parse1(self, response):
    soup = BeautifulSoup(response.content, 'lxml')
    image_divs = soup.find_all('div', class_='rg_di rg_el ivg-i')
    image_alts = soup.find_all('alt')
    alt.write(str(image_alts))
    alt.write(str(image_divs))
    for div in image_divs:
        meta = json.loads(div.text)
        if 'ou' in meta:
            yield dict(file_url=meta['ou'])
    for div in image_alts:
        meta = json.loads(div.text)
        alt.write(meta)

parsernew = Parser()
parsernew.parse = funcType(parse1,parsernew)

google_crawler = GoogleImageCrawler(storage={'root_dir': 'C:/Users/79166/Desktop/флуд'})
google_crawler.parser = funcType(parse1,google_crawler)
cnt = int(input())
req = str(input())
google_crawler.crawl(keyword=req, max_num=cnt)
alt.close()