
#?Selection Sort -find min value in each iteration and swap

nums=[5,3,8,6,7,2]
#?Here,we swap only once in each iteration

def sort(nums):
    for i in range(len(nums)):
        minpos=i #5
        for j in range(i,len(nums)): 
            if nums[j] < nums[minpos]:
                minpos=j 
            temp=nums[i]
            nums[i]=nums[minpos]
            nums[minpos]=temp

sort(nums)
print(nums)
