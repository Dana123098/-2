n=int(input("a = "))
p=0.5
s=0
for i in range(1, n+1):
    s+=p
    p/=2
    print(s)
print(s)
    
