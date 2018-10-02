import turtle,random
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
turtle.width(4)
for i in range(4):
    if i%2==0:
        for j in range(6-i):
            color = random.choice(colors)
            turtle.forward(100)
            turtle.left(360/(6-i))
            turtle.color(color)
    else:
        for z in range(6-i):
            color = random.choice(colors)
            turtle.forward(100)
            turtle.left(360/(6-i))
            turtle.color(color)

mainloop()


