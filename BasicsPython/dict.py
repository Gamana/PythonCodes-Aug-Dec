# Word → Meaning
# Key → Value

# Key Features
# Stores data in key-value pairs , ordered (3.7+)
# Unordered (but maintains insertion order in Python 3.7+)
# Mutable (can change values)
# Keys must be unique
# Keys must be immutable (string, number, tuple)

student = {
    "name": "Rahul",
    "age": 21,
    "course": "BCA"
}

# 3. Accessing Values
print(student["name"])   # Rahul
print(student.get("age"))  # 21

# 🔹 4. Adding / Updating Values
student["age"] = 22        # update
student["city"] = "Delhi"  # add new key
print(student)

# 🔹 5. Removing Elements
student.pop("age")      # removes age
del student["course"]   # deletes course
student.clear()         # removes all items

# 🔹 6. Looping Through Dictionary
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)

# 🔹 7. Useful Methods

student.keys()    # returns all keys
student.values()  # returns all values
student.items()   # returns key-value pairs

# 8. Example Program (Simple & Practical)
marks = {
    "Math": 90,
    "Science": 85,
    "English": 88
}

total = 0

for subject, score in marks.items():
    total += score

print("Total Marks:", total)
print("Average:", total / len(marks))

# 1. get() – Safe Access
d = {"name": "Rahul", "age": 21}

print(d.get("name"))        # Rahul
print(d.get("city"))        # None
print(d.get("city", "NA"))  # NA

# 👉 No error if key doesn’t exist

# 🔹 2. keys() – Get All Keys
d = {"a": 1, "b": 2}

print(d.keys())

# dict_keys(['a', 'b'])

# 🔹 3. values() – Get All Values
print(d.values())
# dict_values([1, 2])

# 🔹 4. items() – Key-Value Pairs
print(d.items())

# dict_items([('a', 1), ('b', 2)])

# 🔹 5. update() – Add / Modify

d = {"a": 1}

d.update({"b": 2})
d.update({"a": 10})

print(d)

# {'a': 10, 'b': 2}

# 🔹 6. pop() – Remove Specific Key

d = {"a": 1, "b": 2}

d.pop("a")

print(d)

# {'b': 2}

# 🔹 7. popitem() – Remove Last Item

d = {"a": 1, "b": 2}

d.popitem()
print(d)


# 🔹 8. clear() – Remove All Items

d.clear()
print(d)
# {}

# 🔹 9. copy() – Create Copy
d1 = {"a": 1}
d2 = d1.copy()

d2["a"] = 10

print(d1)  # {'a': 1}
print(d2)  # {'a': 10}

# 🔹 10. setdefault() – Insert if Not Exists
d = {"a": 1}

d.setdefault("b", 2)
d.setdefault("a", 100)

print(d)

# {'a': 1, 'b': 2}


# 🔹 11. fromkeys() – Create Dictionary
keys = ["a", "b", "c"]
s = set(keys)
print(type(s))
print(type(keys))

d = dict.fromkeys(keys, 0)
print(type(d.values()))

# {'a': 0, 'b': 0, 'c': 0}