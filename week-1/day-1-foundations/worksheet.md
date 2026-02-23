# Day 1 — Worksheet

Fill in the blanks. Run the code snippets in your Python REPL (`uv run python`)
to check your answers.

---

## Part 1: Types

What type is each of these values? Write your answer next to each one.

```python
"hello"          # ________
42               # ________
3.14             # ________
True             # ________
"123"            # ________   ← careful, this one is tricky
```

Verify with `type()`:
```python
print(type("hello"))
print(type(42))
```

---

## Part 2: Variables

Assign values to these variables so the `print()` statements produce the
shown output.

```python
device_name = ________
device_state = ________
brightness = ________

print(f"Device: {device_name}")        # Device: kitchen light
print(f"State: {device_state}")        # State: on
print(f"Brightness: {brightness}%")   # Brightness: 75%
```

---

## Part 3: String Operations

Python lets you do math-like operations on strings.

```python
first = "home"
second = "assistant"

# What does this print?
print(first + second)         # ________
print(first + " " + second)  # ________
print(first * 3)             # ________
```

---

## Part 4: Converting Types

Sometimes you need to change a value's type. This is called **casting**.

```python
brightness_str = "200"          # This came from user input (always a string)
brightness_int = int(brightness_str)   # Convert to int

print(brightness_int + 50)     # What prints? ________
print(brightness_str + "50")   # What prints? ________  ← different!
```

---

## Part 5: input()

Write a script that:
1. Asks the user: `Which room?`
2. Asks the user: `What state? (on/off)`
3. Prints: `Setting [room] light to [state]`

```python
room = ________
state = ________
print(________)
```

---

## Reflection

Answer these in plain English (no code needed):

1. Why does Python have different types instead of just storing everything as text?

2. What's the difference between `200` and `"200"` in Python?

3. What would go wrong if you tried to do `brightness + "%" ` when `brightness = 200`?
