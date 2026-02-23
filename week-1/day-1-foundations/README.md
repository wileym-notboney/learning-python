# Day 1 — Foundations

## What You're Learning Today

The absolute basics: how Python stores information, what types of data exist,
and how to get input from users and print output back. These are the building
blocks everything else sits on top of.

## Why This Matters for `home-cli`

When your Home Assistant sends back data about a device, it looks like this:

```json
{
  "entity_id": "light.bedroom",
  "state": "on",
  "attributes": {
    "brightness": 200,
    "color_temp": 4000
  }
}
```

Every value in there — `"light.bedroom"`, `"on"`, `200` — is a specific
**type** of data. Python needs to know what type something is before it can
work with it. Today you learn those types.

## Concepts

### Variables
A variable is a named box that holds a value.

```python
device_name = "bedroom light"
is_on = True
brightness = 200
```

### Types
Python has several built-in types:

| Type | Example | What it's for |
|------|---------|----------------|
| `str` | `"bedroom"` | Text |
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `bool` | `True` / `False` | Yes/no values |

### print() and input()
```python
# Output to the terminal
print("Hello, home!")

# Get input from the user
device = input("Which device? ")
print("You chose:", device)
```

### f-strings (formatted strings)
The clean way to put variables inside text:
```python
state = "on"
device = "bedroom light"
print(f"The {device} is {state}")
# → The bedroom light is on
```

### type()
Check what type a value is:
```python
brightness = 200
print(type(brightness))   # <class 'int'>
print(type("bedroom"))    # <class 'str'>
```

## Today's Goal

By end of day: you can write a small Python script that asks the user for a
device name and state, then prints a formatted summary.

## Order of Operations

1. Read through this README
2. Check `resources.md` for supporting material
3. Work through `worksheet.md`
4. Do the lab in `lab/lab.md`
