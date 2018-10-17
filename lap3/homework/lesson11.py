def is_inside(x=[],y=[]):
    if 140<= x[0] <= 240 and 60<= x[1]<=260:
        print("true")
        return True
    else:
        print("false")
        return False

x=[40,56]
y =[140, 60, 100, 200]
is_inside(x,y)
