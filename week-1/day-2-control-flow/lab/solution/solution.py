# ABOUTME: Day 2 lab solution — device filter using loops and conditionals
# ABOUTME: Demonstrates if/elif/else, for loops, and list filtering

devices = [
    {"name": "bedroom light", "state": "on", "type": "light"},
    {"name": "kitchen light", "state": "on", "type": "light"},
    {"name": "office fan", "state": "off", "type": "fan"},
    {"name": "bathroom sensor", "state": "unavailable", "type": "sensor"},
    {"name": "living room light", "state": "off", "type": "light"},
]

print("=== Device Filter ===")
filter_by = input("Filter by (state/type): ").strip()
filter_value = input(f"{filter_by.capitalize()} to show: ").strip()

matching = []
others = []

for device in devices:
    if device[filter_by] == filter_value:
        matching.append(device)
    else:
        others.append(device)

print(f"\nMatching ({filter_value}):")
for device in matching:
    print(f"  - {device['name']} ({device['state']})")

print(f"\nOthers:")
for device in others:
    print(f"  - {device['name']} ({device['state']})")
