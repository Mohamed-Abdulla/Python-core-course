
pos=-1
list=[5,8,4,6,9,2]
#?Search 9 by manually
n=9
def search(list,n):
    i=0
    # while i<len(list):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
        # i=i+1
    return False

if search(list,n):
    print('found',pos+1)
else:
    print('not found')