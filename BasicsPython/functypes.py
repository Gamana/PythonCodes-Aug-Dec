# No arguments + No return value
def add():
    a = 30
    b = 20
    print( a+b )
add()

# No arguments + Return value
def add():
    c = 10
    d = 10
    return c+d
print(add())

# Arguments + No return value
def add(x, y):
    print(x+y)
add(100,200)

# Arguments + Return value
def add(p, q):
    return p+q
res = add(200, 300)
print(res)

#Write a functions in all 4 types for finding a cube of a number