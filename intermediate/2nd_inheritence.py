class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def get_older(years):
        self.age += years


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary * 12

    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary: {}".format(self.salary)
        return text


worker = Worker("Kid", 21, 177, 4000)

print(worker)


class Programmer(Worker):
    def __init__(self, name, age, height, salary, preferred_language):
        super(Programmer, self).__init__(name, age, height, salary)
        self.preferred_language = preferred_language

    def __str__(self):
        text = super(Programmer, self).__str__()
        text += ", Preferred Language: {}".format(self.preferred_language)
        return text


programmer = Programmer("ki2", 22, 180, 5000, "python")

print(programmer)

print("Operator overloading")

print("Operator overloading is you can decide what happens if you use some sort of operators")

print("For example you can decide what happens if you subtract one object by another one")


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)


vector1 = Vector(2, 5)
vector2 = Vector(3, 1)

print(vector1, vector2)

vector3 = vector1 + vector2

print(vector3)

vector4 = vector2 - vector1

print(vector4)
