#Public members - Protected _ - Private __

class Person:
    def __init__(self,name):
        self._name = name # protected

class student(Person):
    def display(self):
        print(self._name)

p = student("Gamana")
p.display()
print(p._name)

# Private Members

class Employee:
    def __init__(self,salary):
        self.__salary = salary #private

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,amt):
        if amt >= 0:
            self.__salary = amt
            
e = Employee(30000)
#Name Mangling _classname__variable
print(e._Employee__salary)
# print(e.get_salary())
# e.set_salary(50000)
# print(e.get_salary())
# print(e.__salary) Error
