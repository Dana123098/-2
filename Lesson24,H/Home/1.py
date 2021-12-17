class Human:
    def __init__(self,name,surname,place_of_birth,age,year):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.age = age
        self.year = year
    
    
    def info(self,n):
        for i in range(n):
            print(f"имя : {self.name}, порода : {self.surname}, place_of_birth : {self.place_of_birth}, age {self.age}, year {self.year}")

p1 = Human("Seren", "Неизвестно", "UK", 3, 2019)

p1.info(1)


class Human:
    def __init__(self,name):
        self.name = name
        
    
    def info(self,n):
        for i in range(n):
            print(f"история : {self.name}")

p2 = Human("Увидели возле реки когда шли на дачу . После нескольких встреч решили забрать домой . ")

p2.info(1)



