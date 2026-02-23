# Day 6 — HTTP, APIs & Files

## What You're Learning Today

How to talk to the internet from Python. HTTP requests, JSON parsing, reading
and writing files, and environment variables for secrets. This is the last
building block before the capstone.

## Why This Matters for `home-cli`

Everything before today was local Python. Starting today (and Day 7) your code
reaches out to Home Assistant over your home network:

```
home-cli → HTTP request → Home Assistant API → JSON response → Python dict
```

The HA REST API uses a long-lived access token for auth, which you'll store
in an environment variable (never hardcode secrets).

## Concepts

### `httpx` — making HTTP requests

```python
import httpx

response = httpx.get("https://httpbin.org/json")
print(response.status_code)   # 200
print(response.json())        # parsed dict
```

With auth headers (like HA requires):
```python
headers = {"Authorization": "Bearer your-token-here"}
response = httpx.get("http://homeassistant.local/api/states", headers=headers)
```

### JSON

```python
import json

# Dict → JSON string
data = {"name": "bedroom light", "state": "on"}
json_string = json.dumps(data)
print(json_string)   # '{"name": "bedroom light", "state": "on"}'

# JSON string → dict
parsed = json.loads(json_string)
print(parsed["name"])   # bedroom light
```

`httpx` handles this automatically with `.json()` — but knowing `json.dumps`/`json.loads`
helps when reading docs.

### Reading and Writing Files

```python
# Write a file
with open("devices.json", "w") as file:
    json.dump(data, file, indent=2)

# Read a file
with open("devices.json", "r") as file:
    loaded = json.load(file)
```

The `with` keyword automatically closes the file when you're done.

### Environment Variables — keeping secrets safe

Never put passwords or API tokens in code. Use environment variables:

```python
import os

token = os.environ.get("HA_TOKEN")
if not token:
    print("Error: HA_TOKEN not set")
    exit(1)
```

In your terminal before running:
```bash
export HA_TOKEN="your-long-lived-access-token"
python your_script.py
```

Or use a `.env` file (with `python-dotenv`):
```
# .env  ← this file is in .gitignore so it never gets committed
HA_TOKEN=your-long-lived-access-token
HA_URL=http://homeassistant.local:8123
```

### HA REST API basics

```
GET  /api/states                → all entities
GET  /api/states/light.bedroom  → one entity
POST /api/services/light/turn_on → call a service
```

All requests need: `Authorization: Bearer <token>` header.

## Today's Goal

Write a script that connects to the real (or simulated) HA API, fetches states,
and saves them to a file.
