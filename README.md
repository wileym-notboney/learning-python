# Python Curriculum — boney-m's Week 1

A 7-day beginner Python curriculum built around a real capstone project:
a CLI tool that controls your Home Assistant smart home.

## The Plan

| Day | Topic | What You'll Build |
|-----|-------|-------------------|
| 1 | Foundations — variables, types, print/input | Understand how HA sends you data |
| 2 | Control Flow — if/elif, loops, comprehensions | Filter devices by state and type |
| 3 | Data Structures — lists, dicts, sets | Parse real HA JSON responses |
| 4 | Functions & Modules | Organize CLI commands cleanly |
| 5 | Classes & OOP | Model HA entities as Python objects |
| 6 | HTTP, APIs & Files | Call the HA REST API with `httpx` |
| 7 | Capstone Build Day | Build `home-cli` end to end |

## Capstone: `home-cli`

By end of week you'll be able to run:

```bash
# Turn lights on/off
home lights bedroom off

# Check sensor readings
home sensors temperature

# Trigger scenes
home scene "evil tv"

# List all devices
home devices list
```

## Setup

This project uses `uv` for package management. If you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## How Each Day Works

Each day folder contains:

- **README.md** — What you're learning and why it matters
- **resources.md** — Curated links, videos, and reading
- **worksheet.md** — Exercises to fill in as you learn
- **lab/** — A hands-on coding lab with a solution you can peek at

Start with the README, skim the resources, work through the worksheet, then do the lab.

## Structure

```
learning_python/
├── week-1/
│   ├── day-1-foundations/
│   ├── day-2-control-flow/
│   ├── day-3-data-structures/
│   ├── day-4-functions/
│   ├── day-5-oop/
│   ├── day-6-apis/
│   └── day-7-capstone/
├── cheatsheets/
│   ├── syntax.md
│   └── ha-api-reference.md
└── home-cli/          ← the capstone project lives here
```
