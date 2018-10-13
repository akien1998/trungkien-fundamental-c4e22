from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)# mo ket noi
raw_data= conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text,"html.parser")
sec= soup.find("section","section chart-grid")
#print(sec)
li_list = sec.find_all("li")
print(li_list)
new_list=[]
for li in li_list:
    h3 = li.h3
    a = h3.a
    songs_names = a.string
    h4 = li.h4
    a = h4.a
    
    artists = a.string
    news ={
        "artists":artists,
        "songs_name":songs_names,
    }
    new_list.append(news)
    pyexcel.save_as(records=new_list,dest_file_name="iTunes_Charts.xlsx")