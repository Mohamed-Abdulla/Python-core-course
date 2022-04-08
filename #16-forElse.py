
#!for else only work with break statement
nums=[14,12,11,21,26]

for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")

#!find prime num
num=7
for i in range(2,num):
    if num%i==0:
        print("not a prime")
        break
else:
    print("prime")