
#-define once and call multiple add 2nos
def greet():
    print("Hello")
    print("good morning")

greet()

def add(a,b):
    print(a+b)
add(4,5)
#!2 types of func choice
#when u call a function, a function will do a task for you

# return the value ,when we ask something from it
def sub(x,y):
    z=x-y
    return z

result=sub(5,2)
print(result)#now the returned sub value is stored in z which is sub fun,
#sub is assigned to result,so we can do anything using result

def operations(q,w):
    add=q+w
    sub=q-w
    return add,sub #returning 2 statements
add,sub=operations(9,4) #accepting 2 statements
print(add,sub)

#!pass list in functions
def count(lists):
    even=0
    odd=0
    for i in lists:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even ,odd
lists=[1,2,3,4,5,6,7,8]
even, odd =count(lists)
print("Even:{},Odd:{}".format(even, odd))
print(even)
print(odd)

#?find length whose name is more than letters
names=[]
n=10
for i in range(0,n):
    name=input("enter your 10 friends name : ")
    names.append(name)
print(names)

def count1(names):
    shortname=0
    for j in names:
        if len(j)>=4:
            shortname+=1
    return shortname
    

s=count1(names)
print(s)





