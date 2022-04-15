
#?Operator Overloading -operators are same but operands are different or type of arguments passing is different
a='10'
b='ad'
print(a+b) 
print(str.__add__(a,b)) #everything is a object in python

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other): #s1,s2
        m1=self.m1+other.m1 #54+67
        m2=self.m2+other.m2 #32+54
        s3=Student(m1,m2)
        return s3
    def __gt__(self,other): #greater than-gt
        rank1=self.m1+other.m1 #54+67
        rank2=self.m2+other.m2 #32+54
        if rank1 > rank2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2) #we use format to convert to str bcoz it is in tuple format. we cant add str+tuple

s1=Student(54,32) #m1,m2
s2=Student(67,54) #m1,m2
#?we cant normally add two class unless we define it as method in our class.this is called operator overloading
s3=s1+s2 #?-->Student.__add__(s1,s2)
print(s3.m1)
if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')
        
#? when we call a it prints value not address
a=9
print(a)
print(a.__str__())
#?But when we call our user defined objects ,it prints value
print(s1) #prints address
#?to solve that ,we need to overwrite default __str__ method.so define str in our class 
print(s1)#print value