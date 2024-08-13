# create a class called person with attribute name and age create an object of
# the class and print its attributes.
# class Person:
#     name = "ali"
#     age = 20
#
#
# jan = Person()
# print("the name of the person is :", jan.name)
# print("the age of the person is:", jan.age)

# Add a method called greet to the person class that prints a greeting message
# including the person's name
#
#
# class Person:
#     age = 20
#     name = "jan"
#
#     def greet(self, name):
#         self.name = name
#         return f'hello {Person.name} and how are you'
#
#
# khan = Person()
# print(khan.greet("khan"))


# Create a class called car with attributes make,model,and year. include a method
# to print out the car's details.

# class Car:
#     make = "japan"
#     model = "Toyota"
#     year = 2023

#     @staticmethod
#     def details():
#         return f'this car is made in {Car.make} and the model is {Car.model} it made in {Car.year}'


# corolla = Car()
# print(corolla.details())

# Create a class circle with a methode to compute the area. initialize the class
# with the radius
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         print(3.14 * (self.radius ** 2))
#
#
# cir = Circle(10)

# Create a class rectangle with methods to compute the area and perimeter. initialize
# the class with the length and width.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area_rectangle(self):
#         return self.width * self.length
#
#
# first_rectangle = Rectangle(10,20)
# print(first_rectangle.area_rectangle())

# Create a base class Animal with a method speak. Create two derived classes Dog and cat
# that override the speak method.
#
# class Animal:
#     def speak(self):
#         return "The sound of all animal"
#
#     def Dog(speak):
#         return "the sound of the Dog is wak wak wak"
#
#     def Cat(speak):
#         return "the sound of the cat is meow meow meow"
#
#
# pape = Animal()
# print(pape.speak())
# print(pape.Cat())
# print(pape.Dog())

# Create a base class shape with method area. Create a derived classes square and triangle that
# implement the area method
# class Shape:
#     def area(self):
#         return "The area of the Shapes"
#
#
# class Square(Shape):
#     pass
#
#
# class Triangle(Shape):
#     pass
#
#
# pio = Shape()
# print(pio.area())
#
#
# jan = Square()
# print(jan.area())
#
# khan = Triangle()
# print(khan.area())

# Create a class employee with attribute name and salary. create a derived class
# manager with an additional attribute department.
# class Employee:
#     name = "hasib"
#     salary = 20000
#
#
# class Manager(Employee):
#     department = "managing"
#
#
# emp1 = Employee()
# print(emp1.name)
# print(emp1.salary)
#
# emp2 = Manager()
# print(emp2.salary)
# print(emp2.department)

# Create a base class vehicle with a method drive. create derive classes bike and truck
# that override the drive method.
# class Vehicle:
#     def drive(self):
#         return "you can drive the car and airplane"
#
#
# class Bike(Vehicle):
#     def drive(self):
#         return 'you can drive Bike'
#
#
# really = Vehicle()
# print(really.drive())

# tin = Bike()
# print(tin.drive())

# Create a base class Bird with a method fly. create derived classes Eagle
# and penguin. override the fly method in penguin to indicate that penguin cannot fly.
#
# class Bird:
#     def Fly(self):
#         return 'The most of Bird can fly'
#
#
# class Eagle:
#     def Fly(self):
#         return 'Eagle can fly that it is fly'
#
#
# class Penguin:
#     def Fly(self):
#         return 'Penguin can not fly'
#
#
# pen = Bird()
# print(pen.Fly())
#
# khan = Eagle()
# print(khan.Fly())
#
# jan = Penguin()
# print(jan.Fly())

# Create class Account with private attribute balance. provide public methods to deposit
# and withdraw money.
#
# class Account:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def Deposit(self, mount):
#         self.__balance += mount
#
#     def Withdraw(self, money):
#         self.__balance -= money
#
#     def get(self):
#         return self.__balance
#
#
# person = Account(10000)
# person.Deposit(2000)
# person.Withdraw(5000)
# print(person.get())

# create a class Book with private attribute title,author,and pages. provide
# public methods to get and set these attributes.
# class Book:
#     __title = "ali"
#     __pages = 100
#     __author = "layla"
#
#     def display(self):
#         self.__author = Book.__author
#         self.__title = Book.__title
#         self.__pages = Book.__pages
#
#     def get(self):
#         return self.__title, self.__pages, self.__author
#
#     def setter(self, Title, Author, PAGES):
#         self.__title = Title
#         self.__author = Author
#         self.__pages = PAGES
#
#
# pin = Book()
# print(pin.get())
# pin.setter("magical world","hasib jalal",210)
# print(pin.get())

# create a class laptop with private attributes brands, price, and model.provide
# a method to apply a discount and a method to display laptop details.
#
# class Laptop:
#     def __init__(self, brands, price, model):
#         self.__model = model
#         self.__price = price
#         self.__brands = brands
#
#     def get(self):
#         return 'The detail of the laptop:',"model:", self.__model, "price:",self.__price, "brands:",self.__brands
#
#     def discount(self,money_of_discount):
#         if money_of_discount <= self.__price:
#             self.__price -= money_of_discount
#         else:
#             return 'that is false'
#
#
# person = Laptop("MICROSOFT",20000,"DELL")
# print(person.get())
# print(person.discount(2000))
# print(person.get())

# create a class Bank Account with private attributes Account_number and balance.
# provide methods to deposit, withdraw, and check the balance
#
# class BankAccount:
#     __Account_number = 2304
#     __balance = 1000000
#
#     def Account(self):
#         self.__Account_number = BankAccount.__Account_number
#         self.__balance = BankAccount.__balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def withdraw(self,amount):
#         self.__balance -= amount
#
#     def check_balance(self):
#         return self.__balance
#
#
# info = BankAccount()
# print(info.check_balance())
#
# info.deposit(10000)
# info.withdraw(20000)
# print(info.check_balance())

# create a class student with private attribute name, grade,and age. provide method
# to get and set these attributes and a method to display the student's details.

# class Student:
#     __name = "Tamim"
#     __grade = 90
#     __age = 30
#
#     def set(self, name, grade, age):
#         Student.__age = age
#         Student.__name = name
#         Student.__grade = grade
#
#     def get(self):
#         return Student.__name, Student.__grade, Student.__age
#
#     def display(self):
#         return f"The name of the person is {self.__name} and the age of the person is {self.__age} and the grade is {self.__grade}"
#
#
# pin = Student()
# print(pin.get())
# pin.set("omid",100,18)
# print(pin.get())
# print(pin.display())
# create a class Library with attribute name and books (a list of Book objects)
# provide methods to add and remove books.
# class Library:
#     def __init__(self):
#         self.name = "center library"
#         self.books = ["new world", "dead", "forest", "brain", "methods of study"]
#     def add_book(self, new_book, book):
#         if new_book and book in self.books:
#             print('this book is in library we can not add this book')
#
#         else:
#             self.books.append(book)
#             self.books.append(new_book)
#
#     def remove_books(self, new_book, book):
#         if new_book and book in self.books:
#             self.books.remove(book)
#             self.books.remove(new_book)
#         else:
#             print("we can not remove this because it is not in our library")
#
#     def display(self):
#         return self.books
#
#
# bik = Library()
# print(bik.display())
# bik.add_book("dead","brain")
# print(bik.display())
# bik.remove_books("brain","dead")
# print(bik.display())
# from os import remove


# create a class School with attribute name and student (a list of student object).
# provide methods to add and remove students.

# class School:
#     name = "malady"
#     students = ["malad", "ahmad", "samim", "tamim", "jawid", "romal", "sultan", "samir", "shamrize", "wali", "mansor"]
#     @staticmethod
#     def add_students(student):
#         if student not in School.students:
#             School.students.extend(student)
#         else:
#             print("This student is include you cannot assign this student")
#
#     @staticmethod
#     def remove_student(student):
#         if student in School.students:
#             School.students.remove(student)
#         else:
#             print("this student is not in our School you cannot remove this")
#
#
# School.add_students('alim')
# School.remove_student("tamim")
# print(School.students)

# create a class team with attribute name and members (a list of person of objects). provide
# a methods to add and remove members.

# class Team:
#     def __init__(self):
#         self.name = "player of football"
#         self.members = ["farhad", "fayaz", "basid", "hameid","obaid"]
#
#     def add_members(self, member):
#         if member not in self.members:
#             self.members.append(member)
#         else:
#             print("we have this member")
#
#     def remove_member(self, member):
#         if member in self.members:
#             self.members.remove(member)
#         else:
#             print("this person is not our member we can not remove this")
#
#
# info = Team()
# info.add_members("mahmood")
# info.add_members("farhad")
# info.remove_member("razaq")
# print(info.name)
# print(info.members)

# create a class company with attribute name and employees (a list of employee objects).
# provide method to add and remove employees.

# class Company:
#     name = "baheer"
#     employees = ["ahmad", "karim", "khalid", "shazad", "amin"]
#
#     @staticmethod
#     def add_employee(employee):
#         if employee not in Company.employees:
#             Company.employees.append(employee)
#         else:
#             print("this employee is in our company we can not register it two time")
#     @staticmethod
#     def remove_employee(employee):
#         if employee in Company.employees:
#             Company.employees.remove(employee)
#         else:
#             print("we don't have this employee and we can not remove this")
#
# Company.add_employee("korosh")
# Company.remove_employee("amin")
# print(Company.employees)

# create a class Zoo with attribute name and animals (a list of Animal objects). provide a method
# to add and remove the animal.
# class Zoo:
#     name = "center Zoo"
#     animals = ["tiger", "cat", "lion", "wolf", "zebra", "eagle", "monkey", "duck", "cow"]
#     @staticmethod
#     def add_animal(animal):
#         if animal not in Zoo.name:
#             Zoo.animals.append(animal)
#         else:
#             print("we have this animal in the zoo")
#
#     @staticmethod
#     def remove_animal(animal):
#         if animal in Zoo.animals:
#             Zoo.animals.remove(animal)
#
#         else:
#             print("there is no animal with this name")
#
#
# Zoo.add_animal("snake")
# Zoo.remove_animal("cat")
# print(Zoo.animals)

# create a class file Manager to read from and write file.

# class FileManager:
#     @staticmethod
#     def write_operation():
#         a = open("Book.txt", 'w')
#         a.write("Book is a good friend to help us to find good way")
#         a.close()
#         return "That is right it work"
#
#     @staticmethod
#     def read_operation():
#         b = open("School.txt", 'r')
#         b.close()
#         return "That is right it work"
#
#
# print(FileManager.write_operation())
# print(FileManager.read_operation())

# Create a class Log with methods to write error messages to a log file.

# class Log:
#     @staticmethod
#     def create_file():
#         b = open("log.txt", 'w')
#         b.write("I want to log in to this site")
#         b.close()
#         return 'this is work'
#
#     @staticmethod
#     def write_error_massages():
#         try:
#             a = open("log.txt", 'r')
#             a.close()
#             return 'this file is exist'
#         except FileNotFoundError:
#             return "this file is not exist please check again"
#
#
#
# print(Log.create_file())
# print(Log.write_error_massages())

# create a class config that read configuration settings from a file and provides a methods to access
# these settings.

# class Config:
#     def __init__(self, config_file):
#         self.config_file = config_file
#         self.setting = {}
#         self.read_config()
#
#     def read_config(self):
#         try:
#             with open(self.config_file,'r') as f:
#                 for line in f:
#                     line = line.strip()
#                     if line and not line.startswith("#"):
#                         key,value=line.split('=',1)
#                         self.setting[key.strip()]=value.strip()
#         except FileNotFoundError:
#             print(f"config file'{self.config_file}' not found")
#         except Exception as e:
#             print(f"Error reading config file: {str(e)}")
#     def get(self, key):
#         return self.setting.get(key)
#     def set(self, key, value):
#         self.setting[key] = value
#     def save(self):
#         try:
#             with open(self.config_file,'w') as f:
#                 for key, value in self.settings.items():
#                     f.write(f"{key}={value}\n")
#             print(f"config saved to '{self.config_file}'")
#         except Exception as e:
#             print(f"Error saving config file:{str(e)}")
#     def display(self):
#         print("Current configuration")
#         for key, value in self.setting.items():
#             print(f"{key}={value}")
# if __name__ == "__main__":
#     config = Config('config.txt')
#
# config.display()
# print("value of 'timeout'",config.get('timeout'))
# config.set('timeout',5000)
# config.display()
# config.save()

# create a class database that connect to a database and provide methods to eexecute
# queries handle exceptions if the file the connection fails.
# import sqlite3
# class Database:
#     def __init__(self, db_name):
#         self.db_name = db_name
#         self.connection = None
#         self.cursor = None
#     def connect(self):
#         try:
#             self.connection = sqlite3.connect(self.db_name)
#             self.cursor = self.connection.cursor()
#             print(f"Connected to sqlite database:{self.db_name}")
#         except sqlite3.Error as e:
#             print(f"Error connecting to sqlite database:{e}")
#     def disconnect(self):
#         if self.connection:
#             self.connection.close()
#             print(f"Disconnected from sqlite database:{self.db_name}")
#         else:
#             print("NOt connected to any database")
#     def execute_query(self, query):
#         try:
#             if not self.connection:
#                 raise sqlite3.Error("Database connection is closed")
#
#                 self.cursor.execute(query)
#                 self.connection.commit()
#         except:
#             print("Query executed successfully")
#
#     def fetch_results(self, query):
#         try:
#             if not self.connection:
#                 raise sqlite3.Error("Database connection is closed")
#                 self.cursor.execute(query)
#                 rows = self.cursor.fetchall()
#                 return rows
#         except sqlite3.Error as e:
#             print(f"Error fetching result:{e}")
#             return None
#
# if __name__ == '__main__':
#     db = Database('example.db')
#     db.connect()
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     age INTEGER);"""
#     db.execute_query(create_table_query)
#     insert_query = """
#     INSERT INTO users (name,age) VALUES ('alice',30);"""
#     db.execute_query(insert_query)
#     select_query = """
#     SELECT * FROM users;
#     """
#     result = db.fetch_results(select_query)
#     if result:
#         for row in result:
#             print(row)
#     db.disconnect()

# create a class report that generates a report from data in a file. provide methods to handle
# exception if the file does not exist or cannot be read.
#
# class Report:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.data = None
#
#     def read_data(self):
#         try:
#             with open(self.file_name,'r') as file:
#                 self.data = file.read()
#                 print(f"Data read successfully from {self.file_name}")
#         except FileNotFoundError:
#             print(f"File '{self.file_name}' not found")
#         except IOError as e:
#             print(f"Error reading file '{self.file_name}':'{e}'")
#     def generate_report(self):
#         if self.data:
#             lines = self.data.splitlines()
#             num_lines = len(lines)
#             print(f"report generate from {self.file_name}")
#             print(f"number of lines :{num_lines}")
#             for i,line in enumerate(lines,start=1):
#                 print(f"Line {i}: {line}")
#         else:
#             print("NO data available to generate a report. read data first using read_data() methods.")
#
# if __name__ == '__main__':
#     report_file = "example.txt"
#     report = Report(report_file)
#     report.read_data()
#     report.generate_report()

# CREATE a class ticket for a movie theater with attributes movie_name, seat_number, and price.
# provide methods to display ticket detail and apply discounts.

# class Ticket:
#     def __init__(self, movie_name, seat_number, price):
#         self.movie_name = movie_name
#         self.seat_number = seat_number
#         self.price = price
#
#     def display_detail(self):
#         return f" the name of the movie is {self.movie_name} the seat number is  {self.seat_number} and the price is {self.price}"
#
#     def apply_discount(self, percentage):
#         self.price = int(self.price-((percentage/100) * self.price))
#         return self.price
# person = Ticket("magical world",23,5000)
# person.apply_discount(50)
# print(person.display_detail())

# create a class shoppingcart with methods to add, remove, and display items. each item should
# be an object of a class item with attribute name and price.
# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Shoppingcart:
#     def __init__(self):
#         self.items = []
#     def add_item(self, item):
#         self.items.append(item)
#         print(f"{item.name} added to the cart.")
#
#     def remove_item(self, item_name):
#         for item in self.items:
#             if item.name == item_name:
#                 self.items.remove(item)
#                 print(f"{item.name} removed from the cart.")
#             else:
#                 print(f"{item.name} is not in cart.")
#     def display(self):
#         if not self.items:
#             print("your shopping cart is empty.")
#         else:
#             print("item is in your shopping cart.")
#             for item in self.items:
#                 print(f"{item.name}:item price $ {item.price}")
#
# if __name__ == '__main__':
#     apple = Item("apple",2)
#     banana = Item("banana",3)
#     orange = Item("orange",5)
#     cart = Shoppingcart()
#     cart.add_item(apple)
#     cart.add_item(banana)
#     cart.add_item(orange)
#     cart.remove_item(apple)
#     print(cart.display())
#

# create a class restaurant with attribute name and menu(a list of item objects).
# provide methods to add and remove items from the menu.

# class Restaurant:
#     menu = ['bargar', 'rice', 'meatball', 'juice', 'water', 'tea']
#     name = "king bargar"
#     @staticmethod
#     def add_to_menu(item):
#         if item not in Restaurant.menu:
#             menu = Restaurant.menu.append(item)
#         else:
#             print("we have this item in menu")
#     @staticmethod
#     def remove_from_menu(item):
#         if item in Restaurant.menu:
#             menu = Restaurant.menu.remove(item)
#         else:
#             print("this is not in list")
#
#
#
# print(Restaurant.name)
# print(Restaurant.menu)
# Restaurant.add_to_menu("rice")
# Restaurant.add_to_menu("meat")
# print(Restaurant.menu)

# Create a class flight with attribute flight_number, destination, and passengers (a list of person
# objects). provide methods to add and remove passengers.

# class Flight:
#     passengers = ['ali', 'jan', 'ahmad', 'khan', 'rashid']
#     def __init__(self, flight_number, destination):
#         self.flight_number = flight_number
#         self.destination = destination
#         # self.passengers = Flight.passengers
#     def add_passenger(self, name):
#         self.passenger = Flight.passengers.append(name)
#
#     def remove_passenger(self, name):
#         self.passenger = Flight.passengers.remove(name)
#     def display_passengers(self):
#         return self.passengers
#
# person = Flight(12, 230)
# person.add_passenger('Tariq')
# person.remove_passenger('khan')
# print(person.display_passengers())

# create a class hotel with attribute name and rooms(alist of room objects). each room
# should have attributes room_number and is_occupied. provide methods to book and check
# out rooms.

# class Room:
#     def __init__(self,room_number, is_occupied=False):
#         self.room_number = room_number
#         self.is_occupied = is_occupied
#
#     def __str__(self):
#         return f"Room {self.room_number} {('occupied') if self.is_occupied else ('vacant')}"
#
# class Hotel:
#     def __init__(self, name, num_rooms):
#         self.name = name
#         self.rooms = [Room(room_number) for room_number in range(1, num_rooms+1)]
#
#     def __str__(self):
#         return f"{self.name} Hotel \n" + '\n'.join(str(room) for room in self.rooms)
#
#     def find_room(self, room_number):
#         for room in self.rooms:
#             if room.room_number == room_number:
#                 return room
#         return None
#     def book_room(self,room_number):
#         room = self.find_room(room_number)
#         if room:
#             if room.is_occupied:
#                 print(f"Room{room_number} is already occupied")
#             else:
#                 room.is_occupied = True
#                 print(f"Room{room_number} has been successfully booked.")
#
#     def checkout_room(self, room_number):
#         room = self.find_room(room_number)
#         if room:
#             if room.is_occupied:
#                 room.is_occupied = False
#                 print(f"checkout successful for room {room_number}")
#             else:
#                 print(f"Room {room_number} is already vacant")
#         else:
#             print(f"Rooms {room_number} does not exist in this hotel.")
# if __name__ == '__main__':
#     hotel = Hotel("grand hotel",10)
#     print(hotel)
#     hotel.book_room(3)
#     hotel.book_room(5)
#     hotel.checkout_room(3)
#     print("\n After operation :\n")
#     print(hotel)

# create a class counter app that uses tkinter to create a simple counter GUI with increment and
# decrement buttons.
#
# from tkinter import *
# from tkinter import ttk
# class CounterApp(Tk):
#     def __init__(self):
#         super(CounterApp, self).__init__()
#         self.title("the counter app")
#         self.minsize(500,600)
#         self.counter = 0
#         self.button()
#
#     def decrement(self):
#         if self.counter >= 1:
#             self.counter -= 1
#             self.label.configure(text=f"the number is {str(self.counter)}",font=("Helvetica",48))
#         elif self.counter < 1:
#             self.button2.configure(state="disable")
#
#     def increment(self):
#         self.counter += 1
#         self.label.configure(text=f"The Number is {str(self.counter)}",font=("Helvetica", 48))
#
#     def button(self):
#         self.label =ttk.Label(self, text=f"The Number is {str(self.counter)}")
#         self.label.grid(column=2,row=0)
#
#         self.button1 = ttk.Button(self, text="increment",command= self.increment)
#         self.button1.grid(column=5,row=0)
#
#         self.button2 = ttk.Button(self, text="decrement",command=self.decrement)
#         self.button2.grid(column =7,row=5)
#
#
#
# root = CounterApp()
# root.mainloop()

# create a class ToDOApp that uses tkinter to create a to-do list GUI where users can add and remove tasks.
# import tkinter as tk
# from tkinter import messagebox
#
# class ToDoApp:
#     def __init__(self,root):
#         self.root = root
#         self.root.title("ToDo list app")
#         frame = tk.Frame(root)
#         frame.pack(pady=10)
#         self.task_listbox = tk.Listbox(frame, width=50,height=10,selectmode=tk.SINGLE)
#         self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
#         scrollbar = tk.Scrollbar(frame)
#         scrollbar.pack(side=tk.RIGHT, fill= tk.Y)
#         self.task_listbox.config(yscrollcommand=scrollbar.set)
#         scrollbar.config(command=self.task_listbox.yview)
#         self.task_entry = tk.Entry(root, width=50)
#         self.task_entry.pack(pady=10)
#         add_button = tk.Button(root, text="add task",command=self.add_task)
#         add_button.pack(side=tk.LEFT,padx=10)
#         remove_button = tk.Button(root, text="remove task",command=self.remove_task)
#         remove_button.pack(side=tk.RIGHT,padx=10)
#     def add_task(self):
#         task = self.task_entry.get().strip()
#         if task:
#             self.task_listbox.insert(tk.END,task)
#             self.task_entry.delete(0,tk.END)
#         else:
#             messagebox.showwarning("warning","The task entry is empty.")
#     def remove_task(self):
#         selected_task_index = self.task_listbox.curselection()
#         if selected_task_index:
#             self.task_listbox.delete(selected_task_index)
#         else:
#             messagebox.showwarning("warning","No task selected")
#
# if __name__=='__main__':
#     root = tk.Tk()
#     app = ToDoApp(root)
#     root.mainloop()

# create a class calculator app that uses tkinter to create a simple calculator GUI.

# from tkinter import Tk, Entry, Button ,StringVar
# class Calculator:
#     def __init__(self, master):
#         master.title("Calculator")
#         master.geometry("360x423")
#         master.config(bg="gray")
#         master.resizable(False,False)
#         self.equation = StringVar()
#         self.entry_value = ''
#         Entry(width=17,bg="#ccddff",font=("Arial bold",28),textvariable=self.equation).place(x=0,y=0)
#         Button(width=11,height=4,text=')',relief='flat',bg="black",fg="white",command= lambda:self.show(')')).place(x=0,y=50)
#         Button(width=11, height=4, text='(', relief='flat', bg="black",fg="white",command=lambda: self.show('(')).place(x=90, y=50)
#         Button(width=11, height=4, text='%', relief='flat', bg="black",fg="white", command=lambda: self.show('%')).place(x=180, y=50)
#         Button(width=11, height=4, text='9', relief='flat', bg="black",fg="white", command=lambda: self.show(9)).place(x=0, y=125)
#         Button(width=11, height=4, text='8', relief='flat', bg="black",fg="white", command=lambda: self.show(8)).place(x=90, y=125)
#         Button(width=11,height=4,text='7',relief='flat',bg="black",fg="white",command= lambda:self.show(7)).place(x=180 ,y= 125)
#         Button(width=11, height=4, text='6', relief='flat', bg="black",fg="white", command=lambda: self.show(6)).place(x=0, y=200)
#         Button(width=11, height=4, text='5', relief='flat', bg="black",fg="white", command=lambda: self.show(5)).place(x=90, y=200)
#         Button(width=11, height=4, text='4', relief='flat', bg="black",fg="white", command=lambda: self.show(4)).place(x=180, y=200)
#         Button(width=11, height=4, text='3', relief='flat', bg="black",fg="white", command=lambda: self.show(3)).place(x=0, y=275)
#         Button(width=11,height=4,text='2',relief='flat',bg="black",fg="white",command= lambda:self.show(2)).place(x=180,y=275)
#         Button(width=11, height=4, text='1', relief='flat', bg="black",fg="white", command=lambda: self.show(1)).place(x=90, y=275)
#         Button(width=11, height=4, text='0', relief='flat', bg="black",fg="white", command=lambda: self.show(0)).place(x=90, y=350)
#         Button(width=11, height=4, text='.', relief='flat', bg="black",fg="white", command=lambda: self.show('.')).place(x=180, y=350)
#         Button(width=11, height=4, text='*', relief='flat', bg="black",fg="white", command=lambda: self.show('*')).place(x=270, y=275)
#         Button(width=11,height=4,text='-',relief='flat',bg="black",fg="white",command= lambda:self.show('-')).place(x=270,y=200)
#         Button(width=11, height=4, text='+', relief='flat', bg="black",fg="white", command=lambda: self.show('+')).place(x=270, y=50)
#         Button(width=11, height=4, text='/', relief='flat', bg="black",fg="white", command=lambda: self.show('/')).place(x=270, y=125)
#         Button(width=11, height=4, text='c', relief='flat',fg="white", bg="green", command=lambda: self.clear()).place(x=270, y=350)
#         Button(width=11, height=4, text='=', relief='flat', bg="green",fg="white", command=lambda: self.solve()).place(x=0, y=350)
#     def show(self, value):
#         self.entry_value += str(value)
#         self.equation.set(self.entry_value)
#     def clear(self):
#         self.entry_value = ''
#         self.equation.set(self.entry_value)
#     def solve(self):
#         result = eval(self.entry_value)
#         self.equation.set(result)
#
#
# root = Tk()
# Calculator = Calculator(root)
# root.mainloop()

# create a class login app that uses tkinter to create a login form GUI.
# from tkinter import *
# from tkinter import ttk
#
# class LoginApp(Tk):
#     def __init__(self):
#         super(LoginApp, self).__init__()
#         self.title("the tkinter app")
#         self.geometry("500x600")
#         self.login()
#
#
#     def jan(self):
#         if self.textbox is self.name:
#             self.label.configure(text=f"you successfully login in {self.name}")
#         else:
#             self.label.configure(text="your name please")
#     def login(self):
#         self.name =StringVar()
#         self.label = ttk.Label(self, text="The login site",font=('Arial',20))
#         self.label.grid(column=5,row=8)
#         self.button = ttk.Button(self,text="login",command=self.jan)
#         self.button.grid(column=8,row=20)
#         self.textbox = ttk.Entry(self,width=20,textvariable=self.name)
#         self.textbox.focus()
#         self.textbox.grid(column=5,row=7)
#
#
#
# root = LoginApp()
# root.mainloop()

# create a class weather app that uses tkinter to create a weather information GUI.
import tkinter as tk
from tkinter import messagebox
import random

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("weather app")
        self.city_label = tk.Label(root, text="city")
        self.city_label.pack(pady=(20,5))
        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.pack(pady=(0,10))
        self.get_weather_button = tk.Button(root, text="Get weather",command=self.get_weather)
        self.get_weather_button.pack(pady=10)
        self.weather_info = tk.Label(root, text="")
        self.weather_info.pack(pady=(20,10))

    def get_weather(self):
        city = self.city_entry.get().strip()
        if city:
            temperature = random.randint(-10,35)
            conditions = random.choice(["sunny","cloudy","Rainy","windy","snowy"])
            weather_message = f"Weather for {city}: \n Temperature : {temperature}c \n conditions: {conditions}"
            self.weather_info.config(text= weather_message)
        else:
            messagebox.showwarning("input Error", "please enter a city name")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

