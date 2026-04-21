print("-------Normal Function--------")
def count_num(n):
    numbers = [] # [1, 2, ..........10 ]
    count = 1
    while count <= n:
        numbers.append(count)
        count+=1
    return numbers

usernum = int(input("Enter the count")) #10

for n in count_num(usernum):
    print(n)

print("-------Generator Function--------")

def count_num(n):
    count = 1
    while count <= n:
        yield count
        count+=1

usernum = int(input("Enter the count")) #10000000000000

for n in count_num(usernum):
    print(n)