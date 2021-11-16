name_users = {"Ivan": 15, "Denis": 24, "Renat": 15, "Kirill": 49, "Nela": 18}
user_auto = {"Zhigul": 1990, "Ferrari": 2021, "Volkswagen": 2020}
#data_user = name_users.copy()
#data_user.update(user_auto)
data_user = name_users|user_auto
print(data_user)
name_users|user_auto
print(name_users)

c = name_users.keys()
print(c)
for a in c:
    print(a)
value = name_users.values()
for x in name_users.values():
    print(x)
    
for s, y in name_users.items():
    print(f"Ключи: {s}, значения: {y}]")

abc = name_users.get("Denis", "User not founded")
print(abc)

name_users.clear()
print(name_users, "Game over")
l = len(user_auto) # длнна словоря
print(l)
