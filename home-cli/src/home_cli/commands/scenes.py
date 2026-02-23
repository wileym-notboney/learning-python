# ABOUTME: 'home scene' command — trigger a Home Assistant scene
# ABOUTME: Calls the scene.turn_on service

import typer

from home_cli.client import get_client

app = typer.Typer(help="Trigger Home Assistant scenes")


@app.command()
def trigger(
    name: str = typer.Argument(..., help="Scene name, e.g. 'evil tv'"),
):
    """Trigger a scene by name."""
    # TODO (Day 7): implement this command
    # Scene entity_id format: "scene.{name}" (lowercase, spaces → underscores)
    # Call POST /api/services/scene/turn_on with {"entity_id": "scene.evil_tv"}
    raise NotImplementedError("Implement me in Day 7!")
