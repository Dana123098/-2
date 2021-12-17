b = []
while True:
    vop_1 = str(input('Введите  имя :'))
    
    if vop_1 == 'stop':
            break
    else:
        b.append( vop_1)
print(f"Поздравляю, Вы зарегестрированы, {b}")
