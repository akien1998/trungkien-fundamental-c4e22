from poll import Poll
import string
import mlab
from random import choice

#1: ket noi vs database

mlab.connect()

# 2: preare chuan bi data
q1 = "Hackathon an gi ?"
q2 = "Sau demo day di dau ?"
q3 = "Sao cua Linh chua chay"
alphabet="abcdefghijklmnopqrstuvwxyz".upper()
c =""
for _ in range(6):
    c+= choice(alphabet)

# 3 : tao documant
p = Poll(question1=q1,question2= q2,question3=q3,code=c )
#4 luu
p.save()
