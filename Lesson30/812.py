class Stroki:
    def __init__(self,strok):
        a = input("Вед. слово : ")
        self.strok=a
    def otr_stroku(self):
        print(f"{self.strok}")
    def s_up_reg(self):
       print(f"{self.strok.upper()}")

p1=Stroki("ddd")
p1.otr_stroku()
p1.s_up_reg()
