# Day 3 — Worksheet

---

## Part 1: List Operations

```python
devices = ["bedroom light", "kitchen sensor", "office fan", "bathroom light"]
```

Write code to:

```python
# 1. Print the first item
print(________)           # bedroom light

# 2. Print the last item
print(________)           # bathroom light

# 3. Print the number of items
print(________)           # 4

# 4. Add "living room light" to the end
________

# 5. Remove "office fan"
________

# 6. Print the updated list
print(devices)
```

---

## Part 2: Dictionary Access

```python
entity = {
    "entity_id": "light.bedroom",
    "state": "on",
    "attributes": {
        "brightness": 200,
        "color_temp": 4000,
        "friendly_name": "Bedroom Light"
    }
}
```

Write code to print each of these:

```python
# 1. The entity_id
print(________)     # light.bedroom

# 2. The state
print(________)     # on

# 3. The friendly_name (it's nested inside attributes)
print(________)     # Bedroom Light

# 4. The brightness
print(________)     # 200
```

---

## Part 3: Building a Dict

Create a dictionary for a new device called "office light" with state "off",
brightness 0, and entity_id "light.office":

```python
office_light = {
    ________
}
```

---

## Part 4: Looping Over a List of Dicts

```python
entities = [
    {"entity_id": "light.bedroom", "state": "on"},
    {"entity_id": "light.kitchen", "state": "off"},
    {"entity_id": "sensor.temp", "state": "21.5"},
]
```

Write a loop that prints: `light.bedroom: on`, `light.kitchen: off`, etc.

```python
for entity in entities:
    print(________)
```

---

## Part 5: Filtering a List of Dicts

From the `entities` list above, get only the ones where `state == "on"`:

```python
active = [________ for ________ in ________ if ________]
print(active)
```

---

## Reflection

1. What's the difference between a list and a dictionary?

2. Why does Python use zero-based indexing (starting at 0)?

3. When would you use `.get("key", default)` instead of `["key"]`?
