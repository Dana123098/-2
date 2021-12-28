import math
x = int(input("b = "))
if 1<=x:
    y=math.e**(-abs(x))
elif abs (x)<1:
    y=math.log10*math.sqrt(1-x**2)
elif x<=-1:
    y=math.atan(x)
print(y)
