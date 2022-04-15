
#?Python does not support abstract class by default we need to import a package
from abc import ABC, abstractmethod
class Computer(ABC): #Class which has Abstracat Method is called Abstract Class
    @abstractmethod
    def process(self): #Abstract method has only declration not definition.
        pass 
class Laptop:
    def process(self):
        print('its laptop') 

#?you cant create object for abstract method
# com=Computer()
lap=Laptop()
lap.process()
