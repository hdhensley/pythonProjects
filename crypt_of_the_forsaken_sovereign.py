"""
The Crypt of the Forsaken Sovereign
is a text-based adventure game.
it contains 8 rooms, 6 items
and 1 boss, the Lich King.
The entrance of the room is the Forsaken Gateway.
South of the Forsaken Gateway is the Decrepit Library, which contains the Ancient Scroll.
To the west of the Decrepit Library is the Cursed Mausoleum, which contains the Stone of the Grave Warden.
To the south of the Decrepit Library is teh Hall of Mirrors, which contains the Mirror of True Sight.
To the South of the Cursed Mausoleum is the Lich's Sanctum where the Lich King waits.
To the east of the Hall of Mirrors is the Shrine to Forgotten Deities, which contains the Amulet of the Dawn Bringer.
To the south of the Hall of Mirror is the Torture Chamber, which contains the Chains of Binding.
To the North of the Shrine to Forgotten Deities is the Vault of the Soulless,
which contains the Dagger of Eternity's End.
"""
dungeon = {
    'Forsaken Gateway': {'south': 'Decrepit Library'},
    'Decrepit Library': {'north': 'Forsaken Gateway', 'south': 'Hall of Mirrors', 'west': 'Cursed Mausoleum'},
    'Hall of Mirrors': {'north': 'Decrepit Library', 'south': 'Torture Chamber', 'east': 'Shrine to Forgotten Deities'},
    'Cursed Mausoleum': {'east': 'Decrepit Library', 'south': 'Lich\'s Sanctum'},
    'Shrine to Forgotten Deities': {'west': 'Hall of Mirrors', 'north': 'Vault of the Soulless'},
    'Torture Chamber': {'north': 'Hall of Mirrors'},
    'Lich\'s Sanctum': {'north': 'Cursed Mausoleum'},
    'Vault of the Soulless': {'south': 'Shrine to Forgotten Deities'}
}
items = {
    'Forsaken Gateway': '',
    'Decrepit Library': 'Ancient Scroll',
    'Hall of Mirrors': 'Mirror of True Sight',
    'Cursed Mausoleum': 'Stone of the Grave Warden',
    'Shrine to Forgotten Deities': 'Amulet of the Dawn Bringer',
    'Torture Chamber': 'Chains of Binding',
    'Vault of the Soulless': 'Dagger of Eternity\'s End',
    'Lich\'s Sanctum': 'Lich King',
}
commands = ['north', 'south', 'east', 'west', 'pickup', 'exit']

'''
The player starts in the Forsaken Gateway, with no items.
'''
current_room = 'Forsaken Gateway'
inventory = []

'''
now the player will be given directions on how to move around the dungeon, as well as how to pick up items.  
They can also exit the game.
To move from room to room the player will simply type the cardinal direction they wish to go.
to pick up an item the player will type 'pickup' and the item in the room will be added to their inventory.
to exit the game the player will type 'exit'.
'''
print('Welcome to the Crypt of the Forsaken Sovereign!')
print('To navigate the dungeon, simply type the direction you wish to go.')
print('Directions are: north, south, east, west.')
print('To pick up an item, type pickup and the item will be added to your inventory.')
print('To exit the game, type exit.')
print('to beat the game, you must find all the items before you encounter the Lich King.')
print('Good luck!')
