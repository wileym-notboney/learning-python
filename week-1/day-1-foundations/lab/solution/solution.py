# ABOUTME: Day 1 lab solution — device status reporter
# ABOUTME: Demonstrates variables, types, input/output, and f-strings

print("=== Home Assistant Status Reporter ===")

# Collect input — input() always returns a string
device_name = input("Device name: ")
state = input("Current state (on/off): ")
brightness = int(input("Brightness (0-255): "))
color_temp = int(input("Color temperature (K): "))

# Calculate brightness as a percentage
brightness_pct = round((brightness / 255) * 100)

# Print the formatted report
print()
print("--- Status Report ---")
print(f"Device:      {device_name}")
print(f"State:       {state.upper()}")
print(f"Brightness:  {brightness} / 255 ({brightness_pct}%)")
print(f"Color temp:  {color_temp}K")
