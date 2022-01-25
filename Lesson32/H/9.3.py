class User:
    def __init__(self,name,last_name,age):
        self.name=name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print(f" Name : {self.name}, Last name : {self.last_name}, age : {self.age}")
    def greet_user(self):
        print(f" {self.name} hello !")
class User_2(User):
    
   
    def describe_user(self):
         print(f" Name : {self.name}, Last name : {self.last_name}, age : {self.age}, studing")
        
    def greet_user(self):
        print(f" {self.name} hello !")
        
class Teacher(User):
    def __init__(self,name,last_name,age,crs,mark):
        super().__init__(name,last_name,age)
        self.crs=crs
        self.mark=mark
    def studing(self):
         print(f" crs : {self.crs},  mark : {self.mark} studing")
        

    def teach(self):
        print(f" Nane Teacher {self.name}, Last name : {self.last_name}, age : {self.age} - teaches")
    def greet_user(self):
        print(f"{self.name} hello !")    

u1=User("Dana","Gen",17)
u1.describe_user()
u1.greet_user()


s1=User_2("VIktopr","Malte",18)
s1.describe_user()
s1.greet_user()



t1=Teacher("Deniell","Rihter",20,5,6)
t1.describe_user()
t1.teach()
t1.studing()



