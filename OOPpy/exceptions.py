#Code raise Exception

# print("Program started")
# a = 10 / b #Exception
# print(b)
# print("Thank you")

#Handle Exception
#Example 1
# print("Program started")
# try:
#     a = 10 / 0

# except (ZeroDivisionError) as e:
#     print("An Error occured :", e)

# print("Thank you")

# #Example 2
# print("Program started")
# try:
#     a = 10 / b
# except:
#     print("An Error occured")

# print("Thank you")

# #Example 3
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num # Exception Zer0, valueError
#     print(result)

# except ZeroDivisionError:
#     print("Error, cannot be divided by zero")

# except ValueError:
#     print("Error, only integer value should be given")

# #Generic Block
# except:
#     print("Error is occured")

# #Example 4 - try - except with else, finally block always executes

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num # Exception Zer0, valueError

# except ZeroDivisionError:
#     print("Error, cannot be divided by zero")

# else:
#     print("Division Successful", result)

# finally:
#     print("Program executed")

#Example 5 - raise keyword
age = int(input("Enter the age : "))
if age < 0:
    raise ValueError("Age cannot be negative")

print("Your age is:" , age)

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return number ** 0.5

try:
    result = calculate_square_root(-9)
    print(f"The result is: {result}")
except ValueError as e:
    print(f"Error: {e}")

