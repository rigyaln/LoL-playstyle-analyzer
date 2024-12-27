 
from apiMethods import *
from playstyleCalcMethods import *
import os
import asyncio
 
async def main():
    api_key = os.environ.get('riot_api_key') 
    puuid_json = await get_puuid('fuwafuwa', '6969', api_key)
    puuid = puuid_json['puuid']
    print(f"API Key: {api_key}")
    print(puuid)

    masteries = await get_masteries(puuid, api_key)
    
    print(masteries)
    #   for champion in masteries:
    #       print(f"Champion ID: {champion['championId']}, Mastery Points: {champion['championPoints']}")
    
    

    

asyncio.run(main())