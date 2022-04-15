
#?factorial in python without recursion

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=0
result=fact(n)
print(result)


def fact2(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


x=fact(5)
print(x)
