list_1=[5, 7, 21, 37, 51, 8]
a=list(filter(lambda x:x%2==0, list_1))
print(a)


#выв. чотные. числа
#filter(функция, обьект)
#(filter(lambda x:x%2==0, list_1))
#или вместо lambda пишем def()
