gosti=["Alex","Beer","Linda","Renat"]
print("Gest:  " , gosti)
print(f" вы пр. на обед {gosti[0]}")


message= f" вы пр. на обед {gosti[1]}"
print(message)

message= f" вы пр. на обед {gosti[2]}"
print(message)

message= f" вы пр. на обед {gosti[3]}"
print(message)

message= f" не прий. {gosti[0]}"
print(message)

print(gosti[0])
gosti[0]= "Mari"
print(gosti)

print(f" вы пр. на обед {gosti[0]}")


message= f" вы пр. на обед {gosti[1]}"
print(message)

message= f" вы пр. на обед {gosti[2]}"
print(message)

message= f" вы пр. на обед {gosti[3]}"
print(message)

print("приг. + 2 человека ")

gosti.insert(0, "Aleksey")
gosti.insert(2, "Amir")
gosti.append("bor")
print(gosti)
message= f"на обед пр. 2 гостя  {gosti[0], gosti[1]}"
print(message)


del_item1 = gosti.pop(2)
print("мне жаль что так квышло" , del_item1)


del_item2 = gosti.pop(2)
print("мне жаль что так квышло" , del_item2)

message= f"мне жаль что так вышло {gosti[2]}"
del_item = gosti.pop(2)
print(message)

message= f"мне жаль что так вышло {gosti[2]}"
del_item = gosti.pop(2)
print(message)

message= f"мне жаль что так вышло {gosti[2]}"
del_item = gosti.pop(2)
print(message)

message= f" {gosti[0], gosti[1]} приглашение остается в силе"
print(message)
print(gosti)
del gosti[0]
del gosti[0]
print(gosti)

