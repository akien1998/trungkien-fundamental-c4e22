print("hello , my name is kien and here is my flock")
items=[5,7,300,90,24,50,75]
print(*items,sep=", ")

print("now my biggest sheep has size 300 let's shear it After shearing ,here is my flock")
items[2]=8
print(*items,sep=", ")

# Month1:
print("Month 1")
for i in range(len(items)):
    items[i] += 50
print("One month has passed ,now here is my flock")
print(*items,sep=", ")
print("now my biggest sheep has size 140 let's shear it After shearing ,here is my flock")
items[3]=8
print(*items,sep=", ")

#Month2:
print("Month2")
for i in range(len(items)):
    items[i] += 50
print("One month has passed ,now here is my flock")
items[3]=58
print(*items,sep=", ")
print("now my biggest sheep has size 190 let's shear it After shearing ,here is my flock")
items[-1]=8
print(*items,sep=", ")
# month 3
print("Month3")
sum = 0
for i in range(len(items)):
    items[i] += 50
print("One month has passed ,now here is my flock")
for i in range(len(items)):
    sum = sum + items[i] 
print("my flock has size in total : ",sum)
money = sum * 2
print("I would get 1010 *2$ = ",money,"$")

