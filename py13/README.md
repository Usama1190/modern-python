Basic concepts of Object-Oriented Programming (OOP) in Python, including classes, methods, attributes, class variables and inheritence. It also include example of an `Employee` class and its subclasses `Designer` and `Developer`, demonstrating the use of `super.__init__()` to initialize the parent class

# Object-Oriented Programming in Python

## Table of Content

1. [OOP basic concepts](#oop-basic-concepts)
2. [Classes, Methods and Attributes](#classes-methods-and-attributes)
3. [Class Variables](#class-variables)
4. [Inheritance](#inheritance)
5. [Example: Employee, Designer, and Developer](#example-employee-designer-and-developer)

## OOP basic concepts

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code that maniplates that data. Objects are instences of classes, which can hold both data (attributes) and code (methods).

## Classes, Methods and Attributes

* `Class`: A blue print for creating objects.
* `Method`: A function defined inside a class.
* `Attribute`: A variable that belongs to an object.

### Example: Creating a simple class

```
class Dog:
    def __init__(self, name, age):
        self.name = name               # Attribute
        self.age = age                 # Attribute

    def bark(self):                    # Method
        print("Woof!")
```

## Class Variables

Class variables are shared by all instences of a class. They are set by prefixing a variable with the name of the class

### Example: Using Class Variables

```
class Dog:
    species = "Canis familiaris"       # class instences or variable

    def __init__(self, name, age):
        self.name = name               # Attribute
        self.age = age                 # Attribute

    def bark(self):                    # Method
        print("Woof!")
```

## Inheritance

Inheritence allows a class to inherit attributes and methods from other class.

### Example: Inheriting from Base Class

```
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")
```

## Example: Employee, Designer, and Developer

Here, we define an `Employee` class and two subclasses `Designer` and `Developer`.

### Base Class: Employee

```
class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def dispaly_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Deparment: {self.department}")
```

### Subclass: Designer

```
class Designer(Employee):
    def __init__(self, name, age, department, tool):
        super().__init__(name, age, department)
        self.tool = tool

    def display_info(self):
        super().dispaly_info()
        print(f"Tool: {self.tool}")
```

### Subclass: Developer

```
class Developer(Employee):
    def __init__(self, name, age, department, language):
        super().__init__(name, age, department)
        self.language = language

    def display_info(self):
        super().dispaly_info()
        print(f"Language: {self.language}")
```

### Usage

```
designer = Designer("Alice", 28, "Design", "Photoshop")
developer = Developer("Usama", 25, "Development", "Python")

designer.dispaly_info()
developer.dispaly_info()
```

You can save this content to a `README.md` file in your project directory. It provides a comprehensive guide on the basics of OOP in Python, with examples and explanation for each concept.