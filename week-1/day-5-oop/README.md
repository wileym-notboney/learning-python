# Day 5 — Classes & OOP

## What You're Learning Today

Object-Oriented Programming: how to create your own types by writing classes.
A class is a blueprint. An object is a thing built from that blueprint.

## Why This Matters for `home-cli`

Right now you're storing device info as plain dicts. That works, but a class
lets you bundle the data AND the behavior together:

```python
light = HADevice("light.bedroom", "on", {"brightness": 200})
light.turn_on()
light.set_brightness(150)
print(light.is_on())    # True
```

That's much cleaner than passing dicts everywhere.

## Concepts

### Defining a Class

```python
class Device:
    def __init__(self, entity_id, state):
        self.entity_id = entity_id
        self.state = state

    def is_on(self):
        return self.state == "on"

    def describe(self):
        return f"{self.entity_id} is {self.state}"
```

- `__init__` runs when you create a new object — it's the "setup" method
- `self` refers to the object itself
- Methods are just functions that live inside a class

### Creating Objects (Instances)

```python
bedroom = Device("light.bedroom", "on")
kitchen = Device("light.kitchen", "off")

print(bedroom.is_on())     # True
print(kitchen.describe())  # light.kitchen is off
```

### Attributes

```python
print(bedroom.entity_id)   # light.bedroom
print(bedroom.state)       # on

bedroom.state = "off"      # you can update attributes directly
```

### Inheritance — one class based on another

```python
class Light(Device):
    def __init__(self, entity_id, state, brightness):
        super().__init__(entity_id, state)   # run the parent __init__
        self.brightness = brightness

    def brightness_percent(self):
        return round((self.brightness / 255) * 100)

bedroom_light = Light("light.bedroom", "on", 200)
print(bedroom_light.brightness_percent())  # 78
print(bedroom_light.is_on())               # True — inherited from Device
```

### `__str__` — how an object prints itself

```python
class Device:
    def __str__(self):
        return f"Device({self.entity_id}, {self.state})"

bedroom = Device("light.bedroom", "on")
print(bedroom)    # Device(light.bedroom, on)
```

## Today's Goal

Model your HA entities as classes. Create a `Device` base class and a
`Light` subclass with extra behavior.
