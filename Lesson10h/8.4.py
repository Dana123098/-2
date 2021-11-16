def make_shirt(size,*nazvanie):
    
    print(f"Вы выбрали такой текст, с размером {size.title()}:")
    for i in nazvanie:
        print(f"- {i.title()}")
razmer = str(input('Введите размер текста:'))
text = str(input('Введите text:'))
make_shirt("L", "I Love Python")
make_shirt(razmer, text)
