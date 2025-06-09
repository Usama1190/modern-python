# Python Try Except

## Table of Content

1. Pass by reference vs pass by value
2. Mutable and immutable variables
3. Runtime error classes
4. Try except else finally block

## Pass by reference vs pass by value

In Python, the way variables are passed to functions can be thought of as "pass by object reference". This means that the function receives a reference to the object, not a copy of object. However, the behaviour can seem like "pass by value" or "pass by refernece" depending on whether the object is mutable or immutable.

### Example: Pass by value (with immutable type)

```
def modify_value(num: int):
    print("Inside function (before modification):", id(num))
    num = 10
    print("Inside function (after modification):", id(num))

x = 5
print("Before function call: ", id(x))
modify_value(x)
print("After function call: ", id(x))
```

In this example, `x` is an interger (which is immutable). When we pass `x` to the function and modify it inside the function, the id (memory address) of `num` inside the function changes, indicating that a new interger object has been created. The `id` of `x` outside the function remain the same.

### Example: Pass by value (with mutable type)

```
def modify_list(num: int):
    print("Inside function (before modification):", id(num))
    num = 10
    print("Inside function (after modification):", id(num))

my_list: list[int] = [1, 2, 3]
print("Before function call: ", id(my_list))
modify_list(my_list)
print("After function call: ", id(my_list))
```

In this example, `my_list` is a list (which is mutable). When we pass `my_list` to the function and modify it inside the function, the `id` of `1st` inside the function remains the same, indicating that the same list object is being modified. The `id` of `my_list` outside the function also remains the same.

## Mutable and immutable variables

Variables in Python can be either mutable or immutable.

* Mutable types: can be changed after they are created. Examples include lists, dictionaries, and sets.

* Immutable types: can not be changed after they are created. Examples include integers, string, float, and tuples

### Example Mutable type

```
my_list = [1, 2, 3]

print("Before modification:", my_list, "id", id(my_list))

my_list.append(4)

print("After modification:", my_list, "id", id(my_list))
```

In this example, the list `my_list` is modified in place, and its id remains the same.

### Example Immutable type

```
my_string = "Hello"

print("Before modification:", my_string, "id", id(my_string))

my_string = my_string + " world"

print("After modification:", my_string, "id", id(my_string))
```

In this example, when we modify `my_string`, a new string object is created, and the `id` of `my_string` is changes.

## Runtime error classes

Python has several build-in error classes to handle runtime errors. Here are examples of some common runtimes errors.

### IndexError

Occures when trying to access an index that is out of range.

```
try:
    my_list = [1, 2, 3]
    print(my_list[3])    # This will raise an IndexError
except IndexError as e:
    print("Caugh an IndexError:", str(e))
```

### ZeroDivisionError

Occures when dividing by zero.

```
try:
    result = 10 / 0    # This will raise an ZeroDivisionError
except ZeroDivisionError as e:
    print("Caugh an ZeroDivisionError:", str(e))
```

## Try except else finally block

The `try-except-else-finally` block in Python is used for exception handling.

* The `try` block contains the code that may raise an exception.
* The `except` block contains the code that is executed if the exception is raised.
* The `else` block contains the code that is executed if no exceptions are raised.
* The `finally` block contains the code that is always executed, regardless of whether the exception is raised.

```
try:
    numerator = 10
    denominator = 2
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError:", str(e))
else:
    print("Division Successfull:", result)
finally:
    print("This block is always executed.")
```
