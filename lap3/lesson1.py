# x = int(input(" input x : "))
# y = int(input(" input y : "))
# s = x + y
# print("{0} + {1} = {2}".format(x,y,s))
#part 2
# x = int(input(" input x : "))
# y = int(input(" input y : "))
# s = input("*,-,/,+ : ")
# try:
#     if s=='*':
#         x_y = x*y
#         print("x_y = ",x_y)
#     elif s== '-':
#         x_tru_y= x-y
#         print("x_tru_y = ",x_tru_y)
#     elif s=='/':
#         if y == 0:
#             print("khong thuc hien dc phep chia")
#         x_chia_y= x/y
#         print("x_chia_y = ",x_chia_y)
#     elif s=='+':
#         x_cong_y= x+y
#         print("x_cong_y",x_cong_y)
    
# except ValueError:
#         print("Oops!  That was no valid number.  Try again...")   
def seasons(x, y, op):
    if op == "-" :
        return  x - y
      
    elif op == "+":
        return  x + y
     
    elif op == "*":
        return  x*y
       
    elif op == "/":
        return  x/y
      
    else:
        exit()

x = int(input("x = "))
y = int(input("y = "))
op = input("Op (+ - * /): ")
math = seasons(x, y, op)
print(math)
# ngat ham 