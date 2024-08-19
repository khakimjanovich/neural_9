print("whenever we want to read from a file or write to a file, we need so called file streams")
print("we need to open a stream so information can flow")   
file = open('myfile.txt', 'r')

print('There are three basic types of opening a file stream r-reading mode, w-writing mode, a-appending mode')
print("How streams work?")
print("file = open('myfile.txt','r'), with this code we have an open file stream")
print("whenver we opea file stream we have to close it")
file.close()


print("if you don't want to close a stream manually you can open a stream with 'with' method")

with open('file.txt', 'r') as f:
    content = f.read()
    print(content)


file = open('myfile.txt', 'w')

file.write("Hello from vim")

file.close()

file = open('myfile.txt','r')

content = file.read()

file.close()

print(content)


print("flush method flushes written content to the file, without flushing content you cannot put content into that file")

file = open('myfile.txt', 'w')


myfile = open('myfile.txt', 'r')

print(myfile.read())

myfile.close()


file.write('hello from vim 2')

file.flush()

file.write('some other thing from vim')


file.close()

myfile2 = open('myfile.txt','a')
myfile2.write(" Hello world2 in appened mode")
myfile2.flush()
myfile2.close()

from os import *

#mkdir("test")
#chdir("test")
#mkdir("newdir")
#rename('myfile.txt','myfile.txt')