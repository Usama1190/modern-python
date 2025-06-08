## Python Functions

Python functions are a cornerstone of the language, providing modularity and code reusability.

#### Pre-defined Functions

Python comes with a variety of build-in functions, like `len()` that are ready to use without any additional imports.

#### User-defined Functions

User can defined their own functions using the `def` keyword, allowing for customized functionality tailored to specific needs.

#### Arguments and Parameters

Functions can accept inputs in the form of arguments, and these inputs are defined in the function signatures as parameters.

#### Default Functions

Parameters can be given default values, making them optional when the functions is called.

#### Optional, positional, and Keyword Arguments

Functions can accepts for different types of arguments, including functional arguments with default values, positional arguments that depend on order and keyword arguments that are specifeid by name.

#### Lambda Functions

Anonymous functions can be defined on-the-fly using the `lambda` keyword.

By understanding and utilizing these different aspects of Python functions, developer can write cleaner, more efficient, and more maintainable code.

#### Recursive Functions

Functions can solve themselves to solve problems in a recursive manners.

#### Decorators

Functions can be wrapped by other functions to extend their behaviour without modifying their code

#### Functions with Unlimited Arguments

Functions can be designed to accept an arbitrary number of arguments, either as positional arguments or keyword arguments.

### Table of Content

1. Pre-defined functions
2. User-defined functions
3. Arguments and parameters
4. Default functions.
5. Optional, positional, and keyword arguments
6. Lambda functions
7. Recursive functions
8. Decorators
9. Functions with Unlimited Arguments

### Pre-defined functions

Python provides several build-in functions that are readily available for use.

```
# Example of a pre-defined function
result: int = len("Hello, world!")
print(result)    # output: 12
```

### User-defined functions

You can defined your own functions in Python using the `def` keyword.

```
def greet(name: str) -> None:
    print(f"Hello, {name}")

greet("Usama")     # output: Hello, Usama
```

### Arguments and parameters

Parameters are the variables listed inside the parentheses in the function definition, whereas arguments are the values passed to the function when it is called.

```
def add(a: int, b: int) -> int:
    return a + b

result: int = add(5, 9)
print(result)     # output: 14
```

### Default functions.

You can assign default values to parameters, making them optional during a function call.

```
def power(base: int, exponent: int = 2) -> int:
    return base ** exponent

print(power(3))     # output: 9
print(power(3, 3))  # output: 27
```

### Optional, positional, and keyword arguments

#### Optional arguments

Optional arguments are those that have a default value.

```
def greet(name: str = "John") -> str:
    print(f"Hello, {name}")

def()           # output: Hello, John
def("Usama")    # output: Hello, Usama
```

#### Positional arguments

Positional arguments are arguments that need to be included in the proper position and order.

```
def subtract(a: int, b: int) -> int:
    return a - b

result: int = subtract(10, 5)
print(result)              # output: 5
```

#### Keyword arguments

Keyword arguments are arguments passed to a function by explicitly specifying the name of the parameter.

```
def divide(divident: int, divisor: int) -> float:
    return divident / divisor

result: float = divide(divisor=2, divident=10)
print(result)     # output: 5.0
```

### Lambda functions

Lambda functions are anonymous functions defined using the `lambda` keyword.

```
square: callable = lambda x : x * x

print(square(3))      # output: 9
```

### Recursive functions

A recursive function is a function that calls itself.

```
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorail(n - 1)

result: int = factorail(5)

print(result)   # 120
```

### Decorators

Decorators are a way to modify or extend the behaviour of a function.

```
def my_decorator(func: Callable) -> callable:
    def wrapper(*args, **kargs) -> None:
        print("something is heppening before the function is called")
        func(*args, **kargs)
        print("something is heppening after the function is called")

    wrapper()

@my_decorator
def say_hello(name: str) -> None:
    print(f"Hello, {name}")

say_hello('Usama')   # output : before func Hello, Usama after func
```

### Functions with Unlimited Arguments

You can define functions that accept an arbitrary number of arguments.

#### Unlimited Positional Arguments

```
def add(*numbers: int) -> int:
    return sun(numbers)

result: int = add(1, 2, 3, 4, 5)

print(result)   # output: 15
```

#### Unlimited Keywords Arguments

```
def print_key_values(**kargs: int) -> None:
    for key, value in kargs.items():
        print(f"{key}: {value}")

print_key_values("name": "John", "age": 26, "country": "usa")
```
