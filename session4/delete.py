person ={
    "name":"quan",
    "age" : 20,
}
#nhap =['D','V']
# del person["age"]
print(person)
while True:
    print("ban muon gi xoa la D cn lai la V")
    x=input("input V or D : ")
    if x=='V':
        text =input("input : ")
        pair =text.split(",")
        key = pair[0]
        value= pair[1]
        person[key]=value
        print(person)
        break
    elif x=='D':
        y = input("input key : ")
        del person[y]
        print(person)
        break
    # theem cai check

