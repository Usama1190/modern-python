## Python Control Flow and Typing

Overview of Python's control flow structures including if, if-else, if-elif-else statements. Addiontionally, it covers the use of Python's static type variables, the `union` and `optional` type from the typing module. The zip function with lists, and sorting a list of tuple based on the second tuple index.

### Table of Content

* If Statement
* If-Else Statement
* If-Elif-Else Statement
* Nested If-Else-Elif Statement
* Static Type variables
* Union and Optional Types
* Zip function with List
* Sorting a list of Tuples

### If Statement

```
x: int = 10

if x > 5:
    print('x is greater then 5')
```

### If-Else Statement

```
x: int = 4

if x > 5:
    print("x is greater then 5")
else:
    print("x is not greatre then 5")
```

### If-Elif-Else Statement

```
x: int = 5

if x > 5:
    print("x is greater then 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is not greatre then 5")
```

### Nested If-Else-Elif Statement

```
x: int = 9
y: int = 4

if x > 5:
    if y > 5:
        print("x and y are both greater then 5")
    else:
        print("x is greater then 5 but y is not")
    print("x is greater then 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is not greatre then 5")
```

### Static Type variables

In Python 3.6 and later, you can use static type annotations to indicate the expected type of a variable

```
x: str = "Osama"
y: int = 3
x: float: = 3.14
```

### Union and Optional Types

`union` allows a variables to be one of several types. `Optional` is the shorthand of `union[T, None]`

```
from typing import Union, Optional

def greet(name: Optional[str] = None) -> str:
    if name == None:
        return "Hello Guest"
    else:
        return f"Hello, {name}"

age: Union[int, str] = "Twenty"

print(greet())
print(greet("Osama"))
```

### Zip function with List

The zip function is used to combine two or more iterables.

```
names: list[str] = ["Alice", "Bob", "Charlie"]
ages: list[int] = [25, 35, 30]

zipped = zip(names, ages)

for name, age in zipped:
    print(f"{name} is {age} year old.")

```

### Sorting a list of Tuples

You can sort a list of tuples based on the second tuple index using the sorted function

```
tuples: list[tuple[str, int]] = [("Alice", 30), ("Bob", 25), ("Charlie", 20)]

sorted_tuple = sorted(tuples, key = lamda x: x[1])

print(sorted_tuple)     # 
```