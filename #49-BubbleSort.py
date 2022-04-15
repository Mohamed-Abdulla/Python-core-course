
#?BubbleSort-technique to sort a list 
nums=[5,3,8,6,7,2]
print(len(nums))
#?comparing and swapping
# nums.sort()

def sort(nums):
    for i in range(len(nums)-1,0,-1): #5,0,-1
        for j in range(i):
            if nums[j]>nums[j+1]: #5
                #?swap
                temp=nums[j] #5
                nums[j]=nums[j+1] #3
                nums[j+1]=temp #5
sort(nums)
print(nums)

#?it consumes lot of power,becoz it takes lots of swapping -so we can use selection soer