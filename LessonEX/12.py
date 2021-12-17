import random
n=int(input("1= "))
m=int(input("1= "))
t=int(input("stol= "))
r=int(input("stol= "))
matrica = [[random.randint(0,9) for w in range(m)] for q in range(n)]
for f in matrica:
    print(f)
diagonal = [matrica[r][t] for r in range(n) for t in range(m) if r == t]
print(f" Diagonal :{diagonal}")
stolbec = [matrica[t-1][w] for w in range(n)]
print(f" stroka :{stolbec}")
