dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
c = {i:"event" if dic[i]%2==0 else "odd" for i,g in dic.items()}
print(c)
