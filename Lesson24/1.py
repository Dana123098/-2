#class Human:
    #name: Den
    #surname: Dmitriev
    #age: 24
    #place_of_birth: UK

#
class Human:
    def info(self,n):
        for i in range(n):
            print(f"имя : {self.name}, фам. : {self.surname}")
        
    


p1 = Human()
p1.name = "Dana"
p1.surname = "Genina"
p1.place_of_birth = "UK"

#print(p1.name)
#print(f"имя : {p1.name}, фам. : {p1.surname} ")
p2 = Human()
p2.name = "Nela"
p2.surname = "Genina"
p2.place_of_birth = "UK"

#print(f"имя : {p2.name}, фам. : {p2.surname} ")




p1.info(5)
p2.info(3)



