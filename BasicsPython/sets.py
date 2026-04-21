# A set in Python is a collection of unique (no duplicates), unordered elements.
# No duplicate values
# Unordered (no indexing like lists)
# Mutable (you can add/remove items)
# Fast operations (like membership check)

# Using curly braces {}
my_set = {1, 2, 3, 4}
print(my_set)

# Using set() function - constructors
another_set = set([1, 2, 2, 3])  # duplicates removed automatically
print(another_set)  # Output: {1, 2, 3}

#add
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

#Remove Elements
s.remove(2)   # Error if not found
s.discard(10) # No error if not found

# Check Membership
print(3 in s)  # True

# Set Operations 
# Union (Combine sets)
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # {1, 2, 3, 4, 5}

# Intersection (Common elements)
print(a & b)   # {3}

# Difference (Elements in a but not in b)
print(a - b)   # {1, 2}
print(b - a)   # {4, 5}

# Symmetric Difference (Not common)
print(a ^ b)   # {1, 2, 4, 5}

# Loop Through a Set
for item in a:
    print(item)


# Removing duplicate values from a list:

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}


# You cannot access elements using index

# Interview Questions

# Difference between list and set?

# Why sets are faster than lists for searching?

# Can sets contain duplicates?

# What is the difference between remove() and discard()?

a = {1, 2}
a.update([3, 4, 5])
print(a)  # {1, 2, 3, 4, 5}

# Frozen Set (Important)

fs = frozenset([1, 2, 3])

#fs.add(4) #Error (cannot modify Immutable)
print(fs)
