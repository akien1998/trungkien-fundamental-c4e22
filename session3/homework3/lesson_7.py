items=[5,7,300,90,24,50,75]
print(*items,sep=", ")
items[2]=8
print(*items,sep=", ")
for i in range(len(items)):
    items[i] += 50
print("One month has passed ,now here is my flock")
print(*items)

     