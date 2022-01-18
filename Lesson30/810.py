class Ractangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def the_area_of_the_rectangle(self):
        self.width*self.length
        print(f"Площа прямокутника == {self.width*self.length}")

        
p1=Ractangle(2,3)
p1.the_area_of_the_rectangle()
        
        
