# Day 4 — Functions & Modules

## What You're Learning Today

Functions let you name a block of code and reuse it. Modules let you split
code across files. Together they're how you go from a script to a real program.

## Why This Matters for `home-cli`

Without functions, your CLI would be one giant script with repeated code
everywhere. With functions, each command (`lights`, `sensors`, `scene`) becomes
its own named block:

```python
def turn_light(room, state):
    # all the logic for this one thing
    ...

def get_sensor(sensor_type):
    # all the logic for this one thing
    ...
```

Clean, testable, reusable.

## Concepts

### Defining and Calling Functions

```python
def greet(name):
    print(f"Hello, {name}!")

greet("boney-m")   # Hello, boney-m!
```

### Parameters and Return Values

```python
def brightness_percent(brightness):
    return round((brightness / 255) * 100)

pct = brightness_percent(200)
print(pct)    # 78
```

### Default Parameters

```python
def describe_device(name, state="unknown"):
    return f"{name} is {state}"

print(describe_device("bedroom light", "on"))   # bedroom light is on
print(describe_device("office fan"))            # office fan is unknown
```

### Multiple Return Values

```python
def parse_entity_id(entity_id):
    parts = entity_id.split(".")
    return parts[0], parts[1]   # returns a tuple

domain, name = parse_entity_id("light.bedroom")
print(domain)  # light
print(name)    # bedroom
```

### Modules — splitting code into files

If you have a file `helpers.py` with a function in it, you can use it
in another file:

```python
# helpers.py
def format_state(state):
    return state.upper()

# main.py
from helpers import format_state

print(format_state("on"))   # ON
```

### The `if __name__ == "__main__":` pattern

This line means "only run this code if this file is being run directly,
not imported by another file":

```python
def main():
    print("Running!")

if __name__ == "__main__":
    main()
```

## Today's Goal

Refactor yesterday's parser into functions, then split it into two files:
one for the helper functions, one for the main script.
