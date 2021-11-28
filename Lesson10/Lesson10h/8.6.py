def describe_city(size,*nazvanie):
    
    print(f"Вы ввели город {size.title()}, старна:")
    for i in nazvanie:
        print(f"- {i.title()}")
gorod = str(input('Введите город:'))
strana = str(input('Введите страну:'))
describe_city(gorod, strana)

