# Day 1 Lab — Device Status Reporter

## Goal

Write a Python script that acts like a mini Home Assistant status display.
It asks the user for device info and prints a nicely formatted summary.

## What to Build

A script called `status.py` that does this when you run it:

```
$ python status.py

=== Home Assistant Status Reporter ===
Device name: bedroom light
Current state (on/off): on
Brightness (0-255): 200
Color temperature (K): 4000

--- Status Report ---
Device:      bedroom light
State:       ON
Brightness:  200 / 255 (78%)
Color temp:  4000K
```

## Requirements

1. Ask the user for: device name, state, brightness (as a number), color temp (as a number)
2. Print a formatted report
3. Calculate the brightness percentage: `(brightness / 255) * 100`, round to nearest whole number
4. Show state in ALL CAPS in the report

## Hints

- Use `input()` to collect values
- Use `int()` to convert brightness and color_temp from strings to numbers
- Use `round()` to round the percentage
- Use f-strings for all output
- `str.upper()` turns a string to uppercase: `"on".upper()` → `"ON"`

## Stretch Goal

Add a second device. Ask for all the same info for a second device and
print both in the report.

---

When you're done, peek at `solution/solution.py` — but try it yourself first!
