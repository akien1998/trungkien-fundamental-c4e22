person ={
    "name":"quan",
    "age" : 20,
}
user = input("input key : ")
if user in person:
    x = person[user]
    print(x)
else:
    print("not found")