from poll import Poll
import string
import mlab
from random import choice

#1: ket noi vs database

mlab.connect()

# 2: preare chuan bi data
q = "vu"
opts = "kien"
re="Subline"
alphabet="abcdefghijklmnopqrstuvwxyz".upper()
c =""
for _ in range(6):
    c+= choice(alphabet)

# 3 : tao documant
p = Poll(first=q,last= opts,coure=re,code=c )
#4 luu
p.save()
