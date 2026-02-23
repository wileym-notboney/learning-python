# ABOUTME: OOP models for Home Assistant entities
# ABOUTME: Demonstrates class inheritance, __str__, and classmethods


class Device:
    """Base class for all Home Assistant entities"""

    def __init__(self, entity_id, state, attributes=None):
        self.entity_id = entity_id
        self.state = state
        self.attributes = attributes or {}

    def is_on(self):
        """Return True if the device state is 'on'"""
        return self.state == "on"

    def domain(self):
        """Return the domain prefix of the entity_id (e.g. 'light')"""
        return self.entity_id.split(".")[0]

    def name(self):
        """Return the friendly name, or entity_id if not set"""
        return self.attributes.get("friendly_name", self.entity_id)

    def __str__(self):
        status = "ON" if self.is_on() else self.state.upper()
        return f"{self.name()} [{status}]"

    @classmethod
    def from_dict(cls, data):
        """Build a Device from a raw HA entity dict"""
        return cls(data["entity_id"], data["state"], data.get("attributes", {}))


class Light(Device):
    """A light entity with brightness support"""

    def __init__(self, entity_id, state, attributes=None):
        super().__init__(entity_id, state, attributes)
        self.brightness = self.attributes.get("brightness", 0)

    def brightness_percent(self):
        """Return brightness as a 0-100 percentage"""
        return round((self.brightness / 255) * 100)

    def set_brightness(self, value):
        """Update brightness, clamped to valid 0-255 range"""
        self.brightness = max(0, min(255, value))


class Sensor(Device):
    """A sensor entity that has a unit of measurement"""

    def __init__(self, entity_id, state, attributes=None):
        super().__init__(entity_id, state, attributes)
        self.unit = self.attributes.get("unit_of_measurement", "")

    def reading(self):
        """Return the sensor value with its unit"""
        return f"{self.state}{self.unit}"


class MediaPlayer(Device):
    """A media player entity"""

    def __init__(self, entity_id, state, attributes=None):
        super().__init__(entity_id, state, attributes)
        self.media_title = self.attributes.get("media_title")

    def now_playing(self):
        """Return what's currently playing, or a 'nothing playing' message"""
        if self.media_title:
            return f"Now playing: {self.media_title}"
        return "Nothing playing"


if __name__ == "__main__":
    bedroom_light = Light("light.bedroom", "on", {"brightness": 200, "friendly_name": "Bedroom Light"})
    temp_sensor = Sensor("sensor.temperature", "21.5", {"unit_of_measurement": "°C", "friendly_name": "Temperature"})
    speaker = MediaPlayer("media_player.living_room", "playing", {"media_title": "Dark Side of the Moon", "friendly_name": "Living Room Speaker"})

    print(bedroom_light)
    print(f"  Brightness: {bedroom_light.brightness_percent()}%")

    print(temp_sensor)
    print(f"  Reading: {temp_sensor.reading()}")

    print(speaker)
    print(f"  {speaker.now_playing()}")
