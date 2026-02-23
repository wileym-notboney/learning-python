# Day 3 — Data Structures

## What You're Learning Today

Lists, dictionaries, and sets — the three workhorses of Python data storage.
Every real program uses these constantly. Home Assistant's API sends all its
data in JSON, which Python reads as dictionaries and lists.

## Why This Matters for `home-cli`

A real HA API response looks like this:

```json
[
  {
    "entity_id": "light.bedroom",
    "state": "on",
    "attributes": {
      "brightness": 200,
      "friendly_name": "Bedroom Light"
    }
  },
  {
    "entity_id": "sensor.temperature",
    "state": "21.5",
    "attributes": {
      "unit_of_measurement": "°C",
      "friendly_name": "Temperature"
    }
  }
]
```

That outer `[...]` is a **list**. Each `{...}` inside is a **dict**.
`"attributes"` is a dict nested inside a dict. Today you learn to read and
write all of this.

## Concepts

### Lists — ordered collections

```python
devices = ["bedroom light", "kitchen sensor", "office fan"]

# Access by position (zero-indexed)
print(devices[0])    # bedroom light
print(devices[-1])   # office fan (last item)

# Add and remove
devices.append("bathroom sensor")
devices.remove("office fan")

# Length
print(len(devices))  # 3

# Slicing — get a chunk
print(devices[0:2])  # ['bedroom light', 'kitchen sensor']
```

### Dictionaries — key-value pairs

```python
device = {
    "name": "bedroom light",
    "state": "on",
    "brightness": 200
}

# Access by key
print(device["name"])      # bedroom light
print(device["state"])     # on

# Add or update a key
device["color_temp"] = 4000
device["state"] = "off"

# Safe access (no crash if key missing)
temp = device.get("color_temp", "unknown")

# Loop over a dict
for key, value in device.items():
    print(f"{key}: {value}")
```

### Nested structures — the real world

```python
entity = {
    "entity_id": "light.bedroom",
    "state": "on",
    "attributes": {
        "brightness": 200,
        "friendly_name": "Bedroom Light"
    }
}

# Drill into nested dicts
print(entity["attributes"]["friendly_name"])   # Bedroom Light
print(entity["attributes"]["brightness"])       # 200
```

### Sets — unique values only

```python
states = {"on", "off", "on", "unavailable", "off"}
print(states)  # {'on', 'off', 'unavailable'} — duplicates removed
```

## Today's Goal

Parse a list of fake HA entities (dicts) and extract specific information from them.
