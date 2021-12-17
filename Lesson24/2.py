class Human:
    def info(self,m):
        print(m-self.rez_year)
    


p1 = Human()
p1.name = "Dana"
p1.surname = "Genina"
p1.place_of_birth = "UK"
p1.rez_year = 2004
#print(p1.name)
#print(f"имя : {p1.name}, фам. : {p1.surname} ")
p2 = Human()
p2.name = "Nela"
p2.surname = "Genina"
p2.place_of_birth = "UK"
p2.rez_year = 2004
#print(f"имя : {p2.name}, фам. : {p2.surname} ")


a=int(input("ved god r."))

p1.info(2021)

p2.info(2021)

