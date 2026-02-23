# ABOUTME: Helper functions for parsing Home Assistant entity data
# ABOUTME: Used by report.py to demonstrate modules and function decomposition


def get_domain(entity_id):
    """Return the domain portion of an entity_id (e.g. 'light' from 'light.bedroom')"""
    return entity_id.split(".")[0]


def get_friendly_name(entity):
    """Return the friendly_name from an entity's attributes"""
    return entity["attributes"]["friendly_name"]


def is_active_light(entity):
    """Return True if the entity is a light that is currently on"""
    return get_domain(entity["entity_id"]) == "light" and entity["state"] == "on"


def brightness_percent(entity):
    """Return brightness as a 0-100 percentage, or None if brightness is not available"""
    brightness = entity["attributes"].get("brightness")
    if brightness is None:
        return None
    return round((brightness / 255) * 100)


def collect_unique_states(entities):
    """Return a set of all unique state values across all entities"""
    return {entity["state"] for entity in entities}
