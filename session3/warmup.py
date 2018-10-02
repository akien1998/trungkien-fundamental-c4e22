
#print(yob_str.isdigit())
while True:
    yob_str=(input("enter your year of birth : ? "))
    if yob_str.isdigit():
        yob = int(yob_str)
        age = 2018 - yob
        print(age)
        break
    else:
        print('not a number')
        