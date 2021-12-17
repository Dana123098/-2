a=int(input("вед. число : "))
b=int(input("вед. число : "))
s = lambda a,b:a*b
x = lambda a,b:a%b
r = lambda a,b:a+b
m = lambda a,b:a**b
n = lambda a,b:b/a
print(s(a,b))
print(x(a,b))
print(r(a,b))
print(m(a,b))
print(n(a,b))
