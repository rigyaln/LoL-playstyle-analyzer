import aiohttp
 
# Returns the Player Universal Unique Identifier using ign, tagline and API key
# returns more player info but only PUUID is needed
async def get_puuid(ingameName=None, tagLine=None, api_key=None):
    link = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{ingameName}/{tagLine}?api_key={api_key}'
    
    async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                return await response.json() 

# Returns champion mastery info of inputted user in form of json file
async def get_masteries(puuid=None, api_key=None):
    count = 10

    link = f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count={count}&api_key={api_key}'
     
    # Use aiohttp for asynchronous HTTP requests
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            return await response.json()
        
    masteries = await get_masteries(puuid, api_key)


