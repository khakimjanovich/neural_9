print("the first thine about strings is that we can treat them sequence of characters")
text = "hello world"

print(len(text))
print(text[6:])
print(text[1])
for l in text:
    print(l)

print("backslash n is the escape character, line break character")

text2 = "hello world with backslash n \n this is new line created with backslash n"
print(text2)

print('string formatter')

name = input()

age = int(input())


print("there are 2 types of string formatting first one is this and the second one with this")

print("my name is %s and I am %d" % (name, age))

print("My name is {} and I am {} yeards old!".format(name,age))

print("String functions")

print("The first one is case manipulation functions")

text = "this is my text!"
text = text.upper()

print(text)

text = text.lower()

print(text)

text = text.title()

print(text)

text = text.swapcase()

print(text)

print('the second type of function is count: counts how many time a substring contained in a string')

text = "The book i was reading was cool, because it was chosen with care"

print(text.count('was'))

print('the third type of function is find: it returns the index of the string')

print(text.find('book'))

print(text.find('The'))
# print(f"my name is {age} and I'm {age} years old!")

print("another useful function is join function: join function is basically used to join list using seperator")

separator = ';'
mylist = ['Kitchen','Dog','Mike']

print(separator.join(mylist))

print('the opposite function of join method is split')

text = "I am happy because my name is jun"

words = text.split(' ')
print(words)

print("the last function is replace")
text = "i am Mike! My name is Mike!"
text = text.replace("Mike","Jun")
print(text)