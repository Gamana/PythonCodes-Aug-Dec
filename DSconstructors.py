# 🔹 1. list() – Create a List
# ✅ When to use:
# When you want a mutable (changeable) ordered collection
# When converting other data types into a list
# 💻 Examples:

l1 = list()              # empty list
l2 = list([1, 2, 3])     # from list
l3 = list("abc")         # from string

print(l3)  # ['a', 'b', 'c']

# Storing items where order matters
# You need to modify data (add/remove)


# 🔹 2. tuple() – Create a Tuple
# ✅ When to use:
# When you want fixed (immutable) data
# Data should not be changed
# 💻 Examples:
t1 = tuple()             # empty tuple
t2 = tuple([1, 2, 3])    # from list
t3 = tuple("abc")        # from string

print(t3)  # ('a', 'b', 'c')

# Coordinates (x, y)
# Constant data


# 🔹 3. set() – Create a Set
# ✅ When to use:
# When you need unique values
# Remove duplicates
# 💻 Examples:

s1 = set()               # empty set (not {})
s2 = set([1, 2, 2, 3])   # duplicates removed
s3 = set("aabbcc")

print(s2)  # {1, 2, 3}

# {}  # ❌ this is dictionary, not set

# Remove duplicates
# Fast membership check

# 🔹 4. dict() – Create a Dictionary
# ✅ When to use:
# When you need key-value pairs
# Real-world structured data
# 💻 Examples:

d1 = dict()  

d2 = dict(name="Rahul", age=21)

d3 = dict([("a", 1), ("b", 2)])

print(d2)  # {'name': 'Rahul', 'age': 21}

# 🔥 Key Difference (Very Important)

a = {}      # dictionary
b = set()   # set

# 🎯 When to Choose What?
# Need	Use
# Ordered + changeable	list()
# Ordered + fixed	tuple()
# Unique values	set()
# Key-value mapping	dict()