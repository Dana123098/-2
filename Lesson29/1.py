class Car:
    def __init__(self,mark,god,marka):
        self.mark=mark
        self.god=god
        self.marka=marka
        self.adometer=0
        
        
    def get_desk_name(self):
        print(f"Mark : {self.mark}, god : {self.god}, marka {self.marka}")
    def read_adometer(self):
        print(f"Mahina Porer imeet Adomet : {self.adometer}")
    def abd_adometer(self):
         
         if n >= self.adometer:
            self.adometer=n
            print(f"{self.adometer}")
         else :
            print("porbeg skinut nevozmozno")
    def incriment_adometer(self,m):
        self.adometer+=m
        print(f"{self.adometer}")

        
class ElectroCar(Car):
    def __init__(self,mark,god,marka,battaru):
        super().__init__(mark,god,marka)
        self.battaru=battaru
        
    def info(self):
         print(f"Mark : {self.mark}, god : {self.god}, marka {self.marka}, battaru : {self.battaru}")
    def b_p(self,b):
        self.battaru=b
        print(f"battaru have : {self.battaru}")

    def zena(self):
        if z >= 10000000:
            print("Sales!")
        else :
            print("NO!")
    
p1 = Car("zen",1999,"porer")
m=int(input("m :"))
n=int(input("n :"))
p1.adometer=23
p1.get_desk_name()
p1.read_adometer()
p1.abd_adometer()
p1.incriment_adometer(m)


p2 = ElectroCar("KKK",1999,"RAR",30)
b=int(input("b :"))
z=int(input("zenna :"))
p2.info()
p2.b_p(b)
p2.zena()
