#def den ():
    #t = f"renat"
    #yield t     #перебор   
#y = den()
#print(y)  



list_my = ["a", "s", "d", "f", "g"]
def gen():
    for i in list_my:
        yield i
y = gen()
print(next(y))
print(next(y))
print(next(y))
print(next(y))






























   
