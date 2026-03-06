# More Tricky Programs on Python Operators

print("1.", 5 + 2 * 3)   #11             # precedence
print("2.", (5 + 2) * 3) #21s

print("3.", 10 / 4) #2.5
print("4.", 10 // 4) # 2
print("5.", 10 % 4) # 2

print("6.", 2 ** 3 ** 2)  #  512        # right to left

print("7.", True + 5)# 6
print("8.", False * 10) # 0

print("9.", 10 and 0) # 0
print("10.", 10 and 5) # 5 last

print("11.", 0 or 5) # 5
print("12.", 0 or 5 or 10) #5 first

print("13.", not 0) # true 1
print("14.", not 10) # False 0

print("15.", 5 > 3 > 1) #true
print("16.", 5 > 3 < 4) #true

print("17.", 5 == 5.0) #true value
print("18.", 5 is 5.0) #False objects

print("19.", -5 % 3) #1
print("20.", 5 % -3)#-1

x = 10
x += 5
print("21.", x) #15

x *= 2
print("22.", x) #30

print("23.", 4 + 3 * 2 ** 2) #16

print("24.", (4 + 3) * 2 ** 2) #28

print("25.", True == 1) #true
print("26.", False == 0) #true

print("27.", 3 < 5 == True) #false

print("28.", bool(0)) # false
print("29.", bool(-1)) # true

print("30.", not True == False) #true