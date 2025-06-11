# Python Static Type Code Example

## Table of Contents

1. [Multiple Inheritance](#multiple-inheritance)
2. [Function Overloading with @overload Decorator](#function-overloading-with-@overload-decorator)
3. [Method Overloading with @overload Decorator](#method-overloading-with-@overload-decorator)
4. [Method Overriding](#method-overriding)
5. [Polymorphism](#polymorphism)
6. [Using __call__()](#using-__call__())
7. [The `object` Class](#the-object-class)

## Multiple Inheritance

Multiple inheritance allows a class to inherit from more than one base class.

```
class Base1():
    def method(self) -> str:
        return Base1

class Base2():
    def method(self) -> str:
        return Base2

class Derived(Base1, Base2):
    pass

obj = Derived()
print(obj.method())     # output: Base1
```

`Derived` inherits from both `Base1` and `Both2`. Since `Base1` is listed first, its method is the one that gets called.

## Function Overloading with @overload Decorator

Function overloading allows defining multiple versions of a function with different types of parameters.

```
from typing import overload

@overload
def add(x: int, y: int) -> int:
    ...

@overload
def add(x: float, y: float) -> float:
    ...

def add(x, y):
    return x + y

print(add(1, 2))       # output: 3
print(add(1.5, 2.5))   # output: 4.0
```

## Method Overloading with @overload Decorator

Method overloading can be achieved in a similar manner to function overloading.

```
from typing import overload

class Calculator():
    @overload
    def add(self, x: int, y: int) -> int:
        ...

    @overload
    def add(self, x: float, y: float) -> float:
        ...

    def add(self, x, y):
        return x + y

calc = Calculator()

print(calc.add(1, 2))        # output: 3
print(calc.add(1.5, 2.5))    # output: 4.0
```

## Method Overriding

Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.

```
class Animal():
    def speak(self) -> str:
        return 'Some generic animal sound'

class Dog(Animal):
    def speak(self):
        return 'Bark'

myDog = Dog()

print(myDog.speak())     # output: Bark
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass.

```
class Cat(Animal):
    def speak(self):
        return "Meow"

def animal_sound(animal: Animal) -> str:
    return animal.speak()

print(animal_sound(Cat))        # output: Meow
print(animal_sound(Dog))        # output: Bark
```

## Using __call__()

The `__call__()` method allows an object to be called like a function.

```
class Multiplier():
    def __call__(self, x: int, y: int) -> int:
        return x * y

multipy = Multiplier()
print(multiply(3, 4))        # output: 12
```

## The `object` Class

Every class in Python 3 implicity inherits from the object class, which is the base class for all classes.

```
class MyClass():
    pass

obj = MyClass()

print(isinstance(obj, object))      # output: true
```

In this example, `MyClass` implicitly inherits from `object`. so an instance of `MyClass` is also an instance of `object`.

```
### Save to File

Would you like to save this `README.md` content to a file? If so, please provide a file name, and I will save it for you.
```
