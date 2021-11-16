numbers=[5, 4, 15, 10, 2, 3, 7, 8, 1, 9, 13, 11, 12, 6, 14]
new=["True_2" if items%2==0 else "True_3" if items%3==0 else "False" for items in numbers]
#for i in numbers:
# if i%2==0:
# new.append('True_2')
# elif i%3==0:
# new.append('True_3')
# else:
# new.append('False')
print(new)
