Python project that demonstrate the usage of various Numpy operations, including `np.in1d`, `np.intersect1d`, `np.where`, boolean indexing, conditional slicing, slicing, `np.ones()`, `np.zeros()`, and `np.ones_like()`. This project uses a `nptyping` library to provide type hints for Numpy ndarray objects.

# Python Numpy NDArray Operations

This Python module provides examples of using Numpy's static NDArry operations, including set operations, conditional operations, and array creation functions, with type annotations using `nptyping`.

## Features

* Check if elements of one array are present in another using `np.in1d`.
* Find the common elements between two arrays with `np.intersect1d`.
* Apply conditional logic to find indexes or elements with `np.where`.
* Use boolean indexing for filtering elements.
* Perform conditional slicing on arrays.
* Utilize basic slicing techniques.
* Create arrays with default values using `np.ones()`, `np.zeros()`, and `np.ones_like()`

## Requirements

* Python 3.8+
* numpy
* nptying

To install the necessary libraries, run

```
pip install numpy nptying
```

## Usage

The module `ndarray_operations.py` contains functions demonstrating each feature. Type hints using `nptyping` are provided for better code readability and maintenance

### np.in1d

```
from nptyping import NDArray
from numpy as np

def elements_in_array(arr1: NDArray, arr2: NDArray) -> NDArray:
    return np.in1d(arr1, arr2)
```

### np.intersect1d

```
def intersection_of_arrays(arr1: NDArray, arr2: NDArray) -> NDArray:
    return np.intersect1d(arr1, arr2)
```

### np.where

```
def elements_where_condition(arr: NDArray, condition) -> NDArray:
    return np.where(condition(arr))
```
### Boolean Indexing

```
def boolean_filter(arr: NDArray, filter_condition) -> NDArray:
    return arr[filter_condition(arr)]
```

### Conditional Slicing

```
def conditional_slice(arr: NDArray, start: int, end: int, condition) -> NDArray:
    return arr[start:end][condition(arr[start:end])]
```

### Slicing

```
def slice_array(arr: NDArry, slice_range: slice) -> NDArray:
    return arr[slice_range]
```

### Array Creation Functions

```
def create_arrys(shape: tuple) -> tuple:
    ones_array = np.ones(shape)
    zeros_array = np.zeros(shape)
    ones_like_array = np.ones_like(ones_array)

    return ones_array, zeros_array, ones_like_array
```

## Testing

To test the functions run the following command

```
python ndarray_operations.py
```

Ensure that you have some test arrays and conditions setup in the script to demonstrate the usage of the function.

## References

The following resources provide additional information on nptyping and its usage for type hinting with Numpy arrays:

* [nptyping on PyPI](https://pypi.org/project/nptyping/) - Official PyPI listing of nptyping. (Shared by Sir Zia Khan at 5:54 AM, 11/3/2023)

* [nptyping functions overview on Snyk Advisor](https://snyk.io/advisor/python/nptyping/functions/nptyping.NDArray) - A comprehensive overview of nptyping.

* NDArray functions. (Shared by Sir Zia Khan at 5:59 AM, 11/3/2023)

* [Stack Overflow: Advantages of nptyping.NDArray over np.ndarray](https://stackoverflow.com/questions/76105551/for-type-hinting-purposes-what-are-the-advantages-of-np-typing-ndarrray-over-np) - A Stack Overflow discussion on the benefits of using nptyping.NDArray for type hinting. (Shared by Sir Zia Khan at 6:25 AM, 11/3/2023)

* [nptyping User Documentation](https://github.com/ramonhagenaars/nptyping/blob/master/USERDOCS.md#Quickstart) - The Quickstart section of the nptyping user documentation on GitHub. (Shared by Sir Zia Khan at 6:51 AM, 11/3/2023)

Please note that the information was provided by Sir Zia Khan and the timestamps reflect when the information was communicated.