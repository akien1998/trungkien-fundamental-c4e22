from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#bs4 là thư viện 
# 1 dowload web ấy về
#1.1 kết nối với trang web đáy 
url = "https://dantri.com.vn"
conn = urlopen(url)# mở kết nối
#1.2 dowloaw dữ liệu về
raw_data = conn.read()# tải dữ liệu về
# 1.3 giải mã dữ liệu
webpage_text = raw_data.decode("utf-8")
# 1.4 lưu filef 
# f = open("dantri.html","wb")
# f.write(raw_data)
# f.close()
# print(len(webpage_text))
# # 2 tach ra đc vùng ROI
#2.1 convert text thanh suop
suop = BeautifulSoup(webpage_text,"html.parser")
print(suop.prettify())# bieets ther mwor nafo uwnsg vs ther ddongs naof 
ul = suop.find("ul","ul1 ulnew")

li_list = ul.find_all("li")
# for li in li_list:
#     print(li)
#     print("**********************************")
# print(li_list)
# print(type(li_list))
# li = li_list[0]
new_list =[]
for li in li_list:
  
    h4 = li.h4
    # print(h4)
    a = h4.a
    # print(a)
    title = a.string
    link =url + a["href"]# day la dict
    # print(title)
    # print(link)
    news = {
        "title":title,
        "link":link,
    }
    new_list.append(news)
    
print(new_list,sep="\n************")
pyexcel.save_as(records=new_list,dest_file_name="dan_tri.xls")
# a =li.h4.a
# # 3 tách đc cái data mình cần
# # save data

 