# Day 5 Lab — HA Entity Models

## Goal

Build a class hierarchy that models your Home Assistant entities.

## Classes to Build

### `Device` (base class)
- `__init__(self, entity_id, state, attributes=None)`
- `is_on()` — returns bool
- `domain()` — returns domain string
- `name()` — returns `attributes["friendly_name"]` or entity_id if not set
- `__str__()` — `"Bedroom Light [ON]"`

### `Light(Device)`
- Adds `brightness` (pulled from attributes, default 0)
- `brightness_percent()` — 0-100 int
- `set_brightness(value)` — updates brightness (clamp to 0-255)

### `Sensor(Device)`
- Adds `unit` (from `attributes["unit_of_measurement"]`, default `""`)
- `reading()` — returns `"21.5°C"` style string

### `MediaPlayer(Device)`
- Adds `media_title` (from attributes, default `None`)
- `now_playing()` — returns `"Now playing: Dark Side of the Moon"` or `"Nothing playing"` if None

## Build a `from_entity_dict` Class Method

Add this to `Device` (and override in subclasses where needed):

```python
@classmethod
def from_dict(cls, data):
    """Build a Device from a raw HA entity dict"""
    return cls(data["entity_id"], data["state"], data.get("attributes", {}))
```

This lets you do:
```python
entity_data = {"entity_id": "light.bedroom", "state": "on", "attributes": {...}}
light = Light.from_dict(entity_data)
```

## Test Your Classes

Create instances for at least one of each type, call all their methods,
and print the results.

---

Solution in `solution/models.py`.

---

## End of Day — Commit Your Work

**Step 1 — Branch off main (do this once at the start of the day).**
```bash
git checkout main
git checkout -b day-5-oop
```
If you already created the branch earlier:
```bash
git checkout day-5-oop
```

**Step 2 — Stage your work.**
```bash
git add week-1/day-5-oop/my-work/
```

**Step 3 — Commit.**
```bash
git commit -m "day 5: OOP — entity models complete"
```

**Step 4 — Ask for your evaluation.**
Tell Claude Code:
> "evaluate day 5"

> **Tip:** OOP has the steepest learning curve of the week. If `self` or
> `super().__init__()` still feels like magic, say so in `my-work/notes.md` —
> Day 6 and the capstone use classes heavily so it's worth nailing down.
