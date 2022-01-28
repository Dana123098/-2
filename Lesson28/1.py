class Human:
    def __init__(self,name,surname,br_of,year_of_b):
        self.name=name
        self.surname=surname
        self.br_of=br_of
        self.year_of_b=year_of_b
    def info(self):
        print(f"Name:{self.name}, F: {self.surname}, {self.br_of}, {self.year_of_b}")
    def year(self,years):
        return years-self.year_of_b


p1=Human("Dana","Genina","UR",2004)
p1.info()
print(p1.year(2022))

p2=Human("Nel","Genina","UR",2004)
p2.info()
        
