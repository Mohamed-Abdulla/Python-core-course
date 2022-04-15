nums=[4,5,7,3]
#?1 way
# it=iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# #?2way
# print(next(it)) #it reserve the old ans and give next one
#*Iterators iterates one value at a time .we need to define func it manually
#?Create your own iteration method -using iter and next
class Topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <=10:
            val=self.num #1
            self.num+=1
            return val
        else:
            raise StopIteration #to stop for loop

values=Topten()
print(next(values))
for i in values:
    print(i)

