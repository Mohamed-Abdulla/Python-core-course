
#*divide only a is bigger than b.if not swap it then div
def div(a,b):
    print(a/b)

#*decorators -add extra func to existing func
def smart_div(div):
    def inner(a,b): #this func change code in orginal func by return
        if a<b:
            a,b=b,a
        return div(a,b)
    return inner
div=smart_div(div) #passing orginal func 
div(2,4)


