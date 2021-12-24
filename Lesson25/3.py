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





