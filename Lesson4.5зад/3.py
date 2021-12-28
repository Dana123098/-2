import math
x=int(input("x= "))
if x>0 and x<2:
    y=x*math.sqrt(abs(x-5.4))
elif x>=2 and x<8:
    y=math.atan(x**2)
elif x>=8:
    y=math.log10(abs(x-7.8))
print(y)
    
