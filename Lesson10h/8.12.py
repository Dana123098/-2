def sandvich(*nazvanie):
    
    print(f"Вы выбрали такие ингредиенты :")
    for i in nazvanie:
        print(f"- {i.title()}")
        

ingridientu = str(input('Введите ингредиенты:'))
ingridientu2 = str(input('Введите ингредиенты:'))
ingridientu3 = str(input('Введите ингредиенты:'))

sandvich(ingridientu, ingridientu2, ingridientu3)


