import random
n = int(input('Vvedite kol-vo strochek'))
m = int(input('Vvedite kol-vo stolbikov'))
matrix = [[random.randint(0,9) for w in range(m)] for q in range(n)]
for a in matrix:
        print(a)
diagonal = [matrix[w][q] for w in range(n) for q in range(m) if w==q]
print('Главная диагональ ===>',diagonal)
k = int(input('Номер строки'))
p = int(input('Номер столбца'))
item = [matrix[k-1][w] for w in range(m)]
item1 = [matrix[q][p-1] for q in range(n)]
print(item)
print(item1)
r = int(input('Номер строки элемента'))
t = int(input('Номер столбца элемента'))
item2 = matrix[r-1][t-1]
print(item2)



#Создать матрицу, в которой вывести основную матрицу,
#а после вывести матрицу,
#в которой все строки стали столбцами
