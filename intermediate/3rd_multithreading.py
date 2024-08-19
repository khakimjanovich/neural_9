"""
    Threads are light weight processes
"""

""" 
    Threads are part of processes. Multiple threads in the same process share the same memory space
    so they can communicate each other. They can synchronize each other
"""

import threading


def function1():
    for x in range(10000):
        print("One")


def function2():
    for x in range(100000):
        print("Two")


t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()


"""
    using join we wait the thread to finish its job
"""
print("Another text")
