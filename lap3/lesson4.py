# from random import randint,choice
# import random

# def ran():
#     x = randint(0,10)
#     y = randint(0,10)
#     r = randint(0,90)
#     error=randint(-1,1)
#     op = choice(["+","-","*","/"])
#     s =  x + y + error
#     return x,y,r,error,s
# # a = int(input(" input a "))
# # b= int(input("input b"))
# lis = ran()
# print(lis)

from random import randint, choice
import lesson1
count = 0

def generate_quiz():
    x = randint(0, 10)
    y = randint(1, 10)
    op = ["+", "-", "*", "/"]
    op = choice(op)
    error = randint(-1, 1)
    r = lesson1.seasons(x, y, op) + error
    return [x, op, y, r, error]


    quiz = generate_quiz()
    x = quiz[0]
    y = quiz[2]
    op = quiz[1]
    r = quiz[3]
    error = quiz[4]
    print('{0} {1} {2} = {3}'.format(x, op, y, r))
    ans = input("(T/F)? ").upper()
    if error == 0:
        if ans == "T":
            print("Yay")
            
        else:
            print("nah")
            
            
    else:
        if ans == "F":
            print("Yay")
            
        else:
            print("nah")
            
            

    
