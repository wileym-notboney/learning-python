# ABOUTME: Fetches all entity states from Home Assistant REST API
# ABOUTME: Demonstrates httpx, environment variables, JSON file I/O

import json
import os
import sys

import httpx
from dotenv import load_dotenv

load_dotenv()

HA_URL = os.environ.get("HA_URL")
HA_TOKEN = os.environ.get("HA_TOKEN")

if not HA_URL:
    print("Error: HA_URL environment variable is not set")
    sys.exit(1)

if not HA_TOKEN:
    print("Error: HA_TOKEN environment variable is not set")
    sys.exit(1)

print(f"Connecting to Home Assistant at {HA_URL}...")

headers = {"Authorization": f"Bearer {HA_TOKEN}"}
response = httpx.get(f"{HA_URL}/api/states", headers=headers)
response.raise_for_status()

entities = response.json()
print(f"Fetched {len(entities)} entities")

with open("states.json", "w") as f:
    json.dump(entities, f, indent=2)
print("Saved to states.json")

print("\nTop 5 entities:")
for entity in entities[:5]:
    entity_id = entity["entity_id"]
    state = entity["state"]
    name = entity.get("attributes", {}).get("friendly_name", entity_id)
    print(f"  {entity_id:<26} | {state:<7} | {name}")

# Stretch: domain breakdown
domains: dict[str, int] = {}
for entity in entities:
    domain = entity["entity_id"].split(".")[0]
    domains[domain] = domains.get(domain, 0) + 1

print("\nDomains found:")
for domain, count in sorted(domains.items(), key=lambda x: -x[1]):
    print(f"  {domain}: {count} entities")
