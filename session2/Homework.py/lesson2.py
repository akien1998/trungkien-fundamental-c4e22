
from turtle import *

for n in range(4):
    if n%2==0:
        for i in range(6-n):
            forward(100) 
            left(360/(6-n))
    else:
        for i in range(6-n):
            forward(100) 
            left(360/(6-n))
mainloop() 