
#!Generator gives you a Iterator
def topten():
    #convert this normal function to generator using yeild 5 instead of return
    # yield 1 #return 1
    #print topten perfect squares
    n=1
    while n<=10:
        squares=n*n
        yield squares #return the value not terminate the func
        n+=1
values=topten()
# print(values.__next__())
# print(next(values))
for i in values:
    print(i)