import math
x = int(input("x= "))
y = int(input("y= "))
if abs(x*y)<1 and x<0:
    y= x+y/math.e**x*y
elif 2<x and y<=0:
    y=-(math.log(x))**2
elif y>0 and x>=0 and x<=2:
    y=math.log10(math.sqrt(y))
else:
    print("error")
print(y)
    


