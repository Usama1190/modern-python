# Python Pandas with Static Typing

Common data manipulation operations in Pandas DataFrames using static type hints. These operations include selecting columns, adding, deleting, updating columns, and retriveing DataFrame information. Each section below includes code snippets with type annotations compatible with Python 3.6+

## Installation

Before running the examples, ensure you have Pandas installed in your environment.

```
pip install pandas
```

You can also use Mypy or any other static type checker to validate the type annotations

```
pip install mypy
```

## Selecting Columns form DataFrame

### Select a Single Column

```
import pandas as pd
from typing import Any

# creating a DataFrame

df: pd.DataFrame = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [1.2, 2.4, 3.6]
})

# selecting a single column

col_a: pd.Series = df['A']
```

### Select Multiple Column

```
# selecting a multiple column

col_ab: pd.Series = df[['A', 'B']]
```

## Add, Delete, and Update Columns in DataFrame

### Add New Column

```
# Add a new column

df['D']: pd.Series = df['A'] + df['C']
```

### Delete a Column

```
# deleting a column

del df['B']
```

### Update a Column

```
# updating a column

df['A']: pd.Series = df['A'] * 2
```

## Add Columns Using a Custom Function

```
from typing import Callable

def add_custom_column(df: pd.DataFrame, column_name: str, func: Callable[[pd.DataFrame]], Any) -> None:
    def[column_name] = func(df)

# use the custom function
add_custom_column(df, 'E', lambda x: x['A'] + x['C'])
```
## DataFrames Information Methods

```
# df.info()
df.info()

# df.describe()
df.describe()

# df.head()
df_head: pd.DataFrame = df.head()

# df.tail()
df_tail: pd.DataFrame = df.tail()
```

## Selecting By Position (iloc) and Label (loc)

### Selecting with iloc

```
# selecting rows by position

row_first: pd.Series = df.iloc[0]

# selecting a specific value by row and column position

value_first: Any = df.iloc[0, 0]
```

### Selecting with loc

```
# selecting rows by label

row_label: pd.Series = df.loc[0]

# selecting a specific value by row and column label

value_label: Any = df.loc[0, 'A']
```

## Accessing a Scalar Value with at and iat

```
# accessing a single value by row and column label

scalar_at: Any = df.at[0, 'A']

# accessing a single value by row and column position

scalar_iat: Any = df.iat[0, 0]
```

## Notes

* It is important to install Pandas and a static type checker to make the most out of the static typing features in Python.

* The `Any` type is used for DataFrame elements because Pandas Series can contain hetrogeneous data types, but you may specify more specific type based on your data.
