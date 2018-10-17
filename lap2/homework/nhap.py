from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)# mo ket noi
raw_data= conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text,"html.parser")
tab = soup.find("table",id="tableContent")
tr_class = tab.find_all("tr")
#print(li_list)
new_list=[]
for tr in tr_class: