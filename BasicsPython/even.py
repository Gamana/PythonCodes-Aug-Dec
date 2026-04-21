# Prompt the user to enter a number and store it in num
num = int(input())
k = num

# Initialize a variable to keep track of whether an even digit is found
found_even = False

# Use a while loop to iterate through each digit to find the first even digit
while num > 0:
    digit = num % 10  # Get the last digit
    if digit % 2 == 0:  # Check if the digit is even
        print(f"The last even digit in {k} is {digit}.")
        found_even = True
        break  # Exit the loop once an even digit is found
    num = num // 10  # Remove the last digit from num

# If no even digit was found, print a message
if not found_even:
    print("No even digit found.")