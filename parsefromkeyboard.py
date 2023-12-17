from icrawler.builtin import  GoogleImageCrawler,GoogleFeeder,GoogleParser,ImageDownloader
from icrawler import downloader
from urllib.parse import urlparse
import pandas as pd
import os
os.chdir("C:/Users/79166/Desktop/флуд")




class MyDownloader(ImageDownloader):
    def get_filename(self, task, default_ext):
        url_path = urlparse(task["file_url"])[2]
        extension = url_path.split(".")[-1] if "." in url_path else default_ext
        file_idx = req +str(self.fetched_num)
        return f"{file_idx}.{extension}"


req = input()
if not os.path.isdir(req):
     os.mkdir(req)
path = 'C:/Users/79166/Desktop/флуд/'+req
crawler = GoogleImageCrawler(downloader_cls=MyDownloader, storage={'root_dir': path})
crawler.crawl(max_num=10, keyword=req)