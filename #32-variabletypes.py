
#*types of  variables in oops
#?there are 2 type of variables 1.class variables which is created outside the init method.2.instance variables which are created inside the init method.

class car:
    #*class variables -which is common for all objects
    wheels=4
    def __init__(self): #*instance variables
        self.mil=10
        self.brand='bmw'
    
c1=car()
c2=car()
c1.mil=8

car.wheels=6 #*class variables -which change all objects 
#?namespace is an area where you create and store object/variables
    #*class namespace
    #*instance namespace

print(c1.mil,c1.brand,c1.wheels)
print(c2.mil,c2.brand,c2.wheels)
