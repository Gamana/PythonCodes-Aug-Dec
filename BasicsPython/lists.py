#Lists - collection of multiple values stored in a single variable - heterogenous
#odered, mutable, allow duplicates, []

# data = [10, 34.5, "Gamana", True]
# print(data)

# #Accessing data - index starts 0
# print(data[2]) #Gamana
# data[2] = "Chandu"
# print(data)

# #Adding Elements
# numbers = [10, 20, 30, 40]
# print(numbers)
# numbers.append(60) #end
# numbers.insert(1, 70) #index
# print(numbers)

# #Remove Elements
# numbers.remove(70) #value
# numbers.pop(4) #index
# print(numbers)

# print(len(numbers)) #4

# numbers.append(100)
# for num in numbers:
#     print(num, end=" ")

# #extend()
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# newlist = list1 + list2
# print(newlist)
# list1.extend(list2)
# print(list1) #[1, 2, 3,4, 5, 6]

# list3 = [4,6, 3, 1, 9]
# print(list3)
# list3.sort() #ascending order
# list3.reverse() #descending
# print(list3)

# words = input().split()
# print(words)

fruits = ["apple", "Mango", "Banana", "Banana"]
print(fruits.index("Banana")) #2
print(fruits.count("Banana")) #2

fruitslist = fruits.copy()


del fruitslist
print(fruits)
print(fruitslist)
