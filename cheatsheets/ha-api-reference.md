# Home Assistant REST API — Quick Reference

Base URL: `http://homeassistant.local:8123` (or your HA IP)

All requests require:
```
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json
```

---

## Common Endpoints

### Check HA is running
```
GET /api/
```
Returns: `{"message": "API running."}`

### Get all entity states
```
GET /api/states
```
Returns: array of entity objects

### Get one entity state
```
GET /api/states/light.bedroom
```
Returns: single entity object

### Call a service
```
POST /api/services/{domain}/{service}
Body: {"entity_id": "light.bedroom"}
```

---

## Entity Object Structure

```json
{
  "entity_id": "light.bedroom",
  "state": "on",
  "attributes": {
    "brightness": 200,
    "color_temp": 4000,
    "friendly_name": "Bedroom Light",
    "supported_features": 44
  },
  "last_changed": "2026-02-23T10:00:00+00:00",
  "last_updated": "2026-02-23T10:00:00+00:00"
}
```

---

## Common Services

### Lights
| Service | Body | Effect |
|---------|------|--------|
| `light/turn_on` | `{"entity_id": "light.bedroom"}` | Turn light on |
| `light/turn_on` | `{"entity_id": "light.bedroom", "brightness": 200}` | Turn on at brightness |
| `light/turn_off` | `{"entity_id": "light.bedroom"}` | Turn light off |
| `light/toggle` | `{"entity_id": "light.bedroom"}` | Toggle on/off |

### Scenes
| Service | Body | Effect |
|---------|------|--------|
| `scene/turn_on` | `{"entity_id": "scene.evil_tv"}` | Activate a scene |

### Switches
| Service | Body | Effect |
|---------|------|--------|
| `switch/turn_on` | `{"entity_id": "switch.printer"}` | Turn switch on |
| `switch/turn_off` | `{"entity_id": "switch.printer"}` | Turn switch off |

### Climate
| Service | Body | Effect |
|---------|------|--------|
| `climate/set_temperature` | `{"entity_id": "climate.bedroom", "temperature": 22}` | Set temp |

---

## Entity ID Patterns

```
light.bedroom          → bedroom light
sensor.temperature     → temperature sensor
media_player.living_room → living room media player
switch.3d_printer      → 3D printer switch
scene.evil_tv          → "evil tv" scene
climate.office         → office climate entity
```

Rules:
- Lowercase only
- Spaces become underscores
- `domain.name` format

---

## Python Example

```python
import httpx
import os

url = os.environ["HA_URL"]
token = os.environ["HA_TOKEN"]
headers = {"Authorization": f"Bearer {token}"}

# Get all states
response = httpx.get(f"{url}/api/states", headers=headers)
entities = response.json()

# Turn on a light
httpx.post(
    f"{url}/api/services/light/turn_on",
    headers=headers,
    json={"entity_id": "light.bedroom"},
)
```

---

## Getting Your Token

1. Open Home Assistant in the browser
2. Click your username (bottom left)
3. Scroll to **Long-Lived Access Tokens**
4. Click **Create Token**, give it a name, copy it
5. Store it in your `.env` file — never commit it to git
