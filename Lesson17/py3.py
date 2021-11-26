import random
n=int(input("1"))
m=int(input("2"))
a = [[random.randint(0,9) for  j in range(m)] for q in range(n)]
print(a)
for t in a:
    print(f"\t{t}")
dil = [a[q][w] for q in range(n) for w in range(m) if q == w]
print(dil)
