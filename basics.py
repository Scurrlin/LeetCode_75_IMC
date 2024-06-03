# Basics

# Variables are placeholders for storing data in a computer program. They have a
# name and a value associated with them. In Python, you don't need to explicitly
# declare variable types; they are dynamically typed. You can assign values to
# variables using the assignment operator `=`.

x = 5
name = "John"

# Data types define the type of data that a variable can hold. Common data types
# include integers, floating-point numbers, strings, booleans, lists, tuples,
# dictionaries, sets, and more.

age = 25                # Integer
height = 6.2            # Float
name = "Alice"          # String
is_student = True       # Boolean

# Loops are used to execute a block of code repeatedly until a certain condition
# is met. Python supports two main types of loops: `for` loops and `while`
# loops.

# for loop

for i in range(5):
    print(i)

# while loop

i = 0
while i < 5:
    print(i)
    i += 1

# Conditionals are used to make decisions in a program based on certain
# conditions. In Python, you can use `if`, `elif` (short for "else if"), and
# `else` statements to control the flow of your code.

x = 10

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Functions are blocks of reusable code that perform a specific task. They help
# in organizing code into manageable chunks and promote code reuse. In Python,
# you can define functions using the `def` keyword.

def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# Classes are blueprints for creating objects. They allow you to define new data
# types with their own attributes (variables) and methods (functions).
# Object-oriented programming (OOP) is a key paradigm in Python, and classes are
# central to it.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(
            "Hello, my name is "
            + self.name
            + " and I'm "
            + str(self.age)
            + " years old."
        )

person1 = Person("Alice", 25)
person1.greet()