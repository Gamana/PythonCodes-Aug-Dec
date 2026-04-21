class A:
    def show(self):
        print("This is A")

class B(A):
    def show(self):
        print("This is B")

class C(A):
    def show(self):
        print("This is C")

class D(B, C):
    pass

# Creating an instance
d = D()
d.show()  # Output: This is B

# Checking the Method Resolution Order
print(D.mro()) 
print(D.__mro__)

# This is B
# D B C A obj
