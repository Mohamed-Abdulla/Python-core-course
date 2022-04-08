
#!tuple - immutable
#!where d0 we use tuple?
#!when you dont have to change values,we can use tuple, since it unchangable its iteration speed is high.




tup=(22,233,4,4,5,66)
tup[0]
print(tup)
# x=tup[1]=1
# print(x) #error
print(tup.count(4))




#!set -{}
#!set never follows a sequence, it uses concept of hash, it is fast
#!cant repeat value,random sequence
#!indexing is not supported
s={12,34,5,4,6,4,5}
s.add(1)

print(s)

