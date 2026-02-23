# ABOUTME: Data models for Home Assistant entities
# ABOUTME: Wraps raw API dicts into Python objects with helpful methods

class Device:
    """Represents any Home Assistant entity"""

    def __init__(self, entity_id: str, state: str, attributes: dict):
        self.entity_id = entity_id
        self.state = state
        self.attributes = attributes

    def domain(self) -> str:
        """Return the entity domain (e.g. 'light' from 'light.bedroom')"""
        return self.entity_id.split(".")[0]

    def name(self) -> str:
        """Return the friendly name, falling back to entity_id"""
        return self.attributes.get("friendly_name", self.entity_id)

    def is_on(self) -> bool:
        """Return True if the device state is 'on'"""
        return self.state == "on"

    def __str__(self) -> str:
        status = "ON" if self.is_on() else self.state.upper()
        return f"{self.name()} [{status}]"

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        """Build a Device from a raw HA API response dict"""
        return cls(
            entity_id=data["entity_id"],
            state=data["state"],
            attributes=data.get("attributes", {}),
        )


class Light(Device):
    """A light entity with brightness and color temperature"""

    @property
    def brightness(self) -> int:
        """Brightness value 0-255"""
        return self.attributes.get("brightness", 0)

    def brightness_percent(self) -> int:
        """Brightness as a 0-100 percentage"""
        return round((self.brightness / 255) * 100)


class Sensor(Device):
    """A sensor entity with a unit of measurement"""

    @property
    def unit(self) -> str:
        """The unit of measurement for this sensor"""
        return self.attributes.get("unit_of_measurement", "")

    def reading(self) -> str:
        """The sensor value with its unit, e.g. '21.5°C'"""
        return f"{self.state}{self.unit}"


def device_from_dict(data: dict) -> Device:
    """Build the right type of Device object based on the entity domain.

    Returns a Light, Sensor, or base Device depending on entity_id prefix.
    """
    domain = data["entity_id"].split(".")[0]
    if domain == "light":
        return Light.from_dict(data)
    if domain == "sensor":
        return Sensor.from_dict(data)
    return Device.from_dict(data)
