prompt = "\nвед. возраст:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    voz = input(prompt)

    if voz == 'quit':
        break
    elif a>=3 and a<=12:
        print("цена=1o$")
    else:
      print("цена=15$")
