# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# extends User object


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # You can overwrite methods
    # def greeting(self):
    #     return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Initialize user object
cj = User('CJ Nour', 'cj@gmail.com', 21)
cj.has_birthday()
# print(cj.greeting())

# Initialize customer
janet = Customer('Janet Johnson', 'janet@yahoo.com', 34)
janet.set_balance(500)
print(janet.greeting())
