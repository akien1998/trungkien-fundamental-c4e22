print("Answer the folowing algebra question ")
ansewr=[35,36,40,44]
ansewr1=[55,65,75,85]
print("If x = 8 , then what is the value of 4(x+3) ?")
j= 1

for i in ansewr:
    print(j,i,sep=' . ')
    j =j+1 

x = int(input("your choice ? "))
if x == 4:
    print("Bingo")
else:
    print("False")

print("Estimate this anwser (exact calculation not needed)")
print("Jack scored these marks in 5 math tests : 49,81,72,66 and 55.What is the mean ? ")
e= 1
for k in ansewr1:
    print(e,". about ",k)
    e=e+1
a = int(input("your choice ? "))
if a ==2:
    print("Bingo")
else:
    print("flase")
print("you correctly answer 1 out of 2 questions")


