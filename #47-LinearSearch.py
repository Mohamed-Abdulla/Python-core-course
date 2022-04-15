
pos=-1 #?to found position
list=[5,8,4,6,9,2]
#?Search 9 by manually
n=9
def search(list,n):
    i=0
    # while i<len(list):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i #?we are modifying global variable inside local variable so we use globalsss
            return True
        # i=i+1
    return False

if search(list,n):
    print('found',pos+1)
else:
    print('not found')


#?In linear Search,it searches one by one ,if the list is too long it takes more time-to solve this we use Binary search
#?No need for the list to be sorted in Linear Search