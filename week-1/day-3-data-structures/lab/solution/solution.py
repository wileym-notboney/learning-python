# ABOUTME: Day 3 lab solution — parsing a list of dicts representing HA entities
# ABOUTME: Demonstrates lists, dicts, nested access, filtering, and sets

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

print("=== HA Entity Report ===\n")

# All entities
print(f"All entities ({len(entities)} total):")
for entity in entities:
    entity_id = entity["entity_id"]
    state = entity["state"]
    name = entity["attributes"]["friendly_name"]
    print(f"  {entity_id:<22} | {state:<7} | {name}")

# Lights that are on — filter by domain prefix and state
active_lights = [
    e for e in entities
    if e["entity_id"].split(".")[0] == "light" and e["state"] == "on"
]

print(f"\nLights that are ON ({len(active_lights)}):")
for light in active_lights:
    name = light["attributes"]["friendly_name"]
    brightness = light["attributes"].get("brightness", "N/A")
    print(f"  - {name} (brightness: {brightness})")

# Collect unique states using a set
unique_states = {e["state"] for e in entities}
print(f"\nUnique states found: {unique_states}")
