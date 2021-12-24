class Human:
    def p(self):
        print(f"имя : {p1.name}, age. : {p1.age}, year : {p1.year}")

a =(input("name == "))
d =(input("age == "))
p = (input("year == "))

p1=Human()
p1.name=a
p1.age=d
p1.year=p
p1.p()



class Human:
    def __init__(self,name,age,year):
        self.name = name
        self.age = age
        self.year = year
    def info(self,n):
        for i in range(n):
            print(f"имя : {self.name}, сколько лет : {self.age}, год р. : {self.year}")


a = (input("name == "))
d = (input("age == "))
p = (input("year == "))
p1 = Human(a,d,p)
p1.info(1)
