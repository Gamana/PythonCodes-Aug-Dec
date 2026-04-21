from functools import reduce

numbers = [2, 3, 4, 5, 6]

# Double each number → keep only even numbers → find sum
result = reduce(lambda x, y: x+y,
                filter(lambda x: x % 2 == 0,
                       map(lambda x: x**2, numbers)))

print(result)

print("------------------------------")

from functools import reduce

def double(x):
    return x ** 2

def is_even(x):
    return x % 2 == 0

def add(x, y):
    return x + y

numbers = [2, 3, 4, 5, 6]

# Double each number → keep only evens → multiply them
result = reduce(add,
                filter(is_even,
                       map(double, numbers)))

print(result)