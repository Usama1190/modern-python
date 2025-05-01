variables name pural in list

## Python Lists and Their Methods

Lists are one of the most versatile and commonly used data types in Python.

### Table of Contents

Introduction to Lists
Indexing
Slicing
Positive and Negative Indexing
List Methods in Python

### Introduction to Lists

A list in Python is an ordered collection of items. Lists can contain a mix of different data types, including numbers, strings, and other lists. Lists are created by placing the items inside square brackets [], separated by commas.

Example:

```
fruits = ["apple", "banana", "cherry"]
```

### Indexing

You can access individual items in a list using an index. Indices start at 0 for the first item, 1 for the second, and so on.

Example:

```
print(fruits[0])  # Outputs: apple
```

### Slicing

Slicing allows you to obtain a subset of items from a list. The syntax for slicing is list[start:stop:step].

Example:

```
print(fruits[1:3])  # Outputs: ['banana', 'cherry']
```

### Positive and Negative Indexing

Positive Indexing: Starts from the beginning of the list.

Example:

```
print(fruits[1])  # Outputs: banana
```

Negative Indexing: Starts from the end of the list.

Example:

```
print(fruits[-1])  # Outputs: cherry
```

### List Methods in Python

Python lists come with a set of built-in methods:

append(): Adds an element to the end of the list.
clear(): Removes all elements from the list.
copy(): Returns a copy of the list.
count(): Returns the number of elements with the specified value.
extend(): Adds elements from another list (or any iterable) to the current list.
index(): Returns the index of the first element with the specified value.
insert(): Adds an element at a specified position.
pop(): Removes the element at a specified position.
remove(): Removes the first item with the specified value.
reverse(): Reverses the order of the list.
sort(): Sorts the list.
For more details and examples on each method, refer to the official <a href='https://docs.python.org/3/tutorial/datastructures.html#more-on-lists'>Python documentation.</a>
