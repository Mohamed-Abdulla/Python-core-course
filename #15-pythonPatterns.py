# i=1
# while i<4:
#     print('# ',end="")
#     j=1
#     while j<4:
#         print('# ',end="")
#         j+=1
#     i+=1
#     print()

#!in for loop
#!square
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()
#!triangle
for i in range(4):
    for j in range(i+1):
        print("# ",end="")
    print()

#!reverse triangle
for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()

#!mirror triangle
for i in range(5):
    for j in range(5-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()

#!reverse mirror triangle
for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(5-i):
        print("*",end="")
    print()

#!num =5
num=5
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(0,i):
        print((k+1),end="")
    print()





    


