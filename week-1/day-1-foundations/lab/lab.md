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

---

## End of Day — Commit Your Work

You've finished Day 1. Save your work to git so it can be evaluated.

**Step 1 — Make sure you're on your day branch.**
If you haven't created it yet, do this now:
```bash
git checkout main
git checkout -b day-1-foundations
```
If the branch already exists:
```bash
git checkout day-1-foundations
```

**Step 2 — Stage your work.**
```bash
git add week-1/day-1-foundations/my-work/
```

**Step 3 — Commit.**
```bash
git commit -m "day 1: foundations — worksheet and lab complete"
```

**Step 4 — Ask for your evaluation.**
Tell Claude Code:
> "evaluate day 1"

Claude will read your work, compare it against the requirements, and update
Day 2's content based on what you need more practice with.

> **Tip:** The more you fill in `my-work/notes.md`, the more useful the
> evaluation will be. Even one bullet point under "Things that confused me"
> helps a lot.
