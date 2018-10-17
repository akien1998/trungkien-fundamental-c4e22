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
    a_dict= {}
    td = tr.find_all("td")
    if len(td) is not None:
        for i in range(len(td)):
            if td[0].string is not None:
                a_dict = {
                    "<Truoc Sau>" : td[0].string.replace("\n" , ""),
                    "Quý 4-2017" : td[1].string,
                    "Quý 1-2017" : td[2].string,
                    "Quý 2-2017" : td[3].string ,
                    "Quý 3-2017":  td[4].string
                }
    new_list.append(a_dict)

print(new_list)
pyexcel.save_as(records=new_list, dest_file_name="new_file.xlsx")
    
