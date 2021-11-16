def printing(models, class_models):
    print(models)
    while models:
        mass = models.pop()
        class_models.append(mass)
        print(class_models)
models = ["Чехол","Пенал","Ручка","Керпич"]
class_models = []
printing(models, class_models)
