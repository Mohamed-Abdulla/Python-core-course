

a=10

def something():
    #*to use global variable inside local scope and redefine it 
    global a
    a=15
    print(a)
something()
print(a)


def something1():
    #?to use same name local variable and also re-assign global variable
    a=9
    x=globals() ['a']
    print(a)
    globals()['a']=15
something1()
print(a)