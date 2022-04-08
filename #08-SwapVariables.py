
#!Swapping 2 varibale
a=5
b=6
temp=a #5
a=b #6
b=temp #5
#this mehtod is ok,but we are wasting variable 
print(a)
print(b)
#!use a better way (another way)
x=1
y=2

x=x+y #3
y=x-y #1
x=x-y #2

print(x)
print(y)
#but this  method we  still wasting one bit

#!using xor operator we dont waste bits
d=5
c=4
d=d^c
c=d^c
d=d^c
print(d)
print(c)

#!another unique method only in python  it used rot_two method  in stack 
e=3
w=2
e,w=w,e
print(e)
print(w)

