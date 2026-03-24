#Program to 

# 1. Square of numbers
# Without List Comprehension
sqr = [1, 2, 3, 4, 5]
new_sqr = []

for n in sqr:
    new_sqr.append(n * n)
print(new_sqr)

# With List Comprehension
lcnew_sqr = [n * n for n in sqr]
print(lcnew_sqr)

# 2. Odd numbers only
# Without
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers) 
# With
lcodd_numbers = [num for num in numbers if num % 2 != 0]
print(lcodd_numbers)

# 3. Convert strings to uppercase
# Without
names = ["ram", "sam", "john"]
upper_names = []

for name in names:
    upper_names.append(name.upper())

print(upper_names)
# With
lcupper_names = [name.upper() for name in names]
print(lcupper_names)

# 4. Numbers greater than 10
# Without
gnumbers = [5, 12, 8, 20, 3]
result = []

for num in gnumbers:
    if num > 10:
        result.append(num)

print(result)
# With
result = [num for num in numbers if num > 10]
print(result)

# 5. Replace negative numbers with 0
# Without
negnumbers = [2, -3, 5, -1, 7]
result = []

for num in negnumbers:
    if num < 0:
        result.append(0)
    else:
        result.append(num)

print(result)
# With
result = [0 if num < 0 else num for num in numbers]
print(result)

# 6. Length of each word
# Without
words = ["apple", "banana", "kiwi"]
lengths = []

for word in words:
    lengths.append(len(word))

print(lengths)
# With
lengths = [len(word) for word in words]
print(lengths)
