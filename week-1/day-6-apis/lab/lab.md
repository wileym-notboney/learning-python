# Day 6 Lab — HA State Fetcher

## Goal

Write a script that pulls live state data from your Home Assistant and saves
it to a local JSON file for offline use.

## What to Build

A script called `fetch_states.py` that does this:

```
$ python fetch_states.py

Connecting to Home Assistant at http://homeassistant.local:8123...
Fetched 147 entities
Saved to states.json

Top 5 entities:
  light.bedroom             | on      | Bedroom Light
  light.kitchen             | off     | Kitchen Light
  sensor.temperature        | 21.5    | Temperature
  media_player.living_room  | playing | Living Room Speaker
  switch.3d_printer         | off     | 3D Printer
```

## Setup

Create a `.env` file in this folder (it's already in `.gitignore`):
```
HA_URL=http://homeassistant.local:8123
HA_TOKEN=your-long-lived-access-token
```

Get your token from HA: Profile → Long-Lived Access Tokens → Create Token

## Requirements

1. Load `HA_URL` and `HA_TOKEN` from environment variables (use python-dotenv)
2. Exit with a clear error message if either is missing
3. Make a GET request to `/api/states` with the Authorization header
4. Save the full response to `states.json`
5. Print the count and a preview of the first 5 entities

## Hints

```python
from dotenv import load_dotenv
load_dotenv()   # loads .env file into environment variables
```

```python
# HA authorization header format:
headers = {"Authorization": f"Bearer {token}"}
```

## Stretch Goal

After fetching, print a breakdown by domain:
```
Domains found:
  light: 12 entities
  sensor: 34 entities
  media_player: 3 entities
  ...
```

---

Solution in `solution/fetch_states.py`.

---

## End of Day — Commit Your Work

**Step 1 — Branch off main (do this once at the start of the day).**
```bash
git checkout main
git checkout -b day-6-apis
```
If you already created the branch earlier:
```bash
git checkout day-6-apis
```

**Step 2 — Stage your work.**
*(Don't commit your `.env` file — it's in `.gitignore` and won't be included.)*
```bash
git add week-1/day-6-apis/my-work/
```

**Step 3 — Commit.**
```bash
git commit -m "day 6: HTTP and APIs — state fetcher complete"
```

**Step 4 — Ask for your evaluation.**
Tell Claude Code:
> "evaluate day 6"

> **Tip:** Tomorrow is capstone day. Note in `my-work/notes.md` anything about
> HTTP, headers, or environment variables that felt shaky — you'll be using all
> of it in `home-cli`.
