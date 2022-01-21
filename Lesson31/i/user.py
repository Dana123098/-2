from priv import User


class Admin(User):
    def __init__(self,first_name,last_name,age,year):
        super().__init__(first_name,last_name,age,year)
        self.privileges=[]
        self.privileges=Privileges()
    
    def describe_admin(self):
        print("Information about the admin :")
        print(f"First name : {self.first_name} Last name : {self.last_name} age : {self.age} year : {self.year}")
    

class Privileges():
    def __init__(self,privileges=[]):
        self.privileges=privileges
    def show_privileges(self):
        for privel in self.privileges:
            print(f"Administrator has these privileges : {privel}")

                
