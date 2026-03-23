t = (1, 3, 6, 7, 8)
print(t)
print(t[1:4]) # 3 6 7
print(t[:3]) # 1 3 6

#         -4       -3     -2    -1
#index.  0.      1.   2.   3
t1 = ("Gamana", 5.4, 100, 'A')
print(t1)
print(t1[0]) #gamana
print(t1[2])
print(t1[-4])

#Immutable
#t1[0] = "Chandu"

t2 = (3 , ) * 3
print(type(t2), t2)

#operations
tup = (1, 2, 3, 4) * 2
print(tup)
print(len(tup)) #4
#concatenation
print(t1 + tup)

#Interview
def name():
    n1 = "Gamana"
    n2 = "Nithin"
    n3 = "Geetha"
    return (n1, n2, n3)

print(name())

# Packing
student = ('Ravi', 20, 'Physics')
print(student)

# Unpacking
name, age, course = student
print(name)
print(age)
print(course)


