print("-------Method Overriding(Runtime polymorphsim)------------")

class Parent:
    def Marry(self):
        print("Marry at the age of 28-30")

class child(Parent):
    pass
    # def Marry(self):
    #     print("Marry at the age of 30-35")

c = child()
c.Marry()

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")   # Overriding

a = Dog()
a.sound()

print("-------Method Overloading(Compile-time polymorphsim)--same name but diff parameter----------")
#Python does NOT support true method overloading
class Test:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

t = Test()
# print(t.add(2, 4)) //Error
print(t.add(3, 3, 3))

# Using *args(0....n) - tuple (Flexible Arguments, functional Arguments)
class Math:
    def add(self, *numbers):
        return sum(numbers)

m = Math()

print(m.add(2, 3))          # 5
print(m.add(2, 3, 4, 5))    # 14
print(m.add(3)) # 3

# *numbers allows any number of inputs

print("------------------Operator OverLoading--------------------")
# Operators behave differently depending on operands.

print(5 + 3)          # 8
print("Hi " + "All")  # Hi All

# + works for numbers AND strings
class Number:
    def __init__(self, value):
        self.value = value # 10

    def __add__(self, other):
        return self.value + other.value # 10 + 20

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)   # 30

# 3 objects
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

n1 = Number(10)
n2 = Number(20)
n3 = Number(30)

result = n1 + n2 + n3
print(result)   # 60 

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(85)
s2 = Student(90)
print(s1 + s2)   # 175

print("------------------Duck Typing-----------------------------")
# If it walks like a duck and quacks like a duck, it's treated as a duck

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())

class Parrot:
    def fly(self):
        print("Parrot is flying high in the sky!")

class Airplane:
    def fly(self):
        print("Airplane is taking off!")

# Function using duck typing
def make_it_fly(thing):
    thing.fly()

# Creating instances
parrot = Parrot()
airplane = Airplane()

# Passing different objects to the same function
make_it_fly(parrot)   # Output: Parrot is flying high in the sky!
make_it_fly(airplane) # Output: Airplane is taking off!