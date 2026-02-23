# Day 6 — Worksheet

Before starting, install httpx and python-dotenv:
```bash
uv add httpx python-dotenv
```

---

## Part 1: A Simple GET Request

```python
import httpx

response = httpx.get("https://httpbin.org/json")

# 1. Print the status code
print(________)        # 200

# 2. Print the full JSON response (it returns a dict)
print(________)

# 3. Print just the "slideshow" key from the response
data = response.json()
print(________)
```

---

## Part 2: JSON Encode and Decode

```python
import json

device = {
    "entity_id": "light.bedroom",
    "state": "on",
    "brightness": 200
}

# 1. Convert the dict to a JSON string
json_string = ________
print(json_string)

# 2. Parse it back to a dict
parsed = ________
print(parsed["entity_id"])    # light.bedroom
```

---

## Part 3: Write and Read a File

```python
import json

data = [
    {"name": "bedroom light", "state": "on"},
    {"name": "kitchen sensor", "state": "22.1"},
]

# Write to devices.json
with open("devices.json", "________") as f:
    json.dump(________, ________, indent=2)

# Read it back
with open("devices.json", "________") as f:
    loaded = json.load(f)

print(loaded[0]["name"])    # bedroom light
```

---

## Part 4: Environment Variables

```python
import os

# 1. Read the HA_TOKEN environment variable (returns None if not set)
token = ________

# 2. Exit with an error message if it's not set
if not token:
    ________

print(f"Token loaded: {token[:10]}...")   # show first 10 chars only
```

In your terminal, test it:
```bash
export HA_TOKEN="test-token-value"
python worksheet.py
```

---

## Part 5: Calling the HA API (requires your HA token)

If you have your HA URL and token, complete this:

```python
import httpx
import os

url = os.environ.get("HA_URL", "http://homeassistant.local:8123")
token = os.environ.get("HA_TOKEN")

headers = {________: ________}

response = httpx.get(f"{url}/api/states", headers=headers)
entities = response.json()
print(f"Got {len(entities)} entities")
```

---

## Reflection

1. Why should API tokens never be hardcoded in source files?

2. What does `with open(...) as f:` do that `f = open(...)` doesn't?

3. What's the difference between `json.dump()` and `json.dumps()`?
