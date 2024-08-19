print("A function is a block of reusable codes")

print("we tell a python using def keyworkd that we are going to define a functions")

def helloworld():
    print("Hello world")

print("hellowrld is a name of  the function")

print("paranthesis indicates that helloworld is a function, and inside parantheis we give parameters")

helloworld()

def add(x=0, y=0):
    return x + y

result = add(1,2)

print(result)


print("we can give default parameters in order to make the function parameters optional")

print("sometimes we don't know how many parameters do we need when we start to writing our function")

def mysum(*numbers):
    result = 0 
    for number in numbers:
        result += number
    return result

print(mysum(10,20))

print(mysum(10,20,30,50))


