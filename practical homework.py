                                 # The practical homework

# create a class Bank Account with private attributes Account_number and balance.
# provide methods to deposit, withdraw, and check the balance

class Acount:
    def __init__(self, Acount_num, balance):
        self.__Account_num = Acount_num
        self.__balance = balance

    def Depsoite(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def display(self):
        return self.__balance

person = Acount(12, 40000)
person.Depsoite(3000)
person.withdraw(23000)
print(person.display())


# create a class Book with private attribute title,author,and pages. provide
# public methods to get and set these attributes.
class Book:
    def __init__(self, author, title, pages):
        self.__title = title
        self.__pages = pages
        self.__author = author

    def set(self,authors, titles, page):
        self.__title = titles
        self.__pages = page
        self.__author = authors

    def get(self):
        return self.__author, self.__pages, self.__title

person = Book("ali", "world",200)
person.set("jan", "magic", 100)
print(person.get())


# create a class shoppingcart with methods to add, remove, and display items. each item should
# be an object of a class item with attribute name and price.

class Item:
    def __init__(self, name ,price):
        self.name = name
        self.price = price

class Shoppingcart:
    def __init__(self, item):
        self.item = item
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
        else:
            return "we have this thing"

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            return "we can not remove this"

    def display_item(self):
        for i in self.items:
            print(f" this is my {i}")


info = Item("apple", 200)
person = Shoppingcart(info)
person.add_item(info)
person.remove_item(info)
print(person.display_item())


























