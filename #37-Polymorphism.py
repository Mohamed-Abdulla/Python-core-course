
#?Polymorphism- poly means many,morph means form. --one thing takes many forms .
    #*Duck typing in python
    #*Operator Overloading
    #*Method Overloading
    #*Method Overriding

#?Duck typing in python 
#*Saying-if it looks like a duck,swims like a duck and quacks like a duck,then it probably is a duck.

class VsCode:
    def execute(self):
        print('compiling')
        print('running')
class Pycharm:
    def execute(self):
        print('spell check')
        print('convection check')
        print('compiling')
        print('running')
class Laptop:
    def code(self,ide):
        ide.execute()

ide=Pycharm()
#?if i change the ide from vscode to pycharm it still works,becoz what matters is ide.execute ,if it acts like a duck
#? execute,it runs vscode or pycharm based on what we passed  is called Duck-Typing

lap1=Laptop()
lap1.code(ide)

