from collections import Counter

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
