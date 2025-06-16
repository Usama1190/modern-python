Python project that demonstrates the usage of static types with `pandas` and includes a fictional library `pander` which is assumed to be related to the project. Since you mentioned 'pander' which is not a known common Python library as of my last update, I'm treating is as part of the project's scope. If `pander` was mentioned by mistake and you meant to refer to functions within `pandas`, the example will still be valid, with `pander` simply being part of the example project's namespace.

# Python Static Typing with Pander and Pandas

The project demonstrate the use of static typing in Python to work with series and DataFrame objects using a `pandas` library and our custom `pander` module.

## Features

* Creating `pandas` Series from tuples, lists and dictionaries.
* Handling malti-index series.
* Constructing `pandas` DataFrame from various data structures.
* Using `loc`, `iloc`, `at`, and `iat` from data selection.

## Getting Started

To get started with this project, make sure you have Python 3.6 or higher installed. as static typing is a features that is best supported in Python 3.6 onwords.

### Prequisites

* Python 3.6+
* pandas
* numpy

Install the required packages using `pip`,

```
pip install pandas numpy
```

### Usage

Below are example of how to use static typing with `pander` and `pandas` for different data structure.

### Series

### Create with tuple

```
from pander import type_series
from pandas import Series

# static typing enforcement
my_series: Series = type_series.create_series_from_tuple(('a', 'b', 'c', 'd'))
```

### Create with list

```
my_series: Series = type_series.create_series_from_list([1, 2, 3, 4])
```

### Create with Dictionary

```
my_series: Series = type_series.create_series_from_dictionary({'a': 1, 'b': 2})
```

### Multi-Index Series

```
my_series: Series = type_series.create_multiindex_series([('a', 'x'), ('b', 'y'), ('c', 'z')], [1, 2, 3])
```

## DataFrame

### Create with list of lists

```
from pander import type_dataframe
from pandas import DataFrame

my_dataframe: DataFrame = type_dataframe.create_dataframe_from_list_of_lists([[1, 2], [3, 4]])
```

### Create with Numpy Array

```
import numpy as np

my_dataframe: DataFrame = type_dataframe.create_dataframe_from_numpy_array(np.array([[1, 2], [3, 4]]))
```

### Data Selection

`loc`, `iloc`, `at`, and `iat`

```
# select a single row using `loc`

row = my_dataframe.loc[0]

# select a single column using `iloc`

column = my_dataframe.iloc[0]

# select a specific value using `at`

value = my_dataframe.at(0, `column_name`)

# select a specific value using `iat`

value = my_dataframe.at(0, 1)
```

### References

* https://pandera.readthedocs.io/en/stable/index.html
* https://pandas.pydata.org/docs/user_guide/basics.html
* https://docs.python.org/3/library/re.html
