
#!arrays of same type
from array import *
#type and values
#!type=signed char- i (allow both neg and pos int)
#!unsigned char -I (only pos)
vals=array('i',[5,6,7,-8,2])

print(vals.buffer_info())#address and size
print(vals.typecode) #type
vals.reverse()
print(vals)

for i in vals:
    print(i)

#create new array using existing array
newarr=array(vals.typecode,(a*a for a in vals))
#first parameter is type,second loops  over old array and sqr it
for e in newarr:
    print(e)

char=array('u',['a','c','b'])
for j in char:
    print(j)






















