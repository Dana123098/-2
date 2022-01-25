from aaa import User

class Admin(User):
    def __init__(self,name,last_name,age):
        super().__init__(name,last_name,age)
        self.privileges=["Allowed to add message","Allowed to delete users"]
        self.privileges=Privileges()
    
