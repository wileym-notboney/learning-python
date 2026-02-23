# Day 2 Lab — Device Filter

## Goal

Write a script that takes a list of devices and lets the user filter them
by state or type.

## What to Build

A script called `filter.py` that works like this:

```
$ python filter.py

=== Device Filter ===
Filter by (state/type): state
State to show (on/off/unavailable): on

Active devices:
  - bedroom light (on)
  - kitchen light (on)

Inactive devices:
  - office fan (off)
  - bathroom sensor (unavailable)
```

## Starter Data

Use this list of devices in your script:

```python
devices = [
    {"name": "bedroom light", "state": "on", "type": "light"},
    {"name": "kitchen light", "state": "on", "type": "light"},
    {"name": "office fan", "state": "off", "type": "fan"},
    {"name": "bathroom sensor", "state": "unavailable", "type": "sensor"},
    {"name": "living room light", "state": "off", "type": "light"},
]
```

## Requirements

1. Ask the user whether to filter by `state` or `type`
2. Ask for the specific value to filter on
3. Use a for loop to separate matching devices from non-matching ones
4. Print both groups with clear labels

## Hints

- Build two lists: `matching` and `others`
- Append to a list with: `my_list.append(item)`
- Loop over the devices and check `device["state"]` or `device["type"]`

## Stretch Goal

Instead of printing matching/non-matching, sort all devices alphabetically
by name and display them with their state.

---

Solution is in `solution/solution.py` — try it yourself first!
