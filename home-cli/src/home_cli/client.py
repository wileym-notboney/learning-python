# ABOUTME: Home Assistant API client — handles auth and HTTP requests
# ABOUTME: All commands use this module to talk to the HA REST API

import os
import sys

import httpx
from dotenv import load_dotenv

load_dotenv()


def get_client() -> httpx.Client:
    """Build an httpx client pre-configured with HA auth headers.

    Reads HA_URL and HA_TOKEN from environment variables.
    Exits with a clear error if either is missing.
    """
    url = os.environ.get("HA_URL")
    token = os.environ.get("HA_TOKEN")

    if not url:
        print("Error: HA_URL environment variable is not set.")
        print("  Set it to your Home Assistant address, e.g. http://homeassistant.local:8123")
        sys.exit(1)

    if not token:
        print("Error: HA_TOKEN environment variable is not set.")
        print("  Create a long-lived token in HA: Profile → Long-Lived Access Tokens")
        sys.exit(1)

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    return httpx.Client(base_url=url, headers=headers)
