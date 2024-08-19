"Arithmetic operators, this operators used for calculations"
"+,-,*,/"

print( 8 + 1)
print(10 -1 )
print( 10 / 2)
print( 2*2)

"modulus operator gives us the remained of the division"
print(10%3) 
"in this case if are to divide 10 into 3, 3 will be the whole number and 1 will be the remainder, so 1 will be printed out"

"exponent operator, if we are to take one power to another number we use ** sign"
print(2 ** 5) 
"print 32"

"floor division, if we want to divide one number by another number and get whole number we use floor division //"

print(10//3) 
"this will give us 3"
print(-10//3) 
"this will give us -4, because it retuns smaller number, floor division rounds down to a number"

"assignment operator"

x = 10

"we can use assignment opetaor with other operators"
x = x + 10

print(x)

"or we can use in different way"

x += 10

print(x)

x -= 10

print(x)

x /= 2
print(x)

x *=2

print(x)

x **=2
print(x)


x //=(x)
print(x)


"comparison operators"

"== equals, != not equals, < less than, > greater than, <= less or equal to, >= greater or equal to"

"we use them to compare two sides"

"operations returns boolean values, True or False"

x = 10
y = 20

print(x == y)

print(x < y)

print(x > y)

print(x != y)

print(x <= y)

print(x >= y)

"we can use them with strings too"

x = "hello"
y = "Hi"
z = "hello"
print( x == y)

print( x == z)

print(x != y)

"logical operators"

"and or not"

print(10 < 20 and 20 > 30)
"returns false because and operator required both sides to be true"

print(not True)

print(not 10<20)

print(not 1 > 20)

"there is also a membership operators and bitwise operators"


"user inputs"
x = input() #this function always returns a value that the user enter
"the value will always be a string, we can type cast it for further processing"
"we can specify a message with paranthesis"
y = input("enter first number: ")
z = input("enter the second number: ")

y = int(y)
z = int(z)

print(y+z)


