
#*Print fibonacci sequence
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n<0:
        print("enter positive number")
        return
    else:
        print(a)
        print(b)
        for i in range(2,n):
            # c=a+b
            # a=b #1
            # b=c #1
            # print(a+b)
            a,b=b,a+b
            print(b)
fib(100)

#*Print fibonacci values up to 100
print('--------------------------')
def fib1(num):
    if (num<0):
        print ('invalid num')
    else:
        c=0
        d=1
        print(c)
        print(d)
        for i in range(2,num): # run upto 100
            c,d=d,c+d
            if(d<=num):
                print(d)
            else:
                break
fib1(100)


def fib2(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n<0:
        return
    else:
        print(a)
        print(b)
        for i in range(2,n):
            a,b=b,a+b
            # print(a)
            print(b)
fib2(5)