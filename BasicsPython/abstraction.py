from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def receive(self):
        print("Amount Received")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

p = UPI()
p.pay(500)
p.receive()

print("----------------Example 2---------------------------------")

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class inheriting from the abstract class
class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

# Creating an instance of Car
my_car = Car()
my_car.start()  # Output: Car is starting
my_car.stop()   # Output: Car is stopping