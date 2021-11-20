players={
    'Python':{
        'определение':'Python представляет собой открытый язык программирования, созданный в конце 1980х годов Гайдо ван Россумоми представленный в 1991. Впервые он был встроен в ArcGIS 9.0 и тех пор стал наиболе актуальным выбором для пользователей, создающих рабочие процессы геообработки'},
    'Class':{
        'определение':'A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.'},
    'Class variable':{
        'определение':'A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the classs methods. Class variables are not used as frequently as instance variables are.'},
    'Data member':{
        'определение':'A class variable or instance variable that holds data associated with a class and its objects.'},
    'Function overloading':{
        'определение':'The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.'}
    }
for p, i in players.items():
    print("-"*30)
    print(f"{p}: ")
    age=f"{i['определение']}"
    print(f"\t{age}")


