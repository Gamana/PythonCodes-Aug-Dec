num = [1, 2, 3, 4]

# for n in num:
#     print(n) # 1 2 3 4
try:
    it = iter(num) #object
    print(next(it)) # 1
    print(next(it)) # 2
    print(next(it)) # 3
    print(next(it)) # 4
    print(next(it)) # ?
except:
    print("No more Items")


class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Create an instance of CountUpTo
counter = CountUpTo(5)

# Use a for loop to iterate through the counter
for number in counter:
    print(number)