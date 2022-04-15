
#?Handling file in Python
#?read file
f=open('#43-MultiThreading.py','r') #filename,read
print(f.read()) #?read all
print(f.readline())#?read oneline 
#?overwrite a file
f1=open('abc','w') #filename,overwrite
f1.write('hey') #overwrite everything
#?append a file
f2=open('abc','a') #filename,append
f2.write('abd') #append/add data

#?copy all data from one file  and write in another file

#?using for loop for read line by line and then write

for data in f:
    f1.write(data)

#?rb-means read in binary format
#?open image 
f3=open('joker03_uhd.jpg','rb')
f4=open('jokercopy.jpg','wb')
for i in f3:
    f4.write(i)


