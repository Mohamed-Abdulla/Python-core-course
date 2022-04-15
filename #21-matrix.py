from numpy import *

#!multi  dimentional array
arr1=array([
    [1,2,3,4,5,6],
    [4,5,6,4,2,1]
])
print(arr1.ndim) #dimensions
print(arr1.shape) #shape-rows and columns
print(arr1.size) #total elements
#convert 2d array to 1d
arr2=arr1.flatten()
print(arr2)
#convert 1d array to 2d
arr3=arr2.reshape(2,2,3)
print(arr3)

#!matrix
#!matrix is a 2d array
mat=matrix(arr1)
print(mat)
#!creating matrix array
m=matrix('1 2 3; 4 5 6; 7 8 9')
print(m);
#!diagonal matrix
print(diagonal(m))
