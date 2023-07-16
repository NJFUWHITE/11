import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    r = requests.get('http://yz.njfu.edu.cn/sszs/')
    r.encoding='utf-8'
    soup=BeautifulSoup(r.text,'html.parser')

    for target in soup.find_all('script'):
        if "dataList" in target.get_text():
            print(target.get_text()[118:54174])
        



    

    