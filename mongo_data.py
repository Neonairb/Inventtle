import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://inventtle:1234@cluster0.xdubogw.mongodb.net/?retryWrites=true&w=majority")

def add_armor(section, name, atk, df, vel, mag, description, code):
    the_stat = {'atk': atk, 'def': df, 'vel': vel, 'mag': mag}

    armors = cluster['inventtle'][section]
    armors.insert_one({'name': name, 'stats': the_stat, 'description': description, 'code': code})

def add_weapon(name, atk, df, vel, mag, description, code):
    the_stat = {'atk': atk, 'def': df, 'vel': vel, 'mag': mag}

    weapons = cluster['inventtle']['weapons']
    weapons.insert_one({'name': name, 'stats': the_stat, 'description': description, 'code': code})

def add_artifact(name, atk, df, vel, mag, description, code):
    the_stat = {'atk': atk, 'def': df, 'vel': vel, 'mag': mag}

    artifacts = cluster['inventtle']['artifacts']
    artifacts.insert_one({'name': name, 'stats': the_stat, 'description': description, 'code': code})

# DELETE ALL
a = cluster['inventtle']
a = cluster['inventtle']['artifacts']
a.delete_many({})
a = cluster['inventtle']['weapons']
a.delete_many({})
a = cluster['inventtle']['helmets']
a.delete_many({})
a = cluster['inventtle']['chestplates']
a.delete_many({})
a = cluster['inventtle']['pants']
a.delete_many({})
a = cluster['inventtle']['boots']
a.delete_many({})
a = cluster['inventtle']['character']
a.delete_many({})

# ALL DATA
add_armor('helmets', 'Nada', 1, 1, 1, 1, 'No llevas nada...', 'h')
add_armor('pants', 'Nada', 1, 1, 1, 1, 'No llevas nada...', 'p')
add_armor('boots', 'Nada', 1, 1, 1, 1, 'No llevas nada...', 'b')
add_armor('chestplates', 'Nada', 1, 1, 1, 1, 'No llevas nada...', 'c')
add_weapon('Nada', 1, 1, 1, 1, 'No llevas nada...', 'w')
add_artifact('Nada', 1, 1, 1, 1, 'No llevas nada...', 'a')

#Minecraft
add_armor('helmets', 'Diamond Helmet', 0, 10, 0, 0, 'Recien crafteada bien maciza.', 'DHM')
add_armor('pants', 'Diamond Pants', 0, 10, 0, 0, 'Recien crafteada bien maciza.', 'DPM')
add_armor('boots', 'Diamond Boots', 0, 10, 0, 0, 'Recien crafteada bien maciza.', 'DBM')
add_armor('chestplates', 'Diamond Chestplate', 0, 10, 0, 0, 'Recien crafteada bien maciza.', 'DCM')
add_weapon('Diamond Sword', 10, 0, 5, 0, 'No esta encantada tristemente.', 'DSM')
add_artifact('Totem of Undying', 1, 1, 1, 5, 'Te regresara de entre los muertos... por desgracia no hay juego que jugar aqui.', 'TOUM')

#star wars
add_armor('helmets', 'Darth Vader\'s helmet', 0, 7, 0, 8, 'You can now feel the dark side', 'DBHS')
add_armor('pants', 'Darth Vader\'s pants', 0, 7, 0, 8, 'You can now feel the dark side', 'DBPS')
add_armor('boots', 'Darth Vader\'s boots', 0, 7, 0, 8, 'You can now feel the dark side', 'DBBS')
add_armor('chestplates', 'Darth Vader\'s chestplate', 0, 7, 0, 8, 'You can now feel the dark side', 'DBCS')
add_weapon('Light Saber', 6, 0, 5, 4, 'You cant be a Jedi without one', 'LSS')

#doom
add_armor('helmets', 'Doom Helmet', 6, 6, 0, 0, 'Wearing this will make you listen epic metal music in your mind', 'DHD')
add_armor('pants', 'Doom Pants', 6, 6, 0, 0, 'Wearing this will make you listen epic metal musice in your mind', 'DPD')
add_armor('boots', 'Doom Boots', 6, 6, 0, 0, 'Wearing this will make you listen epic metal music in your mind', 'DBD')
add_armor('chestplates', 'Doom Chestplate', 6, 6, 0, 0, 'Wearing this will make you listen epic metal music in your mind', 'DCD')
add_weapon('BFG 9000', 20, 0, -10, 0, 'Doesn\'t look like something practical to use, but looks epic', 'BFGD')

#halo
add_armor('helmets', 'Master Shief\'s Helmet', 5, 7, 7, 0, 'Youre now the legendary Spartan', 'HBH')
add_armor('pants', 'Master Shief\'s Pants', 5, 7, 7, 0, 'Youre now the legendary Spartan', 'HPH')
add_armor('boots', 'Master Shief\'s Boots', 5, 7, 7, 0, 'Youre now the legendary Spartan', 'HBH')
add_armor('chestplates', 'Master Shief\'s Chestplate', 5, 7, 7, 0, 'Youre now the legendary Spartan', 'HCH')
add_weapon('Energy Sword', 8, 0, 4, 0, 'Who doesnt know this weapon duh', 'ESH')

#Marvel
add_armor('helmets', 'Iron Man\'s Helmet', 2, 8, 3, 0, 'The latest in fashion and technology', 'IMHMa')
add_armor('pants', 'Iron Man\'s Pants', 2, 8, 3, 0, 'The latest in fashion and technology', 'IMPMa')
add_armor('boots', 'Iron Man\'s Boots', 2, 8, 3, 0, 'The latest in fashion and technology', 'IMBMa')
add_armor('chestplates', 'Iron Man\'s Chestplate', 2, 8, 3, 0, 'The latest in fashion and technology', 'IMCMa')
add_weapon('Mjolnir', 8, 0, -3, 5, 'Only someone worthy can use it', 'MTMa')

# Megaman
add_armor('helmets', 'Megaman\'s Helmet', 0, 4, 0, 5, 'Shooting lemons won\'t be that fun without wearing this', 'MHMe')
add_armor('pants', 'Megaman\'s Pants', 0, 4, 0, 5, 'Shooting lemons won\'t be that fun without wearing this', 'MPMe')
add_armor('boots', 'Megaman\'s Boots', 0, 4, 0, 5, 'Shooting lemons won\'t be that fun without wearing this', 'MBMe')
add_armor('chestplates', 'Megaman\'s Chestplate', 0, 4, 0, 5, 'Shooting lemons won\'t be that fun without wearing this', 'MCMe')

#FFVII
add_weapon('Buster Sword', 10, 0, -5, 3, 'FFVII is not that good...', 'BSF')

# Artefactos
add_artifact('Magna Soulprism', 4, 0.8, 1, 1, 'A dark and wild power flows in you', 'APMMu')
add_artifact('Foliacath bug', 2, 2, 2, 2, 'Faithful companion of hunters', 'FBMu')
add_artifact('Storm bead', 3, 1, 2, 2, 'Gods use this to get stronger', 'SBG')
add_artifact('Strange Coin', 1, 3, 1, 2, 'It\'s certainly weird ', 'SCD')

#personaje
character = cluster['inventtle']['character']
character.insert_one({
        "name": "Nahida",
        "gender": "Female",
        "race": "Archon",
        "age": 500,
        "stats": {'atk': 0, 'def': 0, 'vel': 0, 'mag': 0},
        "weapon": 'w',
        "armor": {'helmet': 'h', 'chestplate': 'c', 'pants': 'p', 'boots': 'b'},
        "artifact": "a",
        "description": "La pobrecita que encerraron"
})