def get_even_list(l):
    new_list=[]
    for i in range(len(l)):
        if l[i] %2==0:
            new_list.append(l[i])
        else:
            print("erro")
    return new_list
    #print(new_list)
l =[2,4,6]
get_even_list(l)

