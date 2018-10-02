
while True:
    menu=["T-Shirt", "Sweater"]
    you_want=input(" what do you want (C, R, U, D)? ")
    if you_want == "R":
        print(*menu,sep=", ")
        break
    elif you_want =="C":
        menu.append("Jeans")
        print(*menu,sep=", ")
        break
    elif you_want =="U":
        menu.insert(1,"Skirt")
        print(*menu,sep=", ")
    elif you_want=="R":
        menu.remove(2)
        print(*menu,sep=", ")
    elif you_want == "exit":
        break