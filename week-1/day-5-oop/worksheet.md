# Day 5 — Worksheet

---

## Part 1: Define a Class

Write a `Device` class with:
- An `__init__` that takes `entity_id` and `state`
- A method `is_on()` that returns `True` if state is `"on"`
- A method `domain()` that returns the domain part of entity_id (e.g. `"light"`)

```python
class Device:
    def __init__(self, ________, ________):
        self.entity_id = ________
        self.state = ________

    def is_on(self):
        return ________

    def domain(self):
        return ________

bedroom = Device("light.bedroom", "on")
print(bedroom.is_on())    # True
print(bedroom.domain())   # light
```

---

## Part 2: Add __str__

Add a `__str__` method to `Device` that returns `"light.bedroom [ON]"`:

```python
def __str__(self):
    return ________

print(bedroom)   # light.bedroom [ON]
```

---

## Part 3: Create Multiple Instances

```python
devices = [
    Device("light.bedroom", "on"),
    Device("light.kitchen", "off"),
    Device("sensor.temperature", "21.5"),
]

# Loop and print only the ones that are on
for device in devices:
    ________
```

---

## Part 4: Inheritance

Create a `Light` class that inherits from `Device` and adds:
- A `brightness` attribute (0-255)
- A `brightness_percent()` method

```python
class Light(________):
    def __init__(self, entity_id, state, brightness):
        super().__init__(________, ________)
        self.brightness = ________

    def brightness_percent(self):
        return ________

bedroom_light = Light("light.bedroom", "on", 200)
print(bedroom_light.brightness_percent())   # 78
print(bedroom_light.is_on())               # True
print(str(bedroom_light))                  # light.bedroom [ON]
```

---

## Reflection

1. What is `self`? Why does every method have it as the first parameter?

2. What does `super().__init__()` do?

3. When would you use inheritance vs. just having two separate classes?
