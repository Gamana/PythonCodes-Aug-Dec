#if
age = 19
if age>=18:
    print("Eligible to vote")

    print("Thank you")

#if - else
age = 10
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")
    print("Thank you")

#if - elif - else
marks = 75
if marks>=90:
    print("Garde A")
elif marks>=70:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("fail")

#nested if 
free_tonight = True
friends_available = False

if free_tonight:
    if friends_available:
        print("Go out for dinner with friends!")
    else:
        print("Order food and watch a movie.")
else:
    print("Continue with assignments.")

#match

day = 6
match day:
    case 1: print("Mon")
    case 2:print("Tue")
    case 3: print("Wed")
    case 4:print("Thu")
    case _: print("Invalid day")

# 3,4,5 - summer 6, 7, 8 - rainy 9,10,11, 12 - winter

month = 14
match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 |10 |11 |12:
        print("Winter")
    case _ : 
        print("Invalid season")

#looping statements for / while

# 0 1 2 3 4
for i in range(5):
    print(i)

i = 0
while i<=4:
    print(i)
    i += 1

#even numbers - 2 4 6 8 10

for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=" ")

#jump control statemenets 1 - 6
#break = 3

for i in range(1, 6):
    if i == 4:
        break
    print(i)

for i in range(0, 6):
    if i == 4:
        continue
    print(i)

def square(n):
    return n * n
print(square(4))

#pass
for i in range(0, 6):
    pass

def add():
    pass
add()
