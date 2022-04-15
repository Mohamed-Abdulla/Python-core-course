
#?What is thread?
    #*breakdown a big file into small lightweight file is called thread. each thread working on multicore called multithread.
from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1) #wait for 1 sec
class Hi(Thread):
     def run(self):
        for i in range(5):
            print('hi')
            sleep(1)
t1=Hello()
t2=Hi()

t1.start() #execute by t1 thread
sleep(0.2) #to prevent collision
t2.start()#execute by t2 thread

#?Each thread has main thread
#?print hello and hi by creating two thread use thread by importing threading and use start for run

t1.join() 
t2.join()
#?these join means join those all then execute last main thread
print('bye') # execute by main thread
