# ABOUTME: Main report script — imports helpers and prints HA entity summary
# ABOUTME: Demonstrates module imports and the if __name__ == "__main__" pattern

from ha_helpers import (
    get_friendly_name,
    is_active_light,
    brightness_percent,
    collect_unique_states,
)

entities = [
    {
        "entity_id": "light.bedroom",
        "state": "on",
        "attributes": {"brightness": 200, "color_temp": 4000, "friendly_name": "Bedroom Light"}
    },
    {
        "entity_id": "light.kitchen",
        "state": "off",
        "attributes": {"brightness": 0, "friendly_name": "Kitchen Light"}
    },
    {
        "entity_id": "sensor.temperature",
        "state": "21.5",
        "attributes": {"unit_of_measurement": "°C", "friendly_name": "Temperature"}
    },
    {
        "entity_id": "media_player.living_room",
        "state": "playing",
        "attributes": {"media_title": "Dark Side of the Moon", "friendly_name": "Living Room Speaker"}
    },
    {
        "entity_id": "light.office",
        "state": "on",
        "attributes": {"brightness": 150, "friendly_name": "Office Light"}
    },
]


def print_all_entities(entities):
    """Print a table of all entities"""
    print(f"All entities ({len(entities)} total):")
    for entity in entities:
        entity_id = entity["entity_id"]
        state = entity["state"]
        name = get_friendly_name(entity)
        print(f"  {entity_id:<22} | {state:<7} | {name}")


def print_active_lights(entities):
    """Print lights that are currently on"""
    active = [e for e in entities if is_active_light(e)]
    print(f"\nLights that are ON ({len(active)}):")
    for light in active:
        name = get_friendly_name(light)
        pct = brightness_percent(light)
        print(f"  - {name} (brightness: {pct}%)")


def main():
    print("=== HA Entity Report ===\n")
    print_all_entities(entities)
    print_active_lights(entities)
    unique_states = collect_unique_states(entities)
    print(f"\nUnique states found: {unique_states}")


if __name__ == "__main__":
    main()
