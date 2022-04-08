
#!Break -skip the iteration and break the loop
av=10
x=int(input("How many candies you want"))
i=1
while i<=x:
    if i>=av: #if  user inp is more than available ,then give what we got then break
        print('out of stock')
        break
    print("candy")
    i+=1
print("next time")

#!Continue --skip that iteration
for j in range(1,11):
    if j%3==0 or j%5==0:
        continue
    print(j)

#!Pass --just pass
for z in range(1,11):
    if z%2!=0:
        pass #do nothing
    else:
        print(z)
