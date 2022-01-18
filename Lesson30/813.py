class Shop:
    def __init__(self,sope_name,store_type):
        self.sope_name=sope_name
        self.store_type=store_type
        self.numder_of_units=0
    def describ_sope(self):
        print(f"name: {self.sope_name} type: {self.store_type}  number: {self.numder_of_units}")
    def open_shop(self):
        print(f"Магазин {self.sope_name} відкрит !")
    def set_number_of_units(self):
        print(f"кoл. товару {n}")
    def incremet_number_of_units(self):
        self.numder_of_units+=m
        print(f"новое кoл. товару{self.numder_of_units}")

class Discont(Shop):
    def __init__(self,discont_products):
        self.discont_products=discont_products
    def get_discont_ptoducts(self):
        print(f"Тов. на які знижка : {self.discont_products}")
    




stor=Shop("Mirri","bar")
n=int(input("Вед. кoл. товару :"))
m=int(input("Вед. доп. кoл. товару :"))
stor.numder_of_units=n

stor.describ_sope()
stor.open_shop()
stor.set_number_of_units()
stor.incremet_number_of_units()


p2=Shop("Tax" , "textil"  )
p2.describ_sope()


store_discount=Discont("Kruppub, sausage, milk")
store_discount.get_discont_ptoducts()
