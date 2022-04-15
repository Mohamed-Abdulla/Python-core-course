
#?Binary Search -all items have to sorted
#?First index is Lowerbound and last index is upper  bound. add upper and lowerbound and floor div by 2 and mid 
#? If search value is smaller then change upperbound & Mid becomes new upper bound. If search value is bigger then,
#?change lowerbound & Mid becomes new lower bound

pos=-1 #?to found position
list=[2,3,5,7,8,9,10]
n=9
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False

if search(list,n):
    print('Found',pos+1)
else:
    print('Not Found')

