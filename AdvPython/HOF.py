print("_-------without HOF !----------_")

#--------------------map-------------------

numbers = [1, 2, 3, 4, 5]

squares = []
for x in numbers:
    squares.append(x * x)

print(squares)

#----------------------------------
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

squares = list(map(square, numbers))
print(squares)

#----------------------------------

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
print(squares)

#----------------filter----------------------

numbers = [1, 2, 3, 4, 5, 6]

evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)

print(evens)
#----------------------------------
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(is_even, numbers))
print(evens)

#-----------------------------------
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#---------------reduce------------------------

numbers = [1, 2, 3, 4, 5]

total = 0
for x in numbers:
    total = total + x

print(total)

#-----------------------------------------
from functools import reduce

def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]

total = reduce(add, numbers)
print(total)

#-----------------------------------------
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)
print(total)