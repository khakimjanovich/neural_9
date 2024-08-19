
print("Sequence is a collection of variables, instead of assigning one value to a varaible we can assign many values to a variable, in order to that we can make use of sequences")

print("First we talk about lists, to define a list we use square brackets [], and i put my variables between 'em with ,")

mylist = [10,20,1,3,100]

print(mylist)

print("as python is dynamically typed we can put different data types inside a single list")
myotherlist = ["hello", 10, True, 10.4]
print(myotherlist)

print("In order to access some value inside a list we can use its index, as in programming we start counting from 0, 10.4 value is in 3index, and we can access it using myotherlist[3]")

print(myotherlist[3])

print("if we try to access an index that has no value, it throws out of range error")
# print(myotherlist[4])

print("Traceback (most recent call last): File '/neural_9/beginner/6th_sequences_collections.py', line 19, in <module> print(myotherlist[4]) IndexError: list index out of range")

print("If we want some slice of the list we can use : mark to get from what index to to index of the values in the list")
print(myotherlist[:3])
print(myotherlist[2:3])
print("element on the right side is not included but the left side is included")




print(myotherlist[-2])

print("in order to change some value inside the list we can use its index to change it")

print(myotherlist)
changing = input("Enter some index to change this list: ")
changing = int(changing)
changer = input("Enter a value to change a value in that index: ")
myotherlist[changing]=changer
print("We have successfully changed your value: ")
print(myotherlist)



for x in myotherlist:
    print(x)

print("now we see what we can do with lists")

x = [1,23,3,5]
y = ['asdf',True,10.3]

print(x + y)

print( x *2)

print("there are three basic list functions they are: len, max, min")

print(len(x))

print(max(x))

print(min(x))

print("min and max can be used with only float and integers")

print("now let us see some list methods")

print("the first method would be: append")

x.append("added value")

print(x)

print("if we want to insert some value into some specific index we can use insert method")

x.insert(3,"soeme other value")

print(x)

print("as you can see we inserte3d some other value into 3 index and the original 3 index value shifted to the next index")

x.remove(1)
print("remove method removes given value in list, if you give a value that doesn't exist in list it throws an erro")

x.pop(1)
print("pop method removes a value by given index, if you giva an index that doesn't exists in list it throws an error")

print(x)
# x.index(3)

print( "index method returns an index that given value")

z = [55,6,1,88,2,34]

print(z)

z.sort()

print(z)

print("sort method sorts the array")

print("there is a functions name with sorts that does the same thing without chaning given list")

print("Tuples")

print("Tuples and list as a set they are the same, except for the difference that we cannot change tuple")

a = (1,2,3,5)

print("this is tuple:")
print(a)
print("this is the first index of the tuple")
print(a[0])

print('we can type cast tuple into list')

x= list(a)

print(x)

print("we try to change some index of casted tuple")

x[2] = "hello"

print(x)

z = tuple(x)

print(z)

print("we have changed value and type casted back to tuple")

print("Last type of the sets are dictionaries")

print("The first difference that they are constructed with curly braces, and the second difference they are constructed by key value pairs, tuple and list are index based sets")

a = {"name":"Car","name":"Car name", "model":"car model", "created_at":"car created at"}

print(a)

print("You access dictionary value by giving its key name in square braces")
print(a['name'])
print("and dictinoary name has to be unique")
a["newkey"] = "Some value"

print(a)

print("Three main methods of the dicitonary are items keys and values")

print(a.items())
print(a.keys())
print(a.values())



print("membership operators")

print("two membership operators in, not in")
x = [1,2,3,5]

print(2 in x)

print(7 in x)

print(2 not in x)

print(7 not in x)

print("identity operators")

print("two identity operators is, is not")

if type(x) is list:
    print("x is list")
else:
    print("x is not list")

a = tuple(x)

if type(a is not list):
    print("a is not a list")
else:
    print("a is a list")


