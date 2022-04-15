
#?you can inherit parent in to child class
#*Single level inheritance
class A: #?super class or parent class
    def feature1(self):
        print('feature 1 working')
    def feature2(self):
        print('feature 2 working')

class B(A): #?sub class or child class
    def feature3(self):
        print('feature 3 working')
    def feature4(self):
        print('feature 4 working')

#*Multilevel Inheritance

class C(B): #?sub class or child class --can inherit both parent and grandparent cls
     def feature5(self):
        print('feature 5 working')



a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature1()
c1=C()
c1.feature1()

#*Multiple Inheritance
# class D(A,B): it can inherit any class both a and b .even if b isn't inherit a'
    # pass






