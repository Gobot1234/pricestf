import asyncio
from json import load
from enum import IntEnum
from typing import Optional

import aiohttp

session = aiohttp.ClientSession()

with open('defindex_mapping.json') as f:
    mapping = load(f)
    f.close()


class Quality(IntEnum):
    Normal = 0
    Genuine = 1
    Vintage = 3
    rarity3 = 4
    Unusual = 5
    Unique = 6
    Community = 7
    Valve = 8
    SelfMade = 9
    Customized = 10
    Strange = 11
    Completed = 12
    Haunted = 13
    Collectors = 14
    DecoratedWeapon = 15


async def request(defindex, *, quality: Quality = Quality.Unique,
                  australium: Optional[str] = None, killstreak: Optional[str] = None) -> aiohttp.ClientResponse:
    australium = australium if australium else ""
    killstreak = killstreak if killstreak else ""
    url = f"https://api.prices.tf/items/{defindex};{quality}{australium}{killstreak}?src=bptf"

    resp = await session.get(url)
    if resp.status == 200:
        return await resp.json()
    elif resp.status == 429:
        await asyncio.sleep(float(resp.headers['Retry-After']))


async def get_price(name, *, quality: Quality = Quality.Unique, australium: bool = False, killstreak: int = 0) -> dict:
    if australium:
        australium = ";australium"
    if 0 < killstreak <= 3:
        killstreak = f";kt-{killstreak}"

    try:
        defindex = mapping[name]
    except KeyError:
        raise

    content = await request(defindex, quality=quality, australium=australium, killstreak=killstreak)

    if not content['success']:
        raise aiohttp.ClientError(content['message'])
    data = {
        "name": content['name'],
        "buy_price": content['buy'],
        "sell_price": content['sell']
    }

    return data
