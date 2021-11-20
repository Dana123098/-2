players={
    'user_0':{
        'pet_name':'dogs',
        'p_name':'Mar'},
    'user_1':{
        'pet_name':'cat',
        'p_name':'Dana'},
    'user_2':{
        'pet_name':'rat ',
        'p_name':'OOl',}
    }
for p, i in players.items():
    print("-"*30)
    print(f"Игрок под именем {p}: ")
    pets=f"{i['pet_name']}"
    namt_p=f"{i['p_name']}"
    print(f"\tИмя владельца: {namt_p.title()}")
    print(f"\tживотное: {pets}")
