# Generator function - big data
def gen_func():
    yield 1
    yield 2
    yield 3 

gen = gen_func()
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
# print(next(gen)) # ?

#Normal function - small data
def normal():
    return [2, 4, 6]

print(normal())

print("---------------------------")

