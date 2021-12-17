class Human:
    def __init__(self,name,surname,place_of_birth,age,year):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.age = age
        self.year = year
    
    
    def info(self,n):
        for i in range(n):
            print(f"имя : {self.name}, фам. : {self.surname}, place_of_birth {self.place_of_birth}, age {self.age}, year {self.year}")

p1 = Human("Den", "Dmitriev", "UK", 24, 1997)
#p1.name = "Dana"
#p1.surname = "Genina"
#p1.place_of_birth = "UK"
#p1.rez_year = 2004

p2 = Human("Dana", "Genina", "UK", 16, 2004)
#p2.name = "Nela"
#p2.surname = "Genina"
#p2.place_of_birth = "UK"
#p2.rez_year = 2004



p1.info(1)
p2.info(1)

