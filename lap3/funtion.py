# def add( x , y):
#     r=x+y
#     return r 
# a = int(input("input a "))
# b= int(input("input b "))
# t=add(a,b)
# print(t)
# co the dien ca chuoi vao
# def eval(x,y):
#     r=x+y
#     k=x-y
#     t=x*y
#     z=x/y
#     return r,k,t,z
# a = int(input("input a "))
# b= int(input("input b "))
# eval(a,b)
# t=eval(a,b)
# print(t)
# print(type(t))
from lesson1 import *
#lesson1.seasons()
x = int(input("x = "))
y = int(input("y = "))
op = input("Op (+ - * /): ")

math = seasons(x, y, op)
print(x,y,op,math)
