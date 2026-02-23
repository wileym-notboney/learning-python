# ABOUTME: Tests for the Device, Light, and Sensor model classes
# ABOUTME: These run with 'uv run pytest' — no HA connection needed

import pytest

from home_cli.models import Device, Light, Sensor, device_from_dict


LIGHT_DATA = {
    "entity_id": "light.bedroom",
    "state": "on",
    "attributes": {
        "brightness": 200,
        "color_temp": 4000,
        "friendly_name": "Bedroom Light",
    },
}

SENSOR_DATA = {
    "entity_id": "sensor.temperature",
    "state": "21.5",
    "attributes": {
        "unit_of_measurement": "°C",
        "friendly_name": "Temperature",
    },
}

SWITCH_DATA = {
    "entity_id": "switch.printer",
    "state": "off",
    "attributes": {"friendly_name": "3D Printer"},
}


class TestDevice:
    def test_domain(self):
        device = Device.from_dict(LIGHT_DATA)
        assert device.domain() == "light"

    def test_name_from_attributes(self):
        device = Device.from_dict(LIGHT_DATA)
        assert device.name() == "Bedroom Light"

    def test_name_falls_back_to_entity_id(self):
        device = Device("light.bedroom", "on", {})
        assert device.name() == "light.bedroom"

    def test_is_on_true(self):
        device = Device.from_dict(LIGHT_DATA)
        assert device.is_on() is True

    def test_is_on_false(self):
        device = Device.from_dict(SWITCH_DATA)
        assert device.is_on() is False

    def test_str_on(self):
        device = Device.from_dict(LIGHT_DATA)
        assert str(device) == "Bedroom Light [ON]"

    def test_str_off(self):
        device = Device.from_dict(SWITCH_DATA)
        assert str(device) == "3D Printer [OFF]"


class TestLight:
    def test_brightness(self):
        light = Light.from_dict(LIGHT_DATA)
        assert light.brightness == 200

    def test_brightness_percent(self):
        light = Light.from_dict(LIGHT_DATA)
        assert light.brightness_percent() == 78

    def test_brightness_percent_zero(self):
        data = {**LIGHT_DATA, "attributes": {**LIGHT_DATA["attributes"], "brightness": 0}}
        light = Light.from_dict(data)
        assert light.brightness_percent() == 0


class TestSensor:
    def test_unit(self):
        sensor = Sensor.from_dict(SENSOR_DATA)
        assert sensor.unit == "°C"

    def test_reading(self):
        sensor = Sensor.from_dict(SENSOR_DATA)
        assert sensor.reading() == "21.5°C"


class TestDeviceFromDict:
    def test_light_returns_light(self):
        device = device_from_dict(LIGHT_DATA)
        assert isinstance(device, Light)

    def test_sensor_returns_sensor(self):
        device = device_from_dict(SENSOR_DATA)
        assert isinstance(device, Sensor)

    def test_unknown_returns_device(self):
        device = device_from_dict(SWITCH_DATA)
        assert type(device) is Device
