import json
import os
import requests
import secrets
from pathlib import Path
import asyncio
import httpx
from settings.settings import DISCORD_API_KEY

async def send_discord_message(text: str):
    if DISCORD_API_KEY is None:
        return "No API found. Please check your statuts with GLA-DOS discord bot"
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://gla-dos-prod.up.railway.app/discord/say",
            json={"text": text},
            headers={"X-Glados-Key": DISCORD_API_KEY},
        )
        r.raise_for_status()
        return r.json()
