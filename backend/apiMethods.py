import aiohttp
import requests

async def get_puuid(ingameName=None, tagLine=None, api_key=None):
    link = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{ingameName}/{tagLine}?api_key={api_key}'
    response = requests.get(link)
    async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                return await response.json() 

async def get_masteries(puuid=None, api_key=None):
    link = f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}?api_key={api_key}'
    
    # Use aiohttp for asynchronous HTTP requests
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            return await response.json()

