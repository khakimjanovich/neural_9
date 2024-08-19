"all values in python has data types"
"text in python has a data type named string"
"string has keyname of str in python"

#str "hello"
#str 'hello'

#str ''' Hello
#    world
#'''

"next data type is integer, integer is a whoole number, integer has a keyname of int"

#int 10
#int 9
#int -3

"if you need work with decimal number, you can work with float number"

#float 10.9
#float 8.343
#float -8.7685

"if you want to work with advanced mathematics you can make use of complex numbers, python complex method for that"

#complex(10,5) #so in this case 10+5i

"there is another data type called boolean, it has a keyword of bool, it only consist of two values"

#bool True
#bool False

"these are basic data types"

"importance of data types"

print("10"+ "10")
print(10+10)

"first one outputs 1010 hence the second one outputs 20"

"how to convert from one data type to another one"
print(type(10))
"this returns type of the given value or variable"
print(type("19"))

"defining variables"
x = 10
y = "hello"
whatever = True
z = 20
"variables are placeholders so we can use in different places"
print(x + z)
"above code prints the sum of the x and z values"



"Python is dynamically typed language"
"that means when we are defining a variable we don't need to define variable type in advance"
"and also that defined variable can change its data type after being defined"


"type casting"
x = "120"
# print(x / 4) # results type error, first we need to convert the x data type
x = int(x)
print(x/4) # now it works

"this only works if that x contains number string, in other case we get value error"
x = "hello"

# x = int(x) # this results a value error


