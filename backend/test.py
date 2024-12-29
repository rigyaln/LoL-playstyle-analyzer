 
from apiMethods import *
from playstyleCalcMethods import *
from champData.champTagsDic import champ_to_playstyle
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
    for champion in masteries:
        print(f"Champion ID: {champion['championId']}, Mastery Points: {champion['championPoints']}")
        
    champIDs = []
    for champion in masteries:
         champIDs.append(champion['championId'])
    print(champIDs)

    arg = getListChampIDs(masteries)
    print(arg)

    arg2 = getListChampNames(arg)
    print(arg2)
    
     
    champs_and_masteries = getChampNames_AND_masteries(masteries)
    print(champs_and_masteries)

    arg3 = tally_tags(champs_and_masteries, champ_to_playstyle)
    print(arg3)

    arg4 = calculate_tag_percentages(arg3)
    print(arg4)

    arg5 = generate_playstyle_summary(arg4)
    print(arg5)


    

asyncio.run(main())