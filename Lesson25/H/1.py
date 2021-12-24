class Circle:
    PI = 3.14
    C_V=0
    def __init__(self,radius):
        self.radius = radius
        Circle.C_V+=1
    def len_Circle(self):
        
        print(f" l = {2*self.PI*self.radius}")
    def square(self):
        print(f" S = {self.PI*self.radius**2}")

        
a=int(input("ved :"))        
c1=Circle(a)
c1.len_Circle()
p=Circle.C_V
print(p)


c2=Circle(a)    
c2.square()


print(p)


#
class Circle:
    def __init__(self,katet):
        self.katet = katet
        
    def len_Circle(self,katet_t):
        self.katet_t = katet_t
    def square(self):
        print(f" S = {self.katet**2 +self.katet_t**2}")

        
a=int(input("ved :"))
b=int(input("ved :"))
c1=Circle(a)



c2=Circle(a)    
c2.square()


print(p)




#


class Tringle:
    import math
    def hypotenuse(a, b):
        return math.sqrt((a**2) + (b**2))
    print(a, b)
    

a=int(input("ved :"))        
c1=Circle(a)
c1.len_Circle()
p=Circle.C_V
print(p)


c2=Circle(a)    
c2.square()

    


