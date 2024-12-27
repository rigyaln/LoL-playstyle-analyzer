# Your playstyle has best described you as a "____".
# "Burst Beserker" - High burst damage / hp champs
# "Glass Guillotine" - High burst damage / low hp champs
# "Mechanical Maniac" - High skill expression / combo champions
# "Roaming Ronin" - Roam champs / heavy map presence
# "Sidelane Specialist" - Split push / good tower siege champs
# "Staggering Sentinel" - High hp tankers
# "Team Fight Titan" - Team fight specialists
# "Dual-Form Demon" - Multiform champs
# "Unique Usurper" - Unique champs with unconventional playstyles
# "Elite Engager" - Engage champs
# "Final Boss" - Scaling champs
# "Steadfast Spellbinder" - Safe mid-late champs
# "Crowd Control Commando" - High cc champs
# "Reliable Reaper" - Consistent damage output, mediocre hp
# "Ethereal Enchanter" - Buff supporter champs
# "Primeval Peeler" - Peel supporter champs
# "Big Bully" - Lane bullies
# "Sharp Shooter" - Skillshot dependent champs

champ_to_playstyle = {
    "Aatrox": ["Mechanical Maniac", "Burst Bruiser"],
    "Ahri": ["Steadfast Spellbinder", "Roaming Ronin"],
    "Akali": ["Mechanical Maniac", "Glass Guillotine"],
    "Akshan": ["Roaming Ronin", "Reliable Reaper"],
    "Alistar": ["Staggering Sentinel", "Elite Engager", "Primeval Peeler"],
    "Ambessa": ["Mechanical Maniac", "Burst Beserker"],
    "Amumu": ["Team Fight Titan", "Staggering Sentinel", "Elite Engager", "Crowd Control Commando"],
    "Anivia": ["Steadfast Spellbinder", "Crowd Control Commando"],
    "Annie": ["Steadfast Spellbinder", "Crowd Control Commando"],
    "Aphelios": ["Unique Usurper", "Mechanical Maniac"],
    "Ashe": ["Crowd Control Commando", "Elite Engager"],
    "Aurelion Sol": ["Final Boss","Steadfast Spellbinder"],
    "Aurora": ["Glass Guillotine", "Mechanical Maniac"],
    "Azir": ["Mechanical Maniac", "Elite Engager", "Unique Usurper"],
    "Bard": ["Unique Usurper", "Elite Engager", "Roaming Ronin", "Crowd Control Commando"],
    "Bel'Veth": ["Final Boss", "Reliable Reaper"],
    "Blitzcrank": ["Crowd Control Commando", "Elite Engager"],  
    "Brand": ["Glass Guillotine", "Team Fight Titan"],
    "Braum": ["Crowd Control Maestro", "Primeval Peeler"],
    "Briar": ["Unique Usurper", "Glass Guillotine", "Roaming Ronin"],
    "Caitlyn": ["Reliable Reaper", "Final Boss"],
    "Camille": ["Sidelane Specialist", "Elite Engager", "Reliable Reaper"],
    "Cassiopeia": ["Steadfast Spellbinder", "Reliable Reaper"],
    "Cho'Gath": ["Final Boss", "Staggering Sentinel"],
    "Corki": ["Unique Usurper", "Roaming Ronin", "Reliable Reaper"],
    "Darius": ["Big Bully", "Sidelane Specialist"],
    "Diana": ["Team Fight Titan", "Elite Engager", "Glass Guillotine"],
    "Dr. Mundo": ["Staggering Sentinel", "Final Boss"],
    "Draven": ["Final Boss","Reliable Reaper", "Mechanical Maniac"],
    "Ekko": ["Glass Guillotine", "Steadfast Spellbinder"],
    "Elise": ["Dual-Form Demon", "Mechanical Maniac", "Elite Engager"],
    "Evelynn": ["Glass Guillotine", "Roaming Ronin"],
    "Ezreal": ["Mechanical Maniac", "Sharp Shooter"],
    "Fiddlesticks": ["Glass Guillotine", "Roaming Ronin", "Team Fight Titan"],
    "Fiora": ["Sidelane Specialist", "Mechanical Maniac"],
    "Fizz": ["Mechanical Maniac", "Roaming Ronin"],
    "Galio": ["Staggering Sentinel", "Team Fight Titan"],
    "Gangplank": ["Mechanical Maniac", "Sidelane Specialist"],
    "Garen": ["Big Bully", "Final Boss"],
    "Gnar": ["Dual-Form Demon", "Mechanical Maniac"],
    "Gragas": ["Staggering Sentinel", "Team Fight Titan"],
    "Graves": ["Sharp Shooter", "Reliable Reaper"],
    "Gwen": ["Mechanical Maniac", "Reliable Reaper"],
    "Hecarim": ["Roaming Ronin", "Elite Engager"],
    "Heimerdinger": ["Steadfast Spellbinder", "Sharp Shooter"],
    "Hwei": ["Sharp Shooter", "Final Boss"],
    "Illaoi": ["Big Bully", "Sidelane Specialist"],
    "Irelia": ["Mechanical Maniac", "Sidelane Specialist"],
    "Ivern": ["Unique Usurper", "Primeval Peeler", "Roaming Ronin"],
    "Janna": ["Ethereal Enchanter", "Primeval Peeler"],
    "Jarvan IV": ["Elite Engager", "Team Fight Titan"],
    "Jax": ["Final Boss", "Sidelane Specialist"],
    "Jayce": ["Dual-Form Demon", "Mechanical Maniac"],
    "Jhin": ["Sharp Shooter", "Final Boss"],
    "Jinx": ["Final Boss", "Sharp Shooter"],
    "K'Sante": ["Staggering Sentinel", "Elite Engager"],
    "Kai'Sa": ["Mechanical Maniac", "Final Boss"],
    "Kalista": ["Mechanical Maniac", "Sharp Shooter"],
    "Karma": ["Steadfast Spellbinder", "Ethereal Enchanter"],
    "Karthus": ["Reliable Reaper", "Steadfast Spellbinder"],
    "Kassadin": ["Final Boss", "Steadfast Spellbinder"],
    "Katarina": ["Mechanical Maniac", "Glass Guillotine"],
    "Kayle": ["Final Boss", "Sidelane Specialist"],
    "Kayn": ["Dual-Form Demon", "Mechanical Maniac"],
    "Kennen": ["Sharp Shooter", "Team Fight Titan"],
    "Kha'Zix": ["Mechanical Maniac", "Glass Guillotine"],
    "Kindred": ["Roaming Ronin", "Sharp Shooter"],
    "Kled": ["Big Bully", "Sidelane Specialist"],
    "Kog'Maw": ["Final Boss", "Sharp Shooter"],
    "Leblanc": ["Mechanical Maniac", "Glass Guillotine"],
    "Lee Sin": ["Mechanical Maniac", "Roaming Ronin"],
    "Leona": ["Elite Engager", "Crowd Control Commando"],
    "Lillia": ["Mechanical Maniac", "Roaming Ronin"],
    "Lissandra": ["Steadfast Spellbinder", "Crowd Control Commando"],
    "Lucian": ["Sharp Shooter", "Roaming Ronin"],
    "Lulu": ["Ethereal Enchanter", "Primeval Peeler"],
    "Lux": ["Sharp Shooter", "Steadfast Spellbinder"],
    "Malphite": ["Staggering Sentinel", "Team Fight Titan"],
    "Malzahar": ["Steadfast Spellbinder", "Final Boss"],
    "Maokai": ["Primeval Peeler", "Staggering Sentinel"],
    "Master Yi": ["Final Boss", "Reliable Reaper"],
    "Miss Fortune": ["Sharp Shooter", "Team Fight Titan"],
    "Mordekaiser": ["Final Boss", "Staggering Sentinel"],
    "Morgana": ["Crowd Control Commando", "Steadfast Spellbinder"],
    "Nami": ["Ethereal Enchanter", "Primeval Peeler"],
    "Naafiri": ["Roaming Ronin", "Glass Guillotine"],
    "Nautilus": ["Crowd Control Commando", "Elite Engager"],
    "Neeko": ["Steadfast Spellbinder", "Crowd Control Commando"],
    "Nidalee": ["Mechanical Maniac", "Dual-Form Demon"],
    "Nilah": ["Team Fight Titan", "Reliable Reaper"],
    "Nocturne": ["Roaming Ronin", "Glass Guillotine"],
    "Nunu & Willump": ["Unique Usurper", "Staggering Sentinel", "Roaming Ronin"],
    "Olaf": ["Big Bully", "Final Boss"],
    "Orianna": ["Steadfast Spellbinder", "Team Fight Titan"],
    "Ornn": ["Staggering Sentinel", "Final Boss"],
    "Pantheon": ["Big Bully", "Roaming Ronin"],
    "Poppy": ["Primeval Peeler", "Staggering Sentinel"],
    "Pyke": ["Glass Guillotine", "Roaming Ronin"],
    "Qiyana": ["Mechanical Maniac", "Roaming Ronin"],
    "Quinn": ["Roaming Ronin", "Sidelane Specialist"],
    "Rakan": ["Elite Engager", "Primeval Peeler"],
    "Rammus": ["Staggering Sentinel", "Elite Engager"],
    "Rek'Sai": ["Roaming Ronin", "Glass Guillotine"],
    "Rell": ["Staggering Sentinel", "Elite Engager"],
    "Renata Glasc": ["Primeval Peeler", "Crowd Control Commando"],
    "Renekton": ["Big Bully", "Sidelane Specialist"],
    "Rengar": ["Glass Guillotine", "Roaming Ronin"],
    "Riven": ["Mechanical Maniac", "Sidelane Specialist"],
    "Rumble": ["Team Fight Titan", "Mechanical Maniac"],
    "Ryze": ["Final Boss", "Steadfast Spellbinder"],
    "Samira": ["Mechanical Maniac", "Glass Guillotine"],
    "Sejuani": ["Staggering Sentinel", "Elite Engager"],
    "Senna": ["Sharp Shooter", "Primeval Peeler"],
    "Seraphine": ["Team Fight Titan", "Ethereal Enchanter"],
    "Sett": ["Big Bully", "Team Fight Titan"],
    "Shaco": ["Glass Guillotine", "Roaming Ronin"],
    "Shen": ["Primeval Peeler", "Roaming Ronin"],
    "Shyvana": ["Dual-Form Demon", "Final Boss"],
    "Singed": ["Unique Usurper", "Big Bully", "Sidelane Specialist"],
    "Sion": ["Staggering Sentinel", "Team Fight Titan"],
    "Sivir": ["Sharp Shooter", "Reliable Reaper"],
    "Skarner": ["Crowd Control Commando", "Staggering Sentinel"],
    "Sona": ["Ethereal Enchanter", "Primeval Peeler"],
    "Soraka": ["Ethereal Enchanter", "Primeval Peeler"],
    "Swain": ["Team Fight Titan", "Final Boss"],
    "Sylas": ["Steadfast Spellbinder", "Roaming Ronin"],
    "Syndra": ["Steadfast Spellbinder", "Mechanical Maniac"],
    "Tahm Kench": ["Primeval Peeler", "Final Boss"],
    "Taliyah": ["Roaming Ronin", "Steadfast Spellbinder"],
    "Talon": ["Roaming Ronin", "Glass Guillotine"],
    "Taric": ["Primeval Peeler", "Team Fight Titan"],
    "Teemo": ["Roaming Ronin", "Sharp Shooter"],
    "Thresh": ["Crowd Control Commando", "Primeval Peeler"],
    "Tristana": ["Sharp Shooter", "Roaming Ronin"],
    "Trundle": ["Big Bully", "Sidelane Specialist"],
    "Tryndamere": ["Final Boss", "Sidelane Specialist"],
    "Twisted Fate": ["Roaming Ronin", "Steadfast Spellbinder"],
    "Twitch": ["Roaming Ronin", "Sharp Shooter"],
    "Udyr": ["Final Boss", "Sidelane Specialist"],
    "Urgot": ["Big Bully", "Mechanical Maniac"],
    "Varus": ["Sharp Shooter", "Steadfast Spellbinder"],
    "Vayne": ["Mechanical Maniac", "Sharp Shooter"],
    "Veigar": ["Steadfast Spellbinder", "Final Boss"],
    "Vel'Koz": ["Steadfast Spellbinder", "Sharp Shooter"],
    "Vex": ["Steadfast Spellbinder", "Crowd Control Commando"],
    "Vi": ["Elite Engager", "Big Bully"],
    "Viego": ["Mechanical Maniac", "Glass Guillotine"],
    "Viktor": ["Steadfast Spellbinder", "Final Boss"],
    "Vladimir": ["Steadfast Spellbinder", "Final Boss"],
    "Volibear": ["Staggering Sentinel", "Team Fight Titan"],
    "Warwick": ["Final Boss", "Reliable Reaper"],
    "Wukong": ["Roaming Ronin", "Elite Engager"],
    "Xayah": ["Sharp Shooter", "Reliable Reaper"],
    "Xerath": ["Steadfast Spellbinder", "Sharp Shooter"],
    "Xin Zhao": ["Big Bully", "Reliable Reaper"],
    "Yasuo": ["Mechanical Maniac", "Final Boss"],
    "Yone": ["Mechanical Maniac", "Final Boss"],
    "Yorick": ["Big Bully", "Sidelane Specialist"],
    "Yuumi": ["Ethereal Enchanter", "Primeval Peeler"],
    "Zac": ["Elite Engager", "Staggering Sentinel"],
    "Zed": ["Glass Guillotine", "Roaming Ronin"],
    "Zeri": ["Sharp Shooter", "Roaming Ronin"],
    "Ziggs": ["Sharp Shooter", "Steadfast Spellbinder"],
    "Zilean": ["Steadfast Spellbinder", "Primeval Peeler"],
    "Zoe": ["Mechanical Maniac", "Steadfast Spellbinder"],
    "Zyra": ["Steadfast Spellbinder", "Crowd Control Commando"]
}
