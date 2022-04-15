
#?pass by value ,pass by referance
#*when we pass variable as a arg to a fn,it pass as a value not as a variable
#*pass by referance means passing a address itself

#!python dont follow passby value or pass by variable; 
def update(x): #?formal arguments
    x=8
    print("x",x)
a=10
update(a)#?actual arguments

#!type of Arguments
#*Actual arguments
#?Position arg
#?Keyword arguments
#?default arguments
#?variable length arguments
#!eg of variable length arguments
def sum(a,*b): #?here b is tuple ,accept multiple values
    c=a
    for i in b:
        c+=i
    print(c)
sum(5,6,3)
#!keyworded variable length arguments
def person(name,**data): #? ** accept multiple parameterr and also  keyword 
    print(name)
    print(data)#now its a dict format, to print in variable ,use for loop
    for i,j in data.items():
        print(i,j)
person('abd',age=20,company='avasoft',num='987654321')

