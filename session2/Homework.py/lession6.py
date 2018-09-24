# part 1
print('********************')
#part 2:
n = int(input('input number : '))
for i in range(n):
 print('*',end='')
print('\n')
#part 3:
m = int(input('input number : '))
for i in range(m):
    if i%2==0:
        print('x',end='')
    else:
        print('*',end='')
print('\n')
# part4
cd = int(input('nhap chieu dai : '))
cr = int(input('nhap chieu rong : '))
for i in range(cr):
    for j in range(cd):
        print('*',end='')
    print('\n')


