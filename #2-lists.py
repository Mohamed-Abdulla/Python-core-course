# grouping together
#!list is mutable
lists=[2,3,4,6,3]
print(lists[0:3])
print(lists[-3])
names=['abd','naruto','kakashi']
print(names)
values=['abd',12,20.0]
print(values)
# we can also group list in to list
group=[lists,names]
print(group)
lists.append(23)
lists.extend([12,23,44]) #add multiple value in lists
lists.insert(0,1)
lists.sort()
lists.remove(1)
lists.pop(0)
lists.reverse()
del lists[7:]
x=sum(lists)
x=min(lists)
x=max(lists)

print(lists)
print(x)