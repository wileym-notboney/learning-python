# Python Syntax Cheatsheet

## Variables & Types

```python
name = "bedroom light"    # str
brightness = 200          # int
temp = 21.5               # float
is_on = True              # bool

type(name)                # <class 'str'>
int("42")                 # convert str → int
str(42)                   # convert int → str
float("3.14")             # convert str → float
```

## Strings

```python
s = "hello"
s.upper()                 # "HELLO"
s.lower()                 # "hello"
s.strip()                 # remove leading/trailing whitespace
s.split(".")              # ["hello"] — split on delimiter
s.replace("l", "r")      # "herro"
len(s)                    # 5
f"Device: {name}"         # f-string interpolation
```

## Lists

```python
items = [1, 2, 3]
items[0]                  # 1 (first)
items[-1]                 # 3 (last)
items.append(4)           # add to end
items.remove(2)           # remove by value
len(items)                # 3
items[1:3]                # [2, 3] — slice
sorted(items)             # sorted copy
```

## Dictionaries

```python
d = {"key": "value", "num": 42}
d["key"]                  # "value"
d.get("missing", "default")  # safe access with fallback
d["new_key"] = "new"     # add or update
d.keys()                  # all keys
d.values()                # all values
d.items()                 # key-value pairs (for loops)
```

## Control Flow

```python
if x == "on":
    ...
elif x == "off":
    ...
else:
    ...

for item in items:
    ...

for key, value in d.items():
    ...

while condition:
    ...
    break     # exit loop
    continue  # skip to next iteration
```

## List Comprehensions

```python
# [expression for item in iterable if condition]
lights = [d for d in devices if d["type"] == "light"]
names = [d["name"] for d in devices]
```

## Functions

```python
def my_function(param, optional="default"):
    return param + optional

result = my_function("hello", " world")
```

## Classes

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def double(self):
        return self.value * 2

    def __str__(self):
        return f"MyClass({self.value})"

obj = MyClass(10)
obj.double()   # 20
print(obj)     # MyClass(10)
```

## Imports

```python
import os
import json
import httpx

from dotenv import load_dotenv
from my_module import my_function
```

## Files

```python
with open("file.json", "w") as f:
    json.dump(data, f, indent=2)

with open("file.json", "r") as f:
    data = json.load(f)
```

## Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()
value = os.environ.get("MY_VAR")
```

## Error Handling

```python
try:
    result = risky_function()
except ValueError as e:
    print(f"Bad value: {e}")
except Exception as e:
    print(f"Something went wrong: {e}")
```

## Useful Built-ins

```python
len(items)           # length
range(5)             # 0,1,2,3,4
enumerate(items)     # (0, item), (1, item), ...
zip(a, b)            # pair up two lists
sorted(items)        # sorted list
round(3.14159, 2)    # 3.14
max(items)           # largest
min(items)           # smallest
```
