import math
x = int(input("b = "))
if x>1 and x<3.2:
    y=-(1.4+x)/(math.log(x))
elif x>0 and x<=1:
    y=(x**2)-0.75
elif x<=0:
    y=(math.cos((x)**2)**3)-(math.sin((x)**2)**3)
print(y)
