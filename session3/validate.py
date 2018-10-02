# while True:
#     pass_word=(input("enter pass : ? "))
#     if len(pass_word)<8:
#         print("False")
#     elif pass_word.isdigit():
#         print("Flase")
#     elif pass_word.isupper():
#         print("FALSE")
#     elif pass_word.islower():
#         print("False")
#     else:
#         print("OK")
#         break
items=["lol","fifa 3","PUBG","GTA5","CS.go"]
#print(*items,sep=", ")
print(*items,sep="\n")
while True:
    i = int(input("enter ? "))
    if i <len(items):
        print(items[i-1])
        break
    else:
        print("False")

