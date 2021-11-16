def Pechat(arr_models, arr_pystoy):
    while arr_models:
        title = arr_models.pop(0)
        arr_pystoy.append(title)
        print(arr_pystoy)
def Print():
    for text in arr_pystoy:
        print(f"Обьект {text} - напечатался")
