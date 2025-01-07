import requests
import json
 

# Returns the Player Universal Unique Identifier using ign, tagline, and API key
# returns more player info but only PUUID is needed
 

def get_puuid(ingameName=None, tagLine=None, api_key=None):
    link = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{ingameName}/{tagLine}?api_key={api_key}'
    
    response = requests.get(link)

    if response.status_code == 404:
        raise ValueError("Username and tagline combination not found (404 error). Please check your input.")
    elif response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    
    return response.json()

# Returns champion mastery info of inputted user in form of JSON file
def get_masteries(puuid=None, api_key=None):
    count = 8
    link = f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count={count}&api_key={api_key}'
    
    response = requests.get(link)

    if response.status_code == 200:
        masteries = response.json()
        if isinstance(masteries, list) and len(masteries) > 0:
            return masteries
        else:
            raise ValueError("No mastery data available for the given PUUID.")
    else:
        raise Exception(f"API request failed with status code {response.status_code}")
