# Elliott Fawcett
def show_instructions():
    print('\nWelcome to Crimson Nightfall: Blood Legacy! A text-based game.')
    print("To win: "
          "Collect all 7 items throughout Enzo the Vampire's mansion, or he will turn you into a vampire spawn!")
    print('Move commands: go North, go East, go South, go West')
    print("To add item to inventory: grab 'item name'")


def player_status(current_room, inventory):
    print('\n=== Status ===')
    print('You are in the {}.'.format(current_room))
    print('Inventory:', inventory)


def main():
    rooms = {
        'Dungeon': {'North': 'Garage', 'South': 'Chapel', 'East': 'Bedroom', 'West': 'Armory'},
        'Chapel': {'North': 'Dungeon', 'West': 'Kitchen', 'item': 'Script'},
        'Kitchen': {'East': 'Chapel', 'item': 'Garlic Clove'},
        'Armory': {'North': 'Shed', 'East': 'Dungeon', 'item': 'Crossbow'},
        'Shed': {'South': 'Armory', 'East': 'Garage', 'item': 'Wood Arrows'},
        'Garage': {'West': 'Shed', 'South': 'Dungeon', 'East': 'Pool', 'item': 'Speed Potion'},
        'Pool': {'West': 'Garage', 'South': 'Bedroom', 'item': 'Enzo'},  # villain
        'Bedroom': {'North': 'Pool', 'West': 'Dungeon', 'South': 'Closet', 'item': 'Silver Arm Cuffs'},
        'Closet': {'North': 'Bedroom', 'item': 'Matches'},
    }

    show_instructions()
    current_room = 'Dungeon'
    inventory = []
    player_status(current_room, inventory)

    while True:

        command = input('Enter command:').split()
        action = command[0]

        if action == 'go':
            move = command[1]
            if move in rooms[current_room].keys():
                current_room = rooms[current_room][move]
                player_status(current_room, inventory)
                if current_room != 'Dungeon':
                    if 'item' in rooms[current_room]:
                        item = rooms[current_room]['item']
                        print('You see a(n)', item)
                    if current_room == 'Pool':
                        if len(inventory) == 7:
                            print('You have defeated Enzo and can now escape! Good job (: Thanks for playing.')
                            exit()
                        else:
                            print("**Ssh-tak! You are now a vampire spawn in Enzo's vampire army... GAME OVER!**")
                            exit()
            else:
                print("\nYou've run into a wall! Try a different direction.")
                player_status(current_room, inventory)

        elif action == 'grab':
            grab_item = ' '.join(command[1:])
            if 'item' in rooms[current_room]:
                item = rooms[current_room]['item']
                if grab_item == item:
                    inventory.append(grab_item)
                    rooms[current_room].pop('item')
                    player_status(current_room, inventory)
                else:
                    print("\nCan't grab that item!")
                    player_status(current_room, inventory)
                    print('You see a(n)', item)

        else:
            print('\nInvalid command!')
            player_status(current_room, inventory)


main()
