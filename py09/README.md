# Python Looping and Input Techniques

Overview of varies looping structures and input methods in Python, emphasizing static type annotations

## Table of Content

1. While Loop
2. For Loop
3. Control Statement
* break
* continue
* pass
4. Input Functions
5. Command Line Arguments (sys.args)
6. Example

## While Loop

The `while` loop in Python is used for repeated execution as long as an expression is true.

### Syntax

```
while expression:
    # code to be executed
```
### Example

```
counter: int = 0
while counter > 5:
    print('Counter is ', counter)
    counter += 1
```

## For Loop

The `for` loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects

### Syntax

```
for variable in sequence
    # code to be executed
```

### Example

```
numbers: list[int] = [1, 2, 3, 4, 5]

for num in numbers:
    print('Number is:', num)
```
## Control Statement
## break

The `break` statement is used to exit the loop before it has completed its natural cycle.

### Example

```
for i in range(5):
    if i == 3:
        break
    print(i)
```
## continue

The `continue` statement is used to skip the rest of the code inside the loop for the current iteration only.

### Example

```
for i in range(5):
    if i == 3:
        continue
    print(i)
```

## pass

The `pass` statement is a null operation, nothing happens when it executes.

### Example

```
for i in range(5):
    if i == 3:
        pass
    print(i)
```

## Input Functions

The `input` function allows for user input.

### Syntax

```
variable: str = input('prompt message')
```

### Example

```
name: str = input("Enter your name:")

print("Hello, ", name)
```

## Command Line Arguments (sys.args)

`sys.argv` is a list in Python, which contains the command-line arguments pass to the script

### Example

```
import sys

arguments: list = sys.argv

print("Script Name: ", argument[0])
print("First Argument: ", argument[0])
```

## Example

You can find various examples and demonstrating how to use while loop, for loop, control statments, the input function, and command line arguments in Python.