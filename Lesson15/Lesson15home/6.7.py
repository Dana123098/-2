people={
    'user_0':{
        'first_name':'Voltn',
        'last_name':'Netop',
        'age':18,
        'country':'UK'},
    'user_1':{
        'first_name':'Vania',
        'last_name':'Tsurkan',
        'age':15,
        'country':'Ukraine'},
    'user_2':{
        'first_name':'Dana',
        'last_name':'Genina',
        'age':16,
        'country':'uk'}
    }
for p, i in people.items():
    print("-"*30)
    print(f"человек под именем {p}: ")
    players_info=f"{i['first_name']} {i['last_name']}"
    age=f"Ему {i['age']}"
    country=f"Он проживает в стране: {i['country']}"
    print(f"\tИмя фамилия игрока: {players_info.title()}")
    print(f"\tВозраст: {age}")
    print(f"\tСтрана: {country}")
