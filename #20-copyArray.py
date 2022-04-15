from numpy  import  *
arr=array([1,2,3,4])
arr1=array([5,6,7,8])
#adding 2 arrays
arr2=arr+arr1
#concantinate 2 array
print(concatenate([arr,arr1]))
print(arr2)

#!copy an array

arr3=array([3,6,6,7,8,])
#!alising method same memory address 
# arr4=arr3
#or 2 different arry with df address -#!shallow copy and deep copy
#shallow copy -if value  in arr3 changes ,arr4 also changes
arr4=arr3.view()
#deep copy -value  dont change
arr4=arr4.copy() 
