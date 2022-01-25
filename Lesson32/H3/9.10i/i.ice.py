from i910 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    def describe_iceCream(self):
        print(f"Name of the restaurant : {self.restaurant_name}, type : {self.cuisine_type}")
    def flavorsss(self):
        print(f"Ice cream flavors : {self.flavors}")
