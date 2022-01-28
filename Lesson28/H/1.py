class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        
    def describe_restaurant(self):
        print(f"Name of the restaurant : {self.restaurant_name}, type : {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is open.")

r1=Restaurant("Orlekin","sushi bar")
r1.describe_restaurant()
r1.open_restaurant()
