class User:
    def __init__(self,name,last_name,age):
        self.name=name
        self.last_name=last_name
        self.age=age
        self.login_attemts=0
    def describe_user(self):
        print(f" Name : {self.name}, Last name : {self.last_name}, age : {self.age}")
    def greet_user(self):
        print(f" {self.name} hello !")
    def increment_login_attemts(self):
        self.login_attemts+=1
        print(f" Login attemts : {self.login_attemts}")
    def reset_login_attemts(self):
        self.login_attemts=0
        print(f" Login attemts_2 : {self.login_attemts}")    
class User_2(User):
    
   
    def describe_user(self):
         print(f" Name : {self.name}, Last name : {self.last_name}, age : {self.age}, studing")
        
    def greet_user(self):
        print(f" {self.name} hello !")
        
class Teacher(User):
        
    def teach(self):
        print(f" Nane Teacher {self.name}, Last name : {self.last_name}, age : {self.age} - teaches")
    def greet_user(self):
        print(f"{self.name} hello !")


class Admin(User):
    def __init__(self,name,last_name,age):
        super().__init__(name,last_name,age)
        self.privileges=["Allowed to add message","Allowed to delete users"]
        self.privileges=Privileges()
    
   
class Privileges():
    def __init__(self,privileges=[]):
        self.privileges=privileges
    def show_privileges(self):
        for privel in self.privileges:
            print(f"Administrator has these privileges : {privel}")



u1=User("Dana","Gen",17)
u1.describe_user()
u1.greet_user()
u1.increment_login_attemts()
u1.reset_login_attemts()

s1=User_2("VIktopr","Malte",18)
s1.describe_user()
s1.greet_user()

t1=Teacher("Deniell","Rihter",20)
t1.describe_user()
t1.teach()

priv=Admin("Milen","Gem",19)


priv.privileges.privileges = ["Allowed to add message","Allowed to delete users"]
priv.privileges.show_privileges()



