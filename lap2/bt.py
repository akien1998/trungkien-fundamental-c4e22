from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url ="https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
suop = BeautifulSoup(webpage_text,"html.parser")
ul = suop.find("div","section-content")
li_list = ul.find_all("ul")
new_list =[]
for li in li_list:
    a=li.a
    #title=a.string
    link =url + a["href"]
    img = a.img
    h4=li.h4
    h4 = li.h4
    title = h4.string
    news = {
        "title":title,
        "link":link,
        "img":img
    }
    new_list.append(news)
pyexcel.save_as(records=new_list,dest_file_name="music.xls")