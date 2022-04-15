
#!Constructor in Inheritance
class A: #?super class or parent class
    def __init__(self):
        print('im A init')
    def feature1(self):
        print('feature 1 working')
    def feature2(self):
        print('feature 2 working')

class B: #?sub class or child class
    # def __init__(self):
    #     super().__init__() #?for getting both A and Child Constructor. we are calling init method of super class.
        # print('im B init')
    def feature3(self):
        print('feature 3 working')
    def feature4(self):
        print('feature 4 working')
class C(A,B): 
    def __init__(self):
        super().__init__()
        print('im C init')
    def feat(self):
        super().feature2()
    

# a1=A() #object constructor
#?Method Resolution Order (MRO) in multiple inheritance.it means it always start from left to right 

c1=C()
c1.feat()
