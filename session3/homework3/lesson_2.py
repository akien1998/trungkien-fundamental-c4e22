import turtle,random 
from turtle import*
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
turtle.width(1)
length = 30
for i in range(5):
     color = random.choice(colors)
     turtle.forward(length)
     turtle.left(90)
     turtle.forward(70)
     turtle.left(90)
     turtle.forward(length)
     turtle.left(90)
     turtle.forward(70)
     turtle.left(90)
     length=length +30
     turtle.color(color)


    


mainloop()