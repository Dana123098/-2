import random
n = int(input('Vvedite kol-vo strochek'))
m = int(input('Vvedite kol-vo stolbikov'))
matrix = [[random.randint(0,9) for w in range(m)] for q in range(n)]
for a in matrix:
        print(a)
k = int(input('Номер строки'))
p = int(input('Номер столбца'))
item = [matrix[p-1][w] for w in range(n)]
item1 = [matrix[q][k-1] for q in range(m)]
print(item)
print(item1)

#2

import random
n = int(input('Vvedite kol-vo strochek'))
m = int(input('Vvedite kol-vo stolbikov'))
matrix = [[random.randint(0,9) for w in range(m)] for q in range(n)]
for a in matrix:
        print(a)
 
import random
n = int(input('Vvedite kol-vo strochek'))
m = int(input('Vvedite kol-vo stolbikov'))
matrix = [[random.randint(0,9) for w in range(n)] for q in range(m )]
for a in matrix:
        print(a)
