#import model_pechat
#import model_dop

#from model_pechat import Pechat
#from model_dop import Ptint

#from model_pechat import Pechat as mp
#from model_dop import Pechat as md
#from all import *

def printing(models, class_models):
    print(models)
    while models:
        mass = models.pop()

        print(class_models)
def Print(arr_pystoy):
    for text in arr_pystoy:
        print(f"Обьект {text} - напечатался")
models = ["Чехол","Пенал","Ручка","Керпич"]
class_models = []
printing(models, class_models)

