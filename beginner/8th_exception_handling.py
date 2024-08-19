print("What an error does is to terminate the script, because something should not happen happened")

print("For example if we divide number to zero, script should throw an error")


try:
    x = int(input("First number: "))
    y = int(input("Second number: "))
    print(x / y)
except ValueError :
    print("Please enter a valid number next time!")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")


print("Using try and except blocks doesnot crash the program when ther is a problem with the code")

print("In order to catch some specific error we use its type after except block above the code you can see we used two different types of error to catch 'em")

print("There is also a finally block that runs in boths scenarios if there is an exception or not")

print("finally block is mostly used in streams as streams can crash easily but whatever happens we should close the stream, in order to that properly we use finally block")

print("Raising exception")

print("We can define the type of Error")
👍
def some_function():
    if True:
        raise Exception("Something went terribly wrong!")

some_function()



