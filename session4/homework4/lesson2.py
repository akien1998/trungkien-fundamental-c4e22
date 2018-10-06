prices ={
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3,
}
stock={
    'banana':6,
    'apple':0,
    'orange':32,
    'pear':15,
}
print(stock['banana'])
#part 1
for i in prices.keys():
    print(i)
    print("price: ",prices[i])
    print("stock: ",stock[i])
#part 2
print("part 2\n")
taotal = 0
for i in prices.keys():
    print(i)
    print("price: ",prices[i]*stock[i])
    #print("stock: ",stock[i])
    taotal = taotal + (prices[i]*stock[i])
print("total = ",taotal)
