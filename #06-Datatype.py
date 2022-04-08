

#!Datatypes
#!none - null (empty variable)
#!numeric-int,float,complex,bool
num=1
print(type(num))
a=3.4
b=int(a)
print(b)
c=4
d=complex(b,c)
print(d)
print(3>1)
print(b>c)
#!Sequence- list,tuple,set,string,range
lists=[33,34,44,55,54]
print(type(lists))
s={2,3,4,5,78,96,}
print(type(s))
tup=(22,233,4,4,5,66)
print(type(tup))
st='a'
print(type(st))
ran=range(10)
print(ran)
rang=list(range(2,10,2))
print(rang)

#!dict or hash map
d={
    'name':'abd','age':20
}
print(d.keys())
print(d.values())
print(d['age'])
print(d.get('name'))


