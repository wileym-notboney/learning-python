# ABOUTME: 'home devices' command group — list and inspect HA entities
# ABOUTME: Fetches all states from the HA API and displays them

import typer

from home_cli.client import get_client
from home_cli.models import device_from_dict

app = typer.Typer(help="List and inspect Home Assistant devices")


@app.command("list")
def list_devices(
    domain: str = typer.Option(None, "--domain", "-d", help="Filter by domain (e.g. light, sensor)"),
):
    """List all devices, optionally filtered by domain."""
    # TODO (Day 7): implement this command
    # Hint: use get_client(), call GET /api/states, loop over results
    # Use device_from_dict() to convert each dict to a Device object
    # Print: entity_id | state | friendly_name
    # If domain is provided, only show entities where device.domain() == domain
    raise NotImplementedError("Implement me in Day 7!")
