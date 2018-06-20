# PythonBasics

I'm learning Python! 

Python is case-sensitive.

REPL is started by running `python` or `python3`. To exit out of the REPL, run `CTRL-D`.

To run a program thru the python interpreter run 

```python

python3 hello.py

```

Assign variables just by naming them in snake-case like this

```python

first_name = "Frank"
print(first_name, "is learning Python!")

```

Ask input from the user by using 

```python

first_name = input("What is your first name? ")
print(first_name, "is learning Python!")

```

Naming things is hard. Here are [Pythons's naming conventions][pythonNamingConvention].

Functions are created with the `def` keyword and the `{}` are replaced with a `:`

Indention is important in Python

```python

def yell(text): 
  text = text.upper()
  number_of_characters = len(text)
  result = text + "!" * (number_of_characters // 2) 
  print(result)
```

Python uses `try except`  instead of `try catch`.
To raise an excemption use `raise`

[pythonNamingConvention]: https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions