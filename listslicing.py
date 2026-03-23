numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]

print("Original List:", numbers)

# 1. First 4 elements 5, 10, 15, 20
print("First 4 elements:", numbers[:4])

# 2. Last 4 elements 30, 35, 40, 45
print("Last 4 elements:", numbers[-4:])

# 3. Elements from index 2 to 6 15, 20, 25, 30, 35
print("Index 2 to 6:", numbers[2:7])

# 4. Skip one element 5, 15, 25, 35, 45
print("Every second element:", numbers[::2])

# 5. Every third element 5 20 35
print("Every third element:", numbers[::3])

# 6. Reverse the entire list 45 40 35 30 25 20 15 10 5
print("Reversed list:", numbers[::-1])

# 7. Reverse a portion 40 35 30 25
print("Reverse from index 7 to 3:", numbers[7:3:-1])

# 8. Elements except first two 15, 20, 25, 30, 35, 40, 45
print("Except first two:", numbers[2:])

# 9. Elements except last two 5, 10, 15, 20, 25, 30, 35,
print("Except last two:", numbers[:-2])

# 10. Copy list
copy_list = numbers[:] #[5, 10, 15, 20, 25, 30, 35, 40, 45]
print("Copied list:", copy_list)

# 11. Middle elements 20, 25, 30
print("Middle elements:", numbers[3:6])

# 12. Odd index elements 10 20 30 40
print("Odd index elements:", numbers[1::2])

# 13. Even index elements 5 15 25 35 45
print("Even index elements:", numbers[::2])