from turtle import *

def draw_square(length,color1=""):
    for i in range(4):
        color(color1)
        forward(length)
        left(90)
        
draw_square(90,'blue')