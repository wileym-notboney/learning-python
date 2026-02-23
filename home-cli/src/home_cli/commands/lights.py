# ABOUTME: 'home lights' command group — turn lights on/off and check status
# ABOUTME: Calls HA light services via the REST API

import typer

from home_cli.client import get_client
from home_cli.models import Light, device_from_dict

app = typer.Typer(help="Control Home Assistant lights")


@app.command()
def on(room: str = typer.Argument(..., help="Room name, e.g. 'bedroom'")):
    """Turn a light on."""
    # TODO (Day 7): implement this command
    # Hint: entity_id is "light.{room}" (lowercase, spaces → underscores)
    # Call POST /api/services/light/turn_on with {"entity_id": "light.bedroom"}
    raise NotImplementedError("Implement me in Day 7!")


@app.command()
def off(room: str = typer.Argument(..., help="Room name, e.g. 'bedroom'")):
    """Turn a light off."""
    # TODO (Day 7): implement this command
    # Same as on, but POST to /api/services/light/turn_off
    raise NotImplementedError("Implement me in Day 7!")


@app.command()
def status(room: str = typer.Argument(..., help="Room name, e.g. 'bedroom'")):
    """Show the current status of a light."""
    # TODO (Day 7): implement this command
    # GET /api/states/light.{room}
    # Print: name, state, brightness percentage
    raise NotImplementedError("Implement me in Day 7!")
