import time
import threading #avialable in python

def inf_loop(): #case 1
    while 1==1:
        pass

'''
def inf_loop(): #case 2 (both are workable)...
    while True:
        time.sleep(0.01) # if this func sleeps then cpu gives a chance to other thread.
'''


def func2():
    print("learning MultiThreading!!!")

#Introducing two individual threads here which operates individually for each function.
t1 = threading.Thread(target=inf_loop)
t2 = threading.Thread(target=func2)

#calling those two threads to operate accordingly...
t1.start()
t2.start()
