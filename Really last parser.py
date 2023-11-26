from icrawler import Crawler,Parser
from icrawler.builtin import  GoogleImageCrawler,GoogleFeeder,ImageDownloader
from bs4 import BeautifulSoup
import re
import base64
import json
alt = open("alts.txt",'r+')


class MyParser(Parser):

    def parse(self, response,**kwargs):
        soup = BeautifulSoup(response.content.decode("utf-8", "ignore"), "lxml")
        image_divs = soup.find_all(name="script")
        image_alts = soup.find_all(name='img')
        for div in image_divs:
            txt = str(div)
            if "AF_initDataCallback" not in txt:
                continue
            if "ds:0" in txt or "ds:1" not in txt:
                continue
            uris = re.findall(r"http[^\[]*?\.(?:jpg|png|bmp)", txt)
            # for image in image_alts:
            #     alt.write(str(image.get("src")))
            #     alt.write('\n')
            #     alt.write(str(image.get("alt")))
            #     alt.write('\n')
            #     div = image.get('alt', '')
            #     url = image.get('src','')
            #     alt.write(str(div))
            #     alt.write('\n')
            #     alt.write(str(url))
            #     alt.write('\n')
            # for uri in uris:
            #     alt.write(str(uri))
            #     alt.write('\n')
            for uri in uris:
                alt.write(uri)
                alt.write('\n')
            return [{"file_url": uri} for uri in uris]


class MyCrawler(GoogleImageCrawler):

    def __init__(self, *args, **kwargs):
        super(GoogleImageCrawler, self).__init__(
            feeder_cls=GoogleFeeder,
            parser_cls=MyParser,
            downloader_cls=ImageDownloader,
            *args,
            **kwargs)


google_crawler = MyCrawler(storage={'root_dir': 'C:/Users/79166/Desktop/флуд'})
cnt = int(input())
req = str(input())
google_crawler.crawl(keyword=req, max_num=cnt)
alt.close()