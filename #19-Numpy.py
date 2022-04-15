from numpy import *
#!for multidimensional array we have to install numpy
#different way of creating array -6 types
#!array(),linspace(),logspace(),arange(),zeros(),ones()
#!array
arr=array([1,2,3,4,5,6,7.0]) #we dont need to specify type of array
# print(arr.dtype)
print(arr)
#!linspace
arr1=linspace(0,15,16)#start,stop,step -stop also included,step-break in to parts-float
#if we didnot specify the step ,it will automatically step to 50 parts
print(arr1)
#!logspace -differentiate with the help of log (1n0^)
arr2=logspace(1,40,5)
print(arr2)
#!arange
arr3=arange(1,15,2)
print(arr3)

#!zeros
arr4=zeros(5)
print(arr4)

#!ones
arr5=ones(5,int)
print(arr5)