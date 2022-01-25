class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        
    def describe_restaurant(self):
        print(f"Name of the restaurant : {self.restaurant_name}, type : {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is open.")
class Restaurant_2(Restaurant):
    def describe_restaurant_2(self):
        print(f"Name of the restaurant : {self.restaurant_name}, type : {self.cuisine_type}")
    
class Restaurant_3(Restaurant):
     def describe_restaurant_3(self):
        print(f"Name of the restaurant : {self.restaurant_name}, type : {self.cuisine_type}")
    

r1=Restaurant("Orlekin","sushi bar")
r1.describe_restaurant()
r1.open_restaurant()
r2=Restaurant_2("bUUT","Bar")
r2.describe_restaurant_2()
r3=Restaurant_3("Muri","Fish")
r3.describe_restaurant_3()
