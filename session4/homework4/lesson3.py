print("Answer the folowing algebra question ")
ansewr=[35,36,40,44]
print("If x = 8 , then what is the value of 4(x+3) ?")
j= 1
while True:
    for i in ansewr:
        print(j,i ,sep=' . ')
        j =j+1 
    x = int(input(" your choice ? "))
    if x == 4:
        print("Bingo")
        break
    
    else:
        print("False")