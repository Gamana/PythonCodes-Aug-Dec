class A:
    def show(self):
        print("This is A")

class B(A):
    def show(self):
        super().show()   # calling parent method
        print("This is B")

b = B()
b.show()
#This is A.  , This is B

print("----------super() with Constructor (__init__)--------------")

class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        print("B constructor")
        super().__init__()

b = B()

print("----------Multiple Inheritance - methods calling--------------")

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D() # D B C A
d.show()