# Duck Typing (Dynamic Polymorphism)
# Python doesn’t care about the object type, only about the method.

class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

# Same method name used
for obj in [Bird(), Airplane()]:
    obj.fly()


class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

# Creating objects separately
b = Bird()
a = Airplane()

# Calling methods
b.fly()
a.fly()

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

print("-----------------------Method Overriding (Runtime polymorphsim)----------------------------")

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")   # Overriding

a = Dog()
a.sound()

print("----------------Method Overloading------------------------")
#Python does NOT support true method overloading
class Test:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
    
    
# Using *args (Flexible Arguments)
class Math:
    def add(self, *numbers):
        return sum(numbers)

m = Math()

print(m.add(2, 3))          # 5
print(m.add(2, 3, 4, 5))    # 14

# *numbers allows any number of inputs

class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()

print(m.add(2, 3))      # 5
print(m.add(2, 3, 4))   # 9

print("------------------Operator OverLoading--------------------")
# Operators behave differently depending on operands.

print(5 + 3)          # 8
print("Hi " + "All")  # Hi All

# + works for numbers AND strings

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)   # 30

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(85)
s2 = Student(90)

print(s1 + s2)   # 175

print("----------------")
class Number:
    def __init__(self, value):
        self.value = value

    # Operator overloading for +
    def __add__(self, other):
        print(f"Adding {self.value} + {other.value}") # ((5 + 10) + 15) + 20
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

    a = Number(5)
    b = Number(10)
    c = Number(15)
    d = Number(20)

    # Using more than 2 objects
    result = a + b + c + d

    print("Final Result:", result)

