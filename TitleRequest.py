from bs4 import BeautifulSoup
import requests
f = open("alts.txt","r+")
c = open("keywords.txt",'r+')
for url in f:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        div = soup.get("Title")
        print(str(div),url)
    except:
        continue
    #print(soup)
f.close()
c.close()