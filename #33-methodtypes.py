
#*types of  methods in oops
    #?instance methods -accecor method,mutator method -is work with instance variables(self)
        #*for fetching instance variables use accecor method (getters)
        #*for modifying instance variables use mutator method(setters)
    #?class methods -is for work with class variables(cls)
    #?static methods- is not work with any of the variables ()

class Student:

    school='MMS' #?class or static variables

    def __init__(self,m1,m2,m3): #?instance variables
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):#?instance method
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):#?accecor method
        return self.m1
    
    def set_m1(self, value): #?mutator method
        self.m1 = value

    @classmethod
    def getSchool(cls): #?class methods
        return cls.school
    
    @staticmethod
    def info(): #?static method
        print("This is student class .. in abc module")

s1=Student(54,32,65) 
s2=Student(54,24,67)

print(Student.getSchool()) #class 
print(s1.avg()) #instance

Student.info()#static 