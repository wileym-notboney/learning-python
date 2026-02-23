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
