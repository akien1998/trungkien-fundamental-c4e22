a = input("Enter the string: ")
b = a.lower()

count ={}

for i in range(len(list(b))):
    if list(b)[i] == " ":
        list(b).remove(list(b)[i])
    else:    
        count[(list(b)[i])] = list(b).count(list(b)[i])

for k,v in sorted(count.items()):
    print(k,v)   