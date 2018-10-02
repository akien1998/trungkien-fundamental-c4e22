# items=["lol","fifa","Pubg","GTA"]
# #items.pop(1)
# items.remove('lol')
# print(items)
items=["lol","fifa","Pubg"]
print(items)
x = input("input index hoac noi dung ban muon xoa ")
if x.isdigit():
    items.pop(int(x)+1)
    print(items)
else:
    items.remove(x)
    print(items)
print(items)