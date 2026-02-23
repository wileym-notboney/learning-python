# Day 3 Lab — HA Response Parser

## Goal

Parse a realistic Home Assistant API response (a list of dicts) and extract
useful information from it.

## The Data

Your script will work with this data (paste it at the top of your file):

```python
entities = [
    {
        "entity_id": "light.bedroom",
        "state": "on",
        "attributes": {"brightness": 200, "color_temp": 4000, "friendly_name": "Bedroom Light"}
    },
    {
        "entity_id": "light.kitchen",
        "state": "off",
        "attributes": {"brightness": 0, "friendly_name": "Kitchen Light"}
    },
    {
        "entity_id": "sensor.temperature",
        "state": "21.5",
        "attributes": {"unit_of_measurement": "°C", "friendly_name": "Temperature"}
    },
    {
        "entity_id": "media_player.living_room",
        "state": "playing",
        "attributes": {"media_title": "Dark Side of the Moon", "friendly_name": "Living Room Speaker"}
    },
    {
        "entity_id": "light.office",
        "state": "on",
        "attributes": {"brightness": 150, "friendly_name": "Office Light"}
    },
]
```

## What to Build

A script called `parser.py` that prints this report:

```
=== HA Entity Report ===

All entities (5 total):
  light.bedroom        | on      | Bedroom Light
  light.kitchen        | off     | Kitchen Light
  sensor.temperature   | 21.5    | Temperature
  media_player.living  | playing | Living Room Speaker
  light.office         | on      | Office Light

Lights that are ON (2):
  - Bedroom Light (brightness: 200)
  - Office Light (brightness: 150)

Unique states found: {'on', 'off', '21.5', 'playing'}
```

## Requirements

1. Loop over all entities and print each one in table format
2. Filter and list only lights that are currently `"on"`, with brightness from attributes
3. Collect all unique states using a set
4. Show counts where shown above

## Hints

- `entity_id.split(".")[0]` gives you the domain (e.g., `"light"`)
- Use `.get("brightness", "N/A")` to safely access attributes that might be missing

---

Solution in `solution/solution.py`.

---

## End of Day — Commit Your Work

**Step 1 — Branch off main (do this once at the start of the day).**
```bash
git checkout main
git checkout -b day-3-data-structures
```
If you already created the branch earlier:
```bash
git checkout day-3-data-structures
```

**Step 2 — Stage your work.**
```bash
git add week-1/day-3-data-structures/my-work/
```

**Step 3 — Commit.**
```bash
git commit -m "day 3: data structures — worksheet and lab complete"
```

**Step 4 — Ask for your evaluation.**
Tell Claude Code:
> "evaluate day 3"

> **Tip:** Nested dict access (`entity["attributes"]["friendly_name"]`) trips
> most beginners up. Note in `my-work/notes.md` whether that felt natural or
> not — Day 4 builds directly on top of it.
