# Day 2 — Worksheet

---

## Part 1: if/elif/else

Write the `if`/`elif`/`else` chain that prints the right message for each state:
- `"on"` → `"Device is active"`
- `"off"` → `"Device is inactive"`
- `"unavailable"` → `"Device is offline — check connection"`
- anything else → `"Unknown state"`

```python
state = "unavailable"

________
________
________
________
```

---

## Part 2: Logical Operators

Predict what each prints (True or False), then check in the REPL:

```python
brightness = 180
state = "on"

print(state == "on" and brightness > 100)   # ________
print(state == "off" or brightness > 100)   # ________
print(not state == "on")                     # ________
print(brightness >= 180 and brightness <= 255)  # ________
```

---

## Part 3: for loop

Write a for loop that prints each device in this list:

```python
devices = ["bedroom light", "kitchen sensor", "office fan", "living room light"]

# Your loop here:
________
```

Expected output:
```
bedroom light
kitchen sensor
office fan
living room light
```

---

## Part 4: Filtering with a loop

Write a for loop that prints ONLY the items that contain the word "light":

```python
devices = ["bedroom light", "kitchen sensor", "office fan", "living room light"]

for device in devices:
    ________
```

Expected output:
```
bedroom light
living room light
```

---

## Part 5: List Comprehension

Rewrite Part 4 as a one-liner list comprehension:

```python
lights = [________ for ________ in ________ if ________]
print(lights)
```

---

## Part 6: while loop

Write a while loop that counts from 1 to 5, printing each number:

```python
count = ________
while ________:
    print(________)
    ________
```

---

## Reflection

1. When would you use a `while` loop instead of a `for` loop?

2. What's the difference between `=` and `==`?

3. In `home-cli`, when might you need to filter a list of devices?
