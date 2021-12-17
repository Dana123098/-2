list_1=(4,16, 64, 256)
def gen():
    for i in list_1:
        yield i
y=gen()
g=0
while g<len(list_1):
    print(next(y))
    g+=1



#a=[4,16, 64, 256]
#b=(i**(1/2)for i in a)
#print(next(b))
#выв. корни кв.
