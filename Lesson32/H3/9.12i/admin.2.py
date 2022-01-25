from admin import User

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
