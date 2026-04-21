#Program to 

# 1. Square of numbers
# ✅ Without List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num * num)

print(squares)

# ✅ With List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]

print(squares)


# 🔹 2. Odd numbers only
# ✅ Without
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print(odd_numbers)
# ✅ With
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)


# 🔹 3. Convert strings to uppercase
# ✅ Without
names = ["ram", "sam", "john"]
upper_names = []

for name in names:
    upper_names.append(name.upper())

print(upper_names)

# ✅ With
upper_names = [name.upper() for name in names]
print(upper_names)


# 🔹 4. Numbers greater than 10
# ✅ Without
numbers = [5, 12, 8, 20, 3]
result = []

for num in numbers:
    if num > 10:
        result.append(num)

print(result)
# ✅ With
result = [num for num in numbers if num > 10]
print(result)

# 🔹 5. Replace negative numbers with 0
# ✅ Without
numbers = [2, -3, 5, -1, 7]
result = []

for num in numbers:
    if num < 0:
        result.append(0)
    else:
        result.append(num)

print(result)
# ✅ With
result = [0 if num < 0 else num for num in numbers]
print(result)

# 🔹 6. Length of each word
# ✅ Without
words = ["apple", "banana", "kiwi"]
lengths = []

for word in words:
    lengths.append(len(word))

print(lengths)
# ✅ With
lengths = [len(word) for word in words]
print(lengths)