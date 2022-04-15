
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap=self.Laptop() #?obj of laptop
    
    def show(self):
        print(self.name,self.age)
        self.lap.show()
    
    class Laptop:
        def __init__(self):
            self.brand = 'hp'
            self.ram = '16gb'
            self.rom = '1tb'
        def show(self):
            print(self.brand,self.ram,self.rom)

s1=Student('abd',20)
s2=Student('abdulla',20)
lap1=s1.lap
lap2=s2.lap
s1.show()
s2.show() 