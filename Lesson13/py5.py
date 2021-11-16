name_users = {"Ivan": 15, "Denis": 24, "Renat": 15, "Kirill": 49, "Nela": 18}
user_auto = {"Zhigul": 1990, "Ferrari": 2021, "Volkswagen": 2020}
about_life = [name_users, user_auto]
print(about_life)
for i in about_life:
    print(i)

empty = []
for x in range(30):
    new_item = {"Color": "gray", "Speed": 50, "Temprature": -10}
    empty.append(new_item)
    print(empty)
for f in empty[:10]:
    if f["Color"] == "gray":
        f["Color"] = "black"
        f["Speet"] = 100
        f["Temprature"] = 25
for y in empty[14:18]:
    print(y)
