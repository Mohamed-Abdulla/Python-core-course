
#?we are solving real world problems with virtual world solutions.
#*in real world ,everything is objects
#*like that all are objects in virtual world too.
#?As a object ,I know something(Attributes(data)),I do something(behavior(methods)) with what i know
#* Class is a blueprint or design
#* object is a Instance of class (real thing) 
#!eg:motorola manufactring and designing


#?CLASS AND OBJECTS
#first create blueprint then design
class Computer: 
    #*Attributes ->variables(for store data)
    
    def __init__(self,processor,ram): #?init func doesnt need to call. it is a constructor
        self.processor = processor
        self.ram = ram
    #*Behavior ->Methods(functions)
    def config(self):
        print(self.processor,self.ram)
    def compare(self,comp2):
        if self.ram!=comp2.ram:
            return True
        else:
            return False

comp1=Computer('i7',16) #?constructor
comp2=Computer('i5',8)

if comp1.compare(comp2): #*to compare two objects
    print("they are different")
# Computer.config(comp1) 
comp1.config()
comp2.config()

#?everytime we created an object,it creates new space 
#?size of an obj is depend up on the no of variables used. size is allocatetd by constructor.constructor calls init method

