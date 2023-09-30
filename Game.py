import random

# Define the rooms and their connections
rooms = {
    'Entrance': {'description': 'You are at the entrance of a mysterious castle.', 'north': 'Library'},
    'Library': {'description': 'You have entered the castle library. There are books everywhere.', 'south': 'Entrance',
                'east': 'Kitchen'},
    'Kitchen': {'description': 'You are in the kitchen. It smells delicious!', 'west': 'Library', 'north': 'Courtyard'},
    'Courtyard': {'description': 'You are in a courtyard surrounded by eerie statues.', 'south': 'Kitchen',
                  'west': 'Bedroom'},
    'Bedroom': {'description': 'You are in a dusty bedroom. A creepy painting hangs on the wall.', 'east': 'Courtyard',
                'north': 'Basement'},
    'Basement': {'description': 'You are in a dark and damp basement. It gives you the creeps.', 'south': 'Bedroom',
                 'east': 'Secret Chamber'},
    'Secret Chamber': {'description': 'You stumbled upon a secret chamber! Something valuable must be here...',
                       'west': 'Basement', 'north': 'Treasure Room'},
    'Treasure Room': {'description': 'You found the treasure room! But it\'s locked...', 'south': 'Secret Chamber'}
}

# Define the items
items = {
    'Key': 'A shiny key that might unlock something important.',
    'Book': 'An old, dusty book with strange symbols.',
    'Knife': 'A sharp knife that could be handy.',
    'Potion': 'A mysterious potion with a strange glow.',
    'Lantern': 'A lantern that can light your way in the dark.',
    'Map': 'A map that reveals hidden paths.',
    'Lich': 'An ancient and powerful Lich, guardian of the castle.'
}

# Initialize the player's inventory
inventory = []

# Initialize game state
defeated_lich = False


# Function to handle combat with the Lich
def combat_with_lich():
    print('You have encountered the Lich!')
    if all(item in inventory for item in ['Key', 'Book', 'Knife', 'Potion', 'Lantern', 'Map']):
        print('You have all the required items to defeat the Lich!')
        print('With your items in hand, you battle the Lich and emerge victorious!')
        return True
    else:
        print('You are not well-prepared to face the Lich. You have been defeated!')
        return False


# Function to display available commands
def display_commands():
    print('Available Commands:')
    print('north - Move to the north.')
    print('south - Move to the south.')
    print('east - Move to the east.')
    print('west - Move to the west.')
    print('quit - Quit the game.')


# Main game loop
player_location = 'Entrance'

# Display available commands at the beginning
print('Welcome to the Mysterious Castle Adventure!')
display_commands()

while True:
    # Display player's current location
    print(rooms[player_location]['description'])

    # Check for items in the room
    if player_location not in ['Entrance', 'Treasure Room', 'Secret Chamber']:
        item_found = random.choice(list(items.keys()))
        print(f'You found {item_found}: {items[item_found]}')
        inventory.append(item_found)
        del items[item_found]

    # Check if the player has defeated the lich
    if 'Lich' in inventory:
        defeated_lich = combat_with_lich()
        if defeated_lich:
            print('You have defeated the Lich! Congratulations, you win!')
        else:
            print('Your adventure ends here. Thanks for playing!')
        break

    # Check access to Treasure Room and Secret Chamber
    if player_location == 'Treasure Room' and 'Map' not in inventory:
        print('The Treasure Room is locked. You need a map to access it.')
        player_location = 'Secret Chamber'  # Move the player to the Secret Chamber instead
    elif player_location == 'Secret Chamber' and 'Key' not in inventory:
        print('The Secret Chamber is locked. You need a key to access it.')
        player_location = 'Basement'  # Move the player back to the Basement

    # Display player's inventory
    print('Inventory:', inventory)

    # Ask for player's action
    action = input('What do you want to do? ').lower()

    # Player navigation
    if action == 'quit':
        print('Thanks for playing!')
        break
    elif action in ['north', 'south', 'east', 'west']:
        if action in rooms[player_location]:
            player_location = rooms[player_location][action]
        else:
            print('You cannot move in that direction.')
    else:
        print('Invalid command. Try again.')

# End of the game
