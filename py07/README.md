## Python Static Typing for Dictionaries

The creation of dictionaries in Python using static typing. We will explore dictionaries with different hashable key types and values of type `any`, `optional` and `Union`, Additionally, we'll use dictionaries comprehensions and demonstrate swapping keys and values.

### Table of Content

1. Setting up Static typing
2. Creating Dictionaries
    * Using `Any` type
    * Using `optional` type
    * Using `Union` type
3. Dictionaries Comprehensions
4. Swapping Keys and values

### Setting up Static Typing
To use static typing in python., we'll need to import the required types from the typing module. For this guide we're specifically interested in `Any`, `optional` and `Union`.

```
from typing import Any, Optional, Union
```

### Creating Dictionaries
#### Using `Any` type
Any is the most flexible type. It can represent any type at all.  Here's how to create a dictionary with keys of any hashable type and values of any type.

```
from typing import Dict

my_dic: Dict[Any, Any] = {
    10: "Ten",
    "seven": 7,
    (1, 2, 3): [1, 2, 3]
}
```

#### Using `Optional` type
`Optional` is a shorthand for a value that can either be a specific type or `None`.

```
from typing import Dict

my_optional_dic: Dict[Any, Optional[int]] = {
    1: "one",
    "seven": None,
    (1, 2, 3): [1, 2, 3]
}
```

#### Using `Union` type
`union` type allows us to specify that a value can be one of several types.

```
from typing import Dict

my_union_dic: Dict[Any, Union[int, str]] = {
    1: "one",
    "seven": None,
    (1, 2, 3): [1, 2, 3]
}
```

#### Dictoinary comprehension
Dictionary comprehensions provide a concise way to create a dictionary.

```
squared_number = { i: i**2 for i in rang(5)}
```

#### Swapping Keys and Values
To swap keys and values of a dictionary

```
swaped_dict = { v: k for k, v in my_dict.items()}
```
