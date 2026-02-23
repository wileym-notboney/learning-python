# Day 4 — Worksheet

---

## Part 1: Write a Basic Function

Write a function called `format_device` that takes a `name` and `state`
and returns the string `"name: STATE"` (state in uppercase):

```python
def format_device(________, ________):
    return ________

print(format_device("bedroom light", "on"))   # bedroom light: ON
print(format_device("kitchen fan", "off"))    # kitchen fan: OFF
```

---

## Part 2: Default Parameters

Add a default value so `state` defaults to `"unknown"` if not provided:

```python
def format_device(name, state=________):
    return f"{name}: {state.upper()}"

print(format_device("office fan"))          # office fan: UNKNOWN
print(format_device("bedroom light", "on")) # bedroom light: ON
```

---

## Part 3: Return Values

Write a function `parse_entity` that takes an entity dict and returns
the `friendly_name` and `state` as two separate values:

```python
def parse_entity(entity):
    name = ________
    state = ________
    return ________, ________

entity = {
    "entity_id": "light.bedroom",
    "state": "on",
    "attributes": {"friendly_name": "Bedroom Light"}
}

name, state = parse_entity(entity)
print(name)   # Bedroom Light
print(state)  # on
```

---

## Part 4: Functions That Call Functions

Write a function `summarize_entity` that calls `parse_entity` internally
and returns a formatted string:

```python
def summarize_entity(entity):
    name, state = ________
    return ________

print(summarize_entity(entity))   # Bedroom Light is ON
```

---

## Part 5: Modules

Create a file called `device_helpers.py` in this folder. Move
`format_device` and `parse_entity` into it. Then in a new file called
`main.py`, import and use them:

```python
# main.py
from device_helpers import ________, ________

entity = {"entity_id": "light.bedroom", "state": "on", "attributes": {"friendly_name": "Bedroom Light"}}
print(format_device("bedroom light", "on"))
name, state = parse_entity(entity)
print(name, state)
```

---

## Reflection

1. What's the difference between `print()` and `return` inside a function?

2. Why is it useful to split code into modules?

3. What happens if you call a function with the wrong number of arguments?
