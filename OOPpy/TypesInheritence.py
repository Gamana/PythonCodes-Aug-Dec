# 1. Single Inheritance
# One child class inherits from one parent.
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    pass

c = Car()
c.start()
# Flow: Vehicle → Car

# 2. Multiple Inheritance - MRO
# One child inherits from multiple parents.
class Engine:
    def engine_type(self):
        print("Petrol Engine")

class Wheels:
    def wheel_count(self):
        print("4 Wheels")

class Car(Engine, Wheels):
    pass
c = Car()
c.engine_type()
c.wheel_count()

# Flow: Engine + Wheels → Car

#  3. Multilevel Inheritance
# A chain of inheritance.
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class SportsCar(Car):
    def speed(self):
        print("Very fast")

s = SportsCar()
s.start()
s.drive()
s.speed()
# Flow: Vehicle → Car → SportsCar

# 4. Hierarchical Inheritance
# Multiple child classes inherit from one parent.

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = Car()
b = Bike()

c.start()
b.start()

#  Flow:

#         Vehicle
#        /      \
#      Car      Bike
# 5. Hybrid Inheritance

# Combination of multiple types (like multiple + multilevel).

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Engine(Vehicle):
    def engine(self):
        print("Engine working")

class Wheels:
    def wheels(self):
        print("Wheels rolling")

class Car(Engine, Wheels):
    pass

c = Car()
c.start()
c.engine()
c.wheels()

# Flow: Combination of hierarchy + multiple

# Quick Summary Table
# Type	Meaning
# Single	1 Parent → 1 Child
# Multiple	Many Parents → 1 Child
# Multilevel	Chain (Grandparent → Parent → Child)
# Hierarchical	1 Parent → Many Children
# Hybrid	Combination of above