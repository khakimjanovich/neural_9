"in python there are 2types of loops, while and for"
"while runs a script until some condition is met"
x = 0
while(x < 10):
    print(x)
    x +=1
"for loop iterates over sequances"

print("this is another function")
for x in range(10):
    print(x)
print("this is new function")
for x in range(1,21):
    print(x)

print("Loop control statements")
print("Loop control statements allow us to control loop manually")

x = 0
while x < 10:
    x +=1
    if x == 5:
        break
    print(x)

print("loop above stopped manually with break when x gets to equal to 5, oringally it has to go till 10")

x=0
while x < 10:
    x+=1
    if x == 5:
        continue
    print(x)

print("loop above skipped a step when x equals to 5")


x = 0
while x < 10:
    x +=1
    if x == 2:
        pass
    print(x)
print("there is also a pass loop controll") 
print("it is hard to explain so read it for yourself")


