# Python (interpreted language)

Except install dependencies, packages, environment paths, or ides

### Install Anaconda

https://anaconda/downloads

### Google Colab (explore)

https://google-colab 

After installaion open Anaconda prompt (black)

Then look at this like,

(base) C:/Users>_

This is base environment where all packages, and something like this installed

Type python -version (for checking version of python)

(base) C:/Users>python --version
Python 3.12.7

This is the answer of current version of python (3.12.7)

Then write python

(base) C:/Users>python
some information and three greater than symbols
>>>

This symbols represents acitvate the python interpreter

Now you can write the print keyword and round brackets () inside this write double quotation and your name see,

>>>print("John")
John

Code is executed and the result is your name

Then you can call the exit function

>>>exit()

Now you are in the normal terminal

(base) C:\Users>

(base) C:\Users>d:           (move to the directory)

(base) D:\>mkdir PIAIC       (create new folder)

(base) D:\>cd PIAIC          (move to the new folder)

(base) D:\PIAIC>code .       (open vs code)

then create a file like main.py inside this write some code

open anaconda terminal move on to the same directory and run this command

(base) D:\PIAIC>python main.py

keyword python and file name with extension

Jupyter notebook 

extension of jupyter notebook is .ipynb

ipynb (intruptive python node book)

environment or virtual environment

base environment (by default)

create virtual environment

(base) D:\PIAIC>conda create -n python12 python==3.12 -y

(base) D:\PIAIC>conda activate python12

(python12) D:\PIAIC>

create file requirements.txt

numpy or numpy==0.2
pandas
jupyter
mypy

(python12) D:\PIAIC>pip install -r requirements.txt

installation packages

pep8 naming convention

google collab

# Installation

* Anaconda
* vs code

# Hello world
* windows -> Anaconda prompt -> python

```
print("Hello world")

```
* open VScode -> `class1.py`

```
    * install python extension
    * click on run button

mypy is very improtant package

In python static type introduce

In particular variable store particular type

mypy class1.py (check errors in file)
