class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_restaurant(self):
        print(f"Name of the restaurant : {self.restaurant_name}, type : {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is open.")
    def set_number_served(self):
        print(f"Number of visitors :  {self.number_served}")
    def increment_number_served(self):
        self.number_served+=m
        print(f"Number of visitors + increment:  {self.number_served}")    
        
restorant=Restaurant("Orlekin","sushi bar")
n=int(input("Вед. number of visitors : "))
m=int(input("Вед. plus new number of visitors . : "))
restorant.number_served=n
restorant.describe_restaurant()
restorant.open_restaurant()
restorant.set_number_served()
restorant.increment_number_served()
