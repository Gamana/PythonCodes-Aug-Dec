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

print(D.__mro__)


print("----------------------------------------")

class A:
    def __init__(self):
        print("A is initialized")

class B(A):
    def __init__(self):
        super().__init__()
        print("B is initialized")

class C(A):
    def __init__(self):
        super().__init__()
        print("C is initialized")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D is initialized")

# Creating an instance
d = D()

print("_------------------------------------")

class A:
    pass

class B(A): 
    pass
class C(A): 
    pass

class D(B, C): 
    pass
class E(C): 
    pass

class F(D, E): 
    pass

print(F.mro())

# F D B E C A Obj