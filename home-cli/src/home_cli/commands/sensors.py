# ABOUTME: 'home sensors' command group — read sensor values from HA
# ABOUTME: Fetches sensor state and unit of measurement

import typer

from home_cli.client import get_client
from home_cli.models import Sensor, device_from_dict

app = typer.Typer(help="Read sensor values from Home Assistant")


@app.command()
def read(
    name: str = typer.Argument(..., help="Sensor name, e.g. 'temperature'"),
):
    """Read a sensor value."""
    # TODO (Day 7): implement this command
    # GET /api/states/sensor.{name}
    # Print the reading using sensor.reading()
    raise NotImplementedError("Implement me in Day 7!")
