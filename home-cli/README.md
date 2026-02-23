# home-cli

Control your Home Assistant smart home from the terminal.

## Setup

```bash
# Install dependencies
uv sync

# Create .env with your HA credentials
cp .env.example .env
# Edit .env and fill in HA_URL and HA_TOKEN
```

Get a token from HA: **Profile → Long-Lived Access Tokens → Create Token**

## Usage

```bash
# List all devices
home devices list

# Filter by domain
home devices list --domain light

# Lights
home lights on bedroom
home lights off bedroom
home lights status bedroom

# Sensors
home sensors read temperature

# Scenes
home scene trigger "evil tv"
```

## Development

```bash
# Run tests
uv run pytest

# Lint
uv run ruff check src/

# Install in editable mode (so 'home' command works)
uv sync
```

## Project Structure

```
src/home_cli/
├── main.py           # CLI entry point, registers command groups
├── client.py         # HA API client (auth + httpx)
├── models.py         # Device, Light, Sensor classes
└── commands/
    ├── devices.py    # home devices ...
    ├── lights.py     # home lights ...
    ├── sensors.py    # home sensors ...
    └── scenes.py     # home scene ...
```
