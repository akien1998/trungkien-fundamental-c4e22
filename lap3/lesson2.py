# from random import randint
# import random
# x = randint(0,10)
# y = randint(0,10)
# r = randint(0,90)
# error=randint(-1,1)
# s = x+y + error
# g= x*y + error
# z=x -y +error
# p =x /y +error
# toan_tu = ["*","/","+","-"]
# random.choice(toan_tu)
# ured= input("Y/N ? ")

# if error ==0:
#     if ured=='Y':
#         print("true")
#     elif ured=='N':
#         print("fail")
    
    
from random import randint
import random
import lesson1 im
x = randint(0,10)
y = randint(0,10)
r = randint(0,90)
error=randint(-1,1)
s =  x + y + error
#op = choice(['+','-','*','/'])

ured= input("Y/N ? ").upper()
if error ==0:
    if ured =='Y':
        print("dung")
    else:
        print("sai")
else:
    if ured=='Y':
        print("sai"):
    else:
        print("dung")