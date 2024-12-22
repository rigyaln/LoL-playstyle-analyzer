from apiMethods import *

import os
import asyncio

async def main():
    api_key = os.environ.get('riot_api_key') 
    puuid_json = await get_puuid('fuwafuwa', '6969', api_key)
    print(puuid_json['puuid'])
    

asyncio.run(main())