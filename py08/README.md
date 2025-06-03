## Python Dictionary

How to work with dictionaries in Python, including how to create dictionaries, access values, add key-value pairs, and use various dictionary methods.

### Table of Content

1. Introduction to Dictionaries
2. Creating a Dictionaries
3. Accessing Values
4. Adding Key-Value pairs
5. Dictionary Methods
* clear
* copy
* fromkeys
* get
* items
* keys
* pop
* popitem
* setdefault
* update
* values
6. Conclusion

### Introduction to Dictionaries

Dictionaries in Python are  a collection of key-value pairs. where each key is unique. They are mutable, meaning you can change their content without changing their identity.

### Creating a Dictionaries

You can create a dictionary by enclosing the comma-separated sequence of key-value pairs in curly braces `{}`, with a colon `:` separating the keys and values

```
from typing import Dict

my_dict: Dict[str, int] = { "apple": 7, "banana": 9 }
print(my_dict)
```

### Accessing Values

You can access the value associated with a specific key using the square bracket `[]` notation.

```
value: int = my_dict["banana"]

print(value)   # Output: 9
```

### Adding Key-Value pairs

Adding a key-value pair to the dictionary is straightforward

```
my_dict["cherry"] = 3

print(my_dict)    # Output: { "apple": 7, "banana": 9, "cherry": 3 }
```

### Dictionary Methods

### clear

Remove all the elements from the dictionary

```
my_dict.clear()

print(my_dict)    # Output: {}
```

### copy

Returns a shallow copy of a dictionary

```
copy_dict = my_dict.copy()

print(copy_dict)    # Output: { "apple": 5, "banana": 9, "cherry": 3 }
```

### fromkeys

Create a new dictionary with keys from a sequence and values set to a specified value.

```
sequence = ("apple", "banana", "cherry")

new_dict = dict.fromkeys(sequence, 0)

print(new_dict)    # Output: {"apple": 0, "banana": 0, "cherry": 0}
```

### get

Returns the value for a specified key if the key is in the dictionary.

```
value = my_dict.get("apple", "Not Found")

print(value)     # Output: 5
```

### items

Returns a view object that display's a list of dictionaries key-value tuple pairs.

```
items = my_dict.items()

print(item)     # Ouput: dict_items([("apple", 5), ("banana": 7), ("cherry": 9)])
```

### keys

Returns a view object that displays a list of all the keys in the dictionary.

```
keys = my_dict.keys()

print(keys)   # Output: dict_keys(["apple", "banana", "cherry"])
```

### pop

Remove the elements with the specified key.

```
my_dict.pop("apple")

print(my_dict)   # Output: {"banana": 7, "cherry": 3}
```

### popitem

Removes the last inserted key-value pair.

```
my_dict.popitem()

print(my_dict)     # Output: {"banana": 7}
```
### setdefault

Returns the value of the specified key. If the key does not exist, insert the key, with the specified value.

```
value = my_dict.setdefault("banana", 6)

print(value)   # Output: 5
```
### update

Updates the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.

```
my_dict.update("banana": 1)

print(my_dict)    # Output {"banana": 1}
```
### values

Returns a view object that displays a list of all the values in the dictionary.

```
value = my_dict.values()

print(value)  # Output: dict_values[4]
```

### Conclusion

Dictionary are a versatile way to store and manipulate data in Python. This guide has covered the basis, as well as the veriety of methods that can be used to work with dictionaries.