class Person:
    """This is a  class variable"""
    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        """We use Person not self because it is a class variable, the same value for all the objects"""
        Person.amount += 1

    def helloWorld(self):
        print("Hi my name is {}, And I'm {} years old".format(self.name, self.age))

    def get_older(years):
        self.age += years

    def __str__(self):
        return "Name: {},\nAge: {},\nHeight: {}\n".format(self.name, self.age, self.height)

    def __del__(self):
        Person.amount -= 1
        print("Object was deleted!")


person1 = Person("Mike", 29, 177)
person2 = Person("Bob", 10, 177)
person1.name = "Michalle"

print(person1.name, person1.age, person1.height)
print(person2.name, person2.age, person2.height)
person1.helloWorld()
person2.helloWorld()
print(person2, person1)
print(person1.amount)
del person2
print(person1.amount)

