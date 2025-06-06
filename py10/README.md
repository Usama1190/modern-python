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

### Table of Content

1. Pre-defined functions
2. User-defined functions
3. Arguments and parameters
4. Default functions.
5. Optional, positional, and keyword arguments
6. Lambda functions

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
