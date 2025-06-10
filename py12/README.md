# Python Error Handling and File Handling

Error handling techniques in Python, including creating custom errors and dynamic error handling. It also covers file handling with various access modifiers and reading files of different types such as CVS, PDF, Excel, and audio files

## Table of Contents

- [Error Handling](#error-handling)
    - [try-except-else](#try-except-else)
    - [Multiple except blocks](#multiple-except-blocks)
    - [Creating cutom errors](#creating-cutom-errors)
    - [Dynamic error handling](#dynamic-error-handling)

- [File handling with access modifiers](#file-handling-with-access-modifiers)
    - [Read mode (r)](#read-mode-r)
    - [Read and write mode (r+)](#read-and-write-mode-r)
    - [Write mode (w)](#write-mode-w)
    - [Write and read mode (w+)](#write-and-read-mode-w)
    - [Append mode (a)](#append-mode-a)
    - [Append and read mode (a+)](#append-and-read-mode-a)
    - [Binary read mode (rb)](#binary-read-mode-rb)

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

```
def convert_to_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        print("Invalid Integer!")
        return 0
    except TypeError:
        print("Value must be a string!")
        return 0
```

### Creating cutom errors

You can create custom error classes by inheriting from the base `Exception` class.

```
class NegativeValueError(Exception):
    def __str__(self) -> str:
        return "Value can not be negative"

def sqrt(value: float) -> int:
    if value == 0:
        raise NegativeValueError()
    return value ** 0.5
```

### Dynamic error handling

You can handle errors dynamically by capturing the exception and analyzing it.

```
def dynamic_error_handling(value: str) -> int:
    try:
        return int(value)
    except Exception as e:
        print(f"An error occured: {str(e)}")
        return 0
```

## File handling with access modifiers

### Read mode (r)

Open a file for reading

```
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
```

### Read and write mode (r+)

Opens a file for reading and writing

```
with open('file.txt', 'r+') as f:
    content = f.read()
    print(content)
    f.write("New line")
```

### Write mode (w)

Opens a file for writing, creates the file if it does not exist, and trancates the file if it exist.

```
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
```

### Write and read mode (w+)

Opens a file for writing and reading

```
with open('file.txt', 'w+') as f:
    f.write("Hello, World!")
    f.seek(0)
    content = f.read()
    print(content)
```

### Append mode (a)

Opens a file for appending, creates the file if it does not exist.

```
with open('file.txt', 'a') as f:
    f.write("Appending line")
```

### Append and read mode (a+)

Opens a file for appending and reading.

```
with open('file.txt', 'a+') as f:
    f.write("Appending line")
    f.seek(0)
    content = f.read()
    print(content)
```

### Binary read mode (rb)

Opens a file for binary read mode.

```
with open('file.txt', 'rb') as f:
    content = f.read()
    print(content)
```

## Reading files

### Reading CSV files

You can use the `csv` module to read CSV files.

```
import csv

with open('file.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)
```

### Reading PDF files

You can use the `PyPDF2` library to read PDF files.

```
import PyPDF2

with open('file.pdf', 'rb') as f:
    reader = PyPDF.PdfFileReader(f)
    text = reader.getPage(0).extractText()
    print(text)
```

### Reading Excel files

You can use the `openpyxl` library to read Excel file.

```
import openpyxl

wb = openpyxl.load_workbook('file.xlsx')
sheet = wb.active
cell = sheet['A1']
print(cell.value)
```

### Reading audio files

You can use the `pydub` library to read audio files.

```
from pydub import AudioSegment

audio = AudioSegment.from_file('file.mp3')

print("Channels:", audio.channels)
print("Sample Width:", audio.sample_width)
print("Frame Rate:", audio.frame_rate)
print("Frame Width:", audio.frame_width)
print("Length (ms):", len(audio))
print("Frame Count:", audio.frame_count)
```
