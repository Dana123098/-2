

#sqrt- извлечь корень.
#sqrt сокращение от square root (квадратный корень).


import math
class Pit :
    print("c - гипотенуза a b - катеты")
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def s_c(self):
        if a>b:
            print(f" if gep a={a}, kat b={b} kat c = {math.sqrt((self.a**2)-(self.b**2))}")
        else:
            print("a mast be > b")
    def s_b(self):
        print(f" if gep a={a}, kat b={b} kat c = {math.sqrt((self.a**2)+(self.b**2))}")

a= int(input('a : '))
b= int(input('b : '))
c1=Pit(a,b)
c1.s_c()

c2=Pit(a,b)
c2.s_b()

        
        

#
from math import sqrt
print("c - гипотенуза a b - катеты")
choice = input('выберете сторону которую будете искать(a, b, c)')
if choice =='c':
	side_a = int(input('a: '))
	side_b = int(input('b: '))
	side_c = sqrt(side_a ** 2 + side_b ** 2)
	
	print('c == : ' )
	print(side_c)
elif choice =='a':
    side_b = int(input('b: '))
    side_c = int(input('c: '))
    
    side_a = sqrt((side_c ** 2) - (side_b ** 2))
    
    print('a == :' )
    print(side_a)
elif choice =='b':
    side_a = int(input('a: '))
    side_b = int(input('c: '))
        
    side_c = sqrt(side_c ** 2 - side_a ** 2)
    
    print('b == :')
    print(side_c)

