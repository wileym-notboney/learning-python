# Day 4 Lab — Modular Parser

## Goal

Refactor the Day 3 HA parser into a proper two-file module structure.

## What to Build

Two files:

**`ha_helpers.py`** — contains all the helper functions
**`report.py`** — the main script that imports and uses them

When you run `python report.py` it should produce the same output as Day 3's
solution, but the logic is now cleanly split.

## Requirements for `ha_helpers.py`

Write these functions:

```python
def get_domain(entity_id):
    """Return the domain portion of an entity_id (e.g. 'light' from 'light.bedroom')"""
    ...

def get_friendly_name(entity):
    """Return the friendly_name from an entity's attributes"""
    ...

def is_active_light(entity):
    """Return True if the entity is a light that is currently on"""
    ...

def brightness_percent(entity):
    """Return brightness as a percentage (0-100), or None if not applicable"""
    ...

def collect_unique_states(entities):
    """Return a set of all unique state values across all entities"""
    ...
```

## Requirements for `report.py`

- Import everything from `ha_helpers`
- Use the same entity data from Day 3
- Print the same report as Day 3's solution
- Wrap main logic in `if __name__ == "__main__":`

## Hints

- `"""docstrings"""` — the text between triple quotes is a docstring. It describes
  what the function does. It's good practice; add them to your functions.
- Keep each function focused on one thing

---

Solution in `solution/`.
