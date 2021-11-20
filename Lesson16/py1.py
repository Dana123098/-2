qwe = [3,2,1]
zxc = [1,2,3]
asd = [(i, n) for i in qwe for n in zxc ]
print(asd)
for z in asd:
    print(z)



qwe = [3,2,1]
zxc = [1,2,3]
asd = []
for i in zxc:
    for n in qwe:
        asd.append((i, n))
print(asd)
for z in asd:
    print(z)


import random
numbers = [random.randint(1,1000000) for i in range(1,30)]
print(numbers)
for n in numbers:
    if n%2==0:
        print(n)
    else:
        print('kirill lox')
