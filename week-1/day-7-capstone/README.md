# Day 7 — Capstone Build Day

## You Made It

Today you build `home-cli` end to end. Every concept from the week feeds into this:

| Skill | Where it appears |
|-------|-----------------|
| Variables & types | Device state, brightness values |
| Control flow | Routing CLI commands |
| Data structures | Parsing HA JSON responses |
| Functions | Each command is a function |
| Classes | Entity models from Day 5 |
| HTTP & APIs | Calling the HA REST API |
| Modules | Split across files |

## The Capstone Project

The fully scaffolded `home-cli` project lives at `../../home-cli/`.

It already has:
- `pyproject.toml` with all dependencies
- Project structure ready to go
- Placeholder functions for each command
- Tests

Your job today is to implement the actual logic inside each command function.

## Commands to Implement

```bash
home devices list              # list all devices
home lights bedroom on         # turn a light on/off
home lights bedroom status     # show light state
home sensors temperature       # show a sensor reading
home scene "evil tv"           # trigger a scene
```

## The Plan

1. `cd ../../home-cli`
2. `uv sync` — install dependencies
3. Set up your `.env` with `HA_URL` and `HA_TOKEN`
4. Run `uv run home --help` to see the CLI skeleton
5. Work through `src/home_cli/commands/` one file at a time
6. Run tests with `uv run pytest`

## Tips

- Work top-down: get `devices list` working first (it uses `GET /api/states`)
- Each command calls the HA API — reuse the `client.py` module
- The models from Day 5 will help you parse responses cleanly
- Run the actual commands against your real HA to see them work

## You're Done When

```bash
$ home devices list
bedroom light          | on      | Bedroom Light
kitchen light          | off     | Kitchen Light
...

$ home lights bedroom on
Turned on bedroom light

$ home sensors temperature
Temperature: 21.5°C
```

---

## End of Day — Commit Your Work

This day's work lives in `home-cli/` rather than a `my-work/` folder, so the
commit is slightly different.

**Step 1 — Branch off main.**
```bash
git checkout main
git checkout -b day-7-capstone
```

**Step 2 — Stage your work.**
```bash
git add home-cli/src/home_cli/commands/
git add week-1/day-7-capstone/my-work/
```

**Step 3 — Commit.**
```bash
git commit -m "day 7: capstone — home-cli commands implemented"
```

**Step 4 — Ask for your final evaluation.**
Tell Claude Code:
> "evaluate day 7"

This eval is different — it's a full week retrospective. Claude will review
all your day branches, identify the patterns in where you struggled and where
you flew, and give you a Week 2 recommendation (more Python? start a real
project? contribute to something open source?).

> **Tip:** Fill in `my-work/notes.md` with how the capstone felt overall.
> That reflection is the most valuable thing in the whole repo.
