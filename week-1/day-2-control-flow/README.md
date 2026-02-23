# Day 2 — Control Flow

## What You're Learning Today

How to make decisions in code and repeat actions. `if`/`elif`/`else` lets
your program choose different paths. Loops let it repeat work without you
writing the same line twenty times.

## Why This Matters for `home-cli`

Your Home Assistant has dozens of devices. To show only lights that are on,
or only climate sensors, you need to make decisions and filter:

```python
if device["state"] == "on":
    print(f"{device['name']} is on")

for device in all_devices:
    if device["type"] == "light":
        print(device["name"])
```

That's exactly what today covers.

## Concepts

### if / elif / else

```python
state = "on"

if state == "on":
    print("Device is active")
elif state == "unavailable":
    print("Device is offline")
else:
    print("Device is off")
```

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal |
| `<=` | less than or equal |

### Logical Operators

```python
# and — both must be true
if state == "on" and brightness > 100:
    print("Bright light is on")

# or — at least one must be true
if state == "on" or state == "unavailable":
    print("Device needs attention")

# not — flip the truth
if not state == "on":
    print("Device is off")
```

### for loops

```python
devices = ["bedroom light", "kitchen light", "living room light"]

for device in devices:
    print(f"Checking {device}...")
```

### while loops

```python
attempts = 0
while attempts < 3:
    print(f"Attempt {attempts + 1}")
    attempts = attempts + 1
```

### List Comprehensions

A compact way to build a list using a loop and optional filter:

```python
all_devices = ["bedroom light", "kitchen sensor", "living room light"]

# Get only the lights
lights = [d for d in all_devices if "light" in d]
# → ["bedroom light", "living room light"]
```

## Today's Goal

Write code that loops through a list of devices and prints only the ones
that match a given state or type.
