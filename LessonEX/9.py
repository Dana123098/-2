keys = ["a", "b", "c", "d", "e", "g"]
values = [1,2,3,4,5,6]
c = {i:g for i, g in zip(keys, values)}
print(c)
for i,g in c.items():
    print(f"я знаю твой ключ {i} его значение  {g}")
