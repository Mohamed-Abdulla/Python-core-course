from traceback import print_tb


data={
    1:'abd',
    2:'abdulla',
    4:'mohamed'
}
print(data[1])
print(data.get(2))
#!when key is not available ,but u waant to return
print(data.get(1,'notfound'))
print(data.get(3,'notfound'))

#!making dict from lists
keys=['mohamed','abd','abdulla']
values=['python','java','js']
#merge using zip and convert using  dict
data1=dict(zip(keys,values))
print(data1)
#how to add values to dict

data1['Mohamed Abdulla']='React'
print(data1)

#!delete a dict
del data1['abd']

#!nested list and dict in dict
#!for various type of collections in a key value pair
prog={
    'js':'vscode',
    'cs':'vs',
    'python':['pycharm','jupyter'],
    'java':{
        'jse':'sublime',
        'jee':'eclipse'
    }
}

print(prog['java']['jee'])
