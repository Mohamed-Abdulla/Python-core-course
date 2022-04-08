from array import *
#!Array value from User
#! Manual method
#create empty array
arr=array('i',[])
n=int(input('enter the length of the array : '))

for i in range(n):
    x=int(input('enter the next value : '))
    arr.append(x)
print(arr)
#!find index value 
val=int(input('enter the value to find : '))
k=0
for z in arr:
    if z==val:
        print(k)
        break
    k+=1

#!function to find the index
print(arr.index(val))

#!create a value 

arra=array('i',[])
g=int(input('enter the length of the array'))

for h in range(g):
        c=int(input('enter the next value : '))
        arra.append(c)
print(arra)

#del the index
valu=int(input('enter the value to delete'))

m=0
for u in arra:
    if u==valu:
        arra.pop(u)
print(arra)
arr=array('u',['a','b','c','d'])
len=len(arr)
# print(len)

for i in range(int(len/2)): #bcoz we changed swap 2 values at a time so 2 iterate is enough
    temp=arr[i]#a
    arr[i]=arr[len-i-1] #3
    arr[len-i-1]=temp
    
    

print('reverse array',arr)