
#func calling itself 
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

#!fact using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(5)
print(result)


def fact1(n):
    return n*fact(n-1)
n=fact(5)