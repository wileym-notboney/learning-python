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
