# Python Error Handling and File Handling

Error handling techniques in Python, including creating custom errors and dynamic error handling. It also covers file handling with various access modifiers and reading files of different types such as CVS, PDF, Excel, and audio files

## Table of Contents

- [Error Handling](#error-handling)
    - [try-except-else](#try-except-else)
    - [Multiple except blocks](#multiple-except-blocks)
    - [Creating cutom errors](#creating-cutom-errors)
    - [Dynamic error handling](#dynamic-error-handling)

- [File handling with access modifiers](#file-handling-with-access-modifiers)
    - Read mode (r)
    - Read and write mode (r+)
    - Write mode (w)
    - Write and read mode (w+)
    - Append mode (a)
    - Append and read mode (a+)
    - Binary read mode (rb)

- Reading files
    - [Reading CSV files](#reading-csv-files)
    - [Reading PDF files](#reading-pdf-files)
    - [Reading Excel files](#reading-excel-files)
    - [Reading audio files](#reading-audio-files)

## Error Handling
### try-except-else

Using `try`, `except`, and `else` block allows you to handle errors gracefully and execute code when no error occur.

```
def divide(a: float, b: float) ->float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return 0.0
    else:
        print("Divide Successfully")
        return result
```

### Multiple except blocks

You can handle different types of exceptions using multiple `except` blocks.

### Creating cutom errors 
### Dynamic error handling

## File handling with access modifiers
### Read mode (r)
### Read and write mode (r+)
### Write mode (w)
### Write and read mode (w+)
### Append mode (a)
### Append and read mode (a+)
### Binary read mode (rb)

## Reading files
### Reading CSV files
### Reading PDF files
### Reading Excel files
### Reading audio files
