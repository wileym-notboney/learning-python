# ABOUTME: Entry point for the home-cli application
# ABOUTME: Registers all command groups and exposes the 'home' command

import typer

from home_cli.commands import devices, lights, scenes, sensors

app = typer.Typer(
    name="home",
    help="Control your Home Assistant smart home from the terminal.",
    no_args_is_help=True,
)

app.add_typer(devices.app, name="devices")
app.add_typer(lights.app, name="lights")
app.add_typer(sensors.app, name="sensors")
app.add_typer(scenes.app, name="scene")


if __name__ == "__main__":
    app()
