class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person created")
    def info(self):
        print(f" Name : {self.name}, age : {self.age}")
    def hello(self):
        print(f"{self.name} seys hello")
class Student(Human):
    def __init__(self,name,age,crs,mark):
        super().__init__(name,age)
        #Human.__init__(self,name,age)
        self.crs=crs
        self.mark=mark
    def studing(self):
         print(f" crs : {self.crs},  mark : {self.mark} studing")
        
   
    def study(self):
         print(f"Name Student : {self.name}, age : {self.age}, studing")
        
    def hello(self):
        print(f"Student cr {self.name} emu {self.age}")
        
class Teacher(Human):
    def teach(self):
        print(f" Nane Teacher {self.name}, age : {self.age} - teaches")


s1=Student("Vlad",18,3,5)
s1.info()
s1.study()
s1.hello()
s1.studing()

t1=Teacher("Den", 24)
t1.info()
t1.teach()
t1.hello()


