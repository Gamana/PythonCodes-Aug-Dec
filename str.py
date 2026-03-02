a = [1, 2, 3] #lists - seperate
b = a
c = [1, 2, 3]

#is => address
#== => content
print(a is b) #true
print(a is c) #false
print(a == c) #true

s1 = "" #String
res = bool(s1) #T/F
print(res) #True
print(type(res))
