from collections import Counter
from apiMethods import *

# Loading json file that contains all json info
with open('backend\champData\LoLchampions.json', 'r', encoding='utf-8') as f:
    champ_data = json.load(f)
id_to_name = {champ["key"]: champ["name"] for champ in champ_data["data"].values()}

def tally_tags(champ_mastery, champ_tags):
    tag_counter = Counter()
    
    # Sort champions by mastery points (highest first)
    sorted_champs = sorted(champ_mastery.items(), key=lambda x: x[1], reverse=True)
    
    # Iterate through the sorted champions and their mastery points
    for champ_name, mastery_points in sorted_champs:
        if champ_name in champ_tags:
            # Update the tag counter with the champion's tags, weighted by mastery points
            weight = mastery_points  # You could normalize this if needed
            tag_counter.update({tag: weight for tag in champ_tags[champ_name]})
    
    return tag_counter

def calculate_tag_percentages(tag_counter):
    total_points = sum(tag_counter.values())  # Total mastery points across all tags
    return {tag: round((count / total_points) * 100) for tag, count in tag_counter.items()}



def generate_playstyle_summary(tag_percentages):
    sorted_tags = sorted(tag_percentages.items(), key=lambda x: x[1], reverse=True)
    top_tag, top_percentage = sorted_tags[0]
    
    return f"Overall your playstyle has been best described as: {top_tag} - About ~{top_percentage}% of your top champ pool are contrived of {top_tag.lower()} champions."

def getListChampIDs(masteries=None):
    champIDs = []
    for champion in masteries:
        champIDs.append(champion['championId'])
    return champIDs

def getListChampNames(champIDs=None):
    champ_names = [id_to_name.get(str(champ_id), "Unknown Champ") for champ_id in champIDs]
    return champ_names  

def getChampNames_AND_masteries(masteries=None):
    # Create a dictionary of champion names and their mastery points
    champ_mastery = {champion['championId']: champion['championPoints'] for champion in masteries}
    
    # Get the champion names based on the IDs
    champ_names = getListChampNames(list(champ_mastery.keys()))
    
    # Combine the names and mastery points into a dictionary
    champs_and_masteries = {champ_name: champ_mastery[champ_id] for champ_name, champ_id in zip(champ_names, champ_mastery.keys())}
    
    return champs_and_masteries
    
     
