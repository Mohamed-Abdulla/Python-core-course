num=5
print(id(num)) #address of the variables
name='hey'
print(id(name))
#!In python,if both variable has same value , it points to same memory address

a=10
b=10
print(id(a))
print(id(b))
#!garbage collection-unused values 

#!we dont have constant variables in python,but we  can use captial letter to show its a const varibale that you dont change
PI=3.14
print(type(PI))
