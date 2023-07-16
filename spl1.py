import requests
from bs4 import BeautifulSoup
import re
import json
import pprint


class Base:
    def __init__(self, school_name, url):
        self.school_name = school_name
        self.url = url

    def get_html(self):
        r = requests.get(self.url)
        self.html = r.text

    def get_info(self):
        pass

    def write_file(self):
        pass

    def run(self):
        self.get_html()
        self.get_info()
        self.write_file()


class NJUBase(Base):
    def __init__(self, school_name, url):
        super().__init__(school_name, url)
        self.l = []

    def get_html(self):
        r = requests.get(self.url)
        self.html = r.text

    def get_info(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        for target in soup.find_all('li', class_="news"):
            self.l.append("http://yzb.nju.edu.cn"+target.contents[1].contents[0]["href"]+"," +
                          target.contents[1].contents[0]["title"]+","+target.contents[3].get_text()+"\n")

    def write_file(self):
        f = open(self.school_name+".csv", 'w')
        for row in self.l:
            f.write(row)
        f.close()






if __name__ == "__main__":

    nju=NJUBase("nju","http://yzb.nju.edu.cn/47862/list.htm")
    nju.run()

    #r = requests.get('http://yzb.nju.edu.cn/47862/list.htm')
    #soup = BeautifulSoup(r.text, 'html.parser')
    #f = open("nju.csv", 'w')
    #for target in soup.find_all('li', class_="news"):
     #   print("http://yzb.nju.edu.cn"+target.contents[1].contents[0]["href"],
     #         target.contents[1].contents[0]["title"], target.contents[3].get_text())
     #  print("=====================================")
#
#        f.write("http://yzb.nju.edu.cn"+target.contents[1].contents[0]["href"]+"," +
#                target.contents[1].contents[0]["title"]+","+target.contents[3].get_text()+"\n")
#
#    f.close()
