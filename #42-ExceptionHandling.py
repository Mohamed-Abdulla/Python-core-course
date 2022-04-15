
#!Errors
    #?Compile time -syntax error
    #?logical time - code gives output but its wrong
    #?run time -code is compiled(foe eg:getting error in run time- div-div by zero -user make error/problem)

a=5
b=2 #critical statement

try:
    print("resources open")
    print(a/b) #if this works ,fine. if its not handle expection block and execute
    k=int(input('enter a number'))
    print(k)

except ZeroDivisionError as e: #we specify this error would come ,if user gives wrong input
    print('Hey, You cannot divide a Number by Zero',e)

except ValueError as e:
    print('Hey,Invalid Input',e)

except Exception as e: # as e,means we can even mention our error also. its  a top general exception
    print("Something went wrong..",e)

finally: #Finally block will be executed if we get error as well as if we dont get the error
    print("resources closed")
    print('bye')
