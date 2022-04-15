
f=lambda a,b:a+b #before : is arg and after is expression
result=f(5,6)
print(result)

#!filter,map and reduce
nums=[1,2,3,4,5,6,7,8,9]
#?filter
evens=list(filter(lambda n : n%2==0,nums)) #func,lists
print(evens)
#?map 
doubles=list(map(lambda n:n*2,evens))
print(doubles)
#?reduce belong to functools ,so import it
from functools import *
sum=reduce(lambda a,b:a+b,doubles)
print(sum)