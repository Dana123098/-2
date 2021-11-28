people={
    'user_0':{
        'first_name':'Dana',
        'last_name':'Genina',
        'age':16,
        'country':'UK'},
    }
for p, i in people.items():
    print("-"*30)
    print(f"человек с именем {p}: ")
    players_info=f"{i['first_name']} {i['last_name']}"
    age=f"Ему {i['age']}"
    country=f"Он проживает в стране: {i['country']}"
    print(f"\tИмя фамилия: {players_info.title()}")
    print(f"\tВозраст: {age}")
    print(f"\tСтрана: {country}")


