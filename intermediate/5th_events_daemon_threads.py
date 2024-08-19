"""

"""
import threading

event = threading.Event()


def func():
    print("waiting for event to trigger..!")
    event.wait()
    print("Performing action XYZ now...")


t1 = threading.Thread(target=func)
t1.start()

x = input("Do you want to trigger the event? (y/n): ")

if x == 'y':
    event.set()

import time

path = 'text.txt'
text = ""


def readFile():
    global path, text
    while True:
        with open("text.txt", 'r') as f:
            text = f.read()
        time.sleep(1)


def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)
t1.start()
t2.start()