print("hello , my name is kien and here is my flock")
items=[5,7,300,90,24,50,75]
# Month1:
for i in range(len(items)):
    items[i] += 50
print("One month has passed ,now here is my flock")
print(*items,sep=", ")

#Month2:
for i in range(len(items)):
    items[i] += 50
print("One month has passed ,now here is my flock")
items[2]=58
print(*items,sep=", ")
print("now my biggest sheep has size 190 let's shear it After shearing ,here is my flock")
items[2]=58
items[3]=8
print(*items,sep=", ")
#Month3:
for i in range(len(items)):
    items[i] += 50
print("One month has passed ,now here is my flock")
print(*items,sep=", ")
print("now my biggest sheep has size 190 let's shear it After shearing ,here is my flock")
items[6]=8
print(*items,sep=", ")