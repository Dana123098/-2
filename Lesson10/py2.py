def pizza(*nazvanie):
    print(f"вы выбрал такую пицу ===> {nazvanie}")
    for i in nazvanie:
        print(f"- {i.title()}")
    
pizza("gavai")
pizza("peperoni", "4sira", "mysna")
