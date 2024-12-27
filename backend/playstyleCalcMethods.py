from collections import Counter
from apiMethods import *

# Loading json file that contains all json info
with open('backend\champData\LoLchampions.json', 'r', encoding='utf-8') as f:
    champ_data = json.load(f)
id_to_name = {champ["key"]: champ["name"] for champ in champ_data["data"].values()}



def tally_tags(top_champs, champ_tags):
    tag_counter = Counter()
    
    for champ in top_champs:
        if champ in champ_tags:
            tag_counter.update(champ_tags[champ])
    
    return tag_counter

def calculate_tag_percentages(tag_counter, total_champs):
    return {tag: (count / total_champs) * 100 for tag, count in tag_counter.items()}

def generate_playstyle_summary(tag_percentages):
    sorted_tags = sorted(tag_percentages.items(), key=lambda x: x[1], reverse=True)
    top_tag, top_percentage = sorted_tags[0]
    
    return f"Overall: {top_tag} - {top_percentage:.1f}% of your top champ pool are heavily {top_tag.lower()} champions."

def getListChampIDs(masteries=None):
    champIDs = []
    for champion in masteries:
        champIDs.append(champion['championId'])
    return champIDs

def getListChampNames(champIDs=None):
    champ_names = [id_to_name.get(str(champ_id), "Unknown Champ") for champ_id in champIDs]
    return champ_names  
     
