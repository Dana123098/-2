#numbers=[8, 64, 999, 541, 6548, 84, 654, 4849, 3, 5, 1, -3]
#empty=[items for items in numbers if items>25 if items%2==0]  
#print(empty)
#больше 25 и нацело бел. на 2


#print(empty)
#for i in numbers:
#    empty.append(i+1)
#print(numbers)
#print(empty)



#numbers=[8, 64, 999, 514, 6548, 84, 654, 4849, 3, 5, 1, -2]
#empty=[items for items in numbers if items>25 and items%2==0]
#print(empty)

#print(empty)
#for i in numbers:
# empty.append(i+1)
#print(numbers)
#print(empty)


numbers=[5, 4, 15, 10, 2, 3, 7, 8, 1, 9, 13, 11, 12, 6, 14]
new=[items if items>4 else 'False' for items in numbers]
#for i in numbers:
# if i>4:
# new.append(i)
# else:
# new.append('False')
print(new)
