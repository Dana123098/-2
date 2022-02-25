#1


#import math


#class circle():
#   def __init__(self, radius):
#        self.radius = radius

#    def area(self):
#        return math.pi * (self.radius ** 2)

#    def perimeter(self):
#        return 2 * math.pi * self.radius


#r = int(input("r: "))
#obj = circle(r)
#print("S:", round(obj.area(), 2))
#print("L:", round(obj.perimeter(), 2))

#2

#n=int(input("password: "))
#if n == 1209:
#    print("OK")

#elif n < 4:
#    print("Не тот!")

#else:
#    print("Enter in numbers ")

#3
#n=int(input("enter your age : "))
#if n>=18 and n<=24:
#    print("Ok . You can get a loan !")
#elif n<=17:
#    print("You are too young")
#else:
#    print("Are you sure you are a student? ")

#4
#n=int(input("Enter the amount of your points : "))
#if n<=100 and n>=90:
#    print("You are cool. Your rating is 12")
#elif n<=90 and n>=80:
#    print("Not bad . Your rating is 9")
#elif n<=80 and n>=70:
#    print("Not bad . Your rating is 8")
#elif n<=70 and n>=60:
#    print("Not bad . Your rating is 7")
#elif n<=60 and n>=50:
#    print("Not bad . Your rating is 6")
#else:
#    print("Your score is not good. No big deal, you can redo it!")

#5
#import math
#x=int(input("x : "))
#y=int(input("y : "))

#if x > y:
#    z = math.sqrt(abs(x * y))
#    print(z)
#else:
#    z =(math.log(x+y))
#    print(z)

#6
#n=int(input("Enter how many degrees  : "))
#if n<=49 and n>=20:
#    print("air conditioning on")
#elif n<=19 :
#    print("air conditioning off")
#elif n>=50:
#    print("You are alive? ")

#7
#def abc(n):
#    if n%2==0:
#       print("2")
#    else:
#       print("1")
#n=int(input())
#abc(n)

#8
#a=int(input("a:"))
#b=int(input("b:"))
#c=int(input("c:"))
#def triugol(a,b,c):
#     if a+b>c:
#        print("Существует")

#     else:
#         print("Error")


#triugol(a,b,c)

#9
#x=int(input("x : "))
#y=int(input("y : "))
#if x>=1 and y>=1:
#    print("1")
#elif x<0 and y>=1:
#    print("2")
#elif x<0 and y<0:
#    print("3")
#elif x>=1 and y<0:
#    print("4")

#10
import math
x = int(input("x = "))
if x>0:
    y = 2*x-10
elif x==0:
    y=0
elif x<0 :
    y=2*math.sqrt(abs(x))-1
else :
    print("aro")
print(y)