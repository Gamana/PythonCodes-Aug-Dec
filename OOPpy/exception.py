# a = int(input("Enter value of a"))
# b = int(input("Enter value of a"))
# c = [1, 2, 3]

# try:
#     result = a / b
#     print("Result: ", result)
# except (ZeroDivisionError,ValueError, IndexError, NameError ) as e:
#     print("Error occurred:" , e)
# except:
#     print("Error occurred")
# finally:
#     print("Execution completed !")


#Custom Exception

class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter the marks"))

    if marks < 0 or marks >100:
        raise InvalidMarksError("Marks should be between 0 to 100")

    print(f"Marks is : {marks}")
except InvalidMarksError as e:
    print("Custom Error " , e)


#Example

print("Program Started")
try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin":
        raise Exception("Invalid username")
    
    if password != "1234":
        raise Exception("Invaild Password")
    
    print("Login Successful")

except Exception as e:
    print("Login failed: ", e)
finally:
    print("Program ended")