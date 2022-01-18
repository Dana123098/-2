class Shop:
    def __init__(self,sope_name,store_type):
        self.sope_name=sope_name
        self.store_type=store_type
        self.numder_of_units=0
    def describ_sope(self):
        print(f"name: {self.sope_name} type: {self.store_type}  number: {self.numder_of_units}")
    def open_shop(self):
        print("Магазин {self.sope_name} відкрит !")


stor=Shop("Mirri","bar")
stor.numder_of_units=111

stor.describ_sope()
stor.open_shop()



p2=Shop("Tax" , "textil"  )
stor.number_of_units=666
p2.describ_sope()
