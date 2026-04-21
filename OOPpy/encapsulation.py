class Bank:
    def __init__(self, name, balance):
        self.name = name          # public
        self.__balance = balance      # private

    def display(self):
        print(self.name, self.__balance)


b = Bank("HDFC", 90000)
# print(b.__balance) #Error
print(b._Bank__balance) # Not recomended

# Best Way to access the private variables is using getters and setters

class Bank:
    def __init__(self, balance):
        self.__balance = balance # Private

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")

b = Bank(1000)
print(b.get_balance())   # 1000

b.set_balance(2000)
print(b.get_balance())   # 2000
