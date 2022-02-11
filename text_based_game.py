"""Space Adventure Text Based Game"""
from enum import Enum
import time


# todo: replace all strings with enums and parse them
class Command(Enum):
    """Define values for the Command type."""
    EXIT = 'exit'
    GET = 'get'
    GO = 'go'
    HELP = 'help'


class Direction(Enum):
    """Define values for the Direction type."""
    EAST = 'East'
    NORTH = 'North'
    SOUTH = 'South'
    WEST = 'West'


class Item(Enum):
    """Define values for the Item type."""
    ACCESS_CARD = 'Access Card'
    FIRST_AID_KIT = 'First Aid Kit'
    FLUX_CAPACITOR = 'Flux Capacitor'
    POWERED_ARMOR = 'Powered Armor'
    SOCKS = 'Socks'
    SONIC_SCREWDRIVER = 'Sonic Screwdriver'
    SPACE_GLUE = 'Space Glue'
    SPACE_SNACKS = 'Space Snacks'
    SPARE_PARTS = 'Spare Parts'
    VILLAIN = 'Space Monster'


class Room(Enum):
    """Define values for the Room type."""
    AIRLOCK = 'Airlock'
    ARMORY = 'Armory'
    BRIDGE = 'Bridge'
    CARGO_BAY = 'Cargo Bay'
    COMMON_AREA = 'Common Area'
    CREW_QUARTERS = 'Crew Quarters'
    ENGINEERING = 'Engineering'
    GALLEY = 'Galley'
    MEDICAL_BAY = 'Medical Bay'
    REACTOR = 'Reactor'
    SCIENCE_LAB = 'Science Lab'


# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    Room.AIRLOCK: {
        Direction.SOUTH: Room.CARGO_BAY,
        'item': Item.VILLAIN
    },
    Room.ARMORY: {
        Direction.SOUTH: Room.BRIDGE,
        Direction.EAST: Room.SCIENCE_LAB,
        'item': Item.POWERED_ARMOR
    },
    Room.BRIDGE: {
        Direction.NORTH: Room.ARMORY,
        Direction.SOUTH: Room.MEDICAL_BAY,
        Direction.EAST: Room.COMMON_AREA,
        'item': Item.ACCESS_CARD
    },
    Room.CARGO_BAY: {
        Direction.NORTH: Room.AIRLOCK,
        Direction.SOUTH: Room.ENGINEERING,
        Direction.WEST: Room.SCIENCE_LAB,
        'item': Item.SPARE_PARTS
    },
    Room.COMMON_AREA: {
        Direction.NORTH: Room.SCIENCE_LAB,
        Direction.SOUTH: Room.GALLEY,
        Direction.EAST: Room.BRIDGE,
        Direction.WEST: Room.ENGINEERING
    },
    Room.CREW_QUARTERS: {
        Direction.WEST: Room.GALLEY,
        'item': Item.SPACE_SNACKS
    },
    Room.ENGINEERING: {
        Direction.NORTH: Room.CARGO_BAY,
        Direction.EAST: Room.REACTOR,
        Direction.WEST: Room.COMMON_AREA,
        'item': Item.SONIC_SCREWDRIVER
    },
    Room.GALLEY: {
        Direction.NORTH: Room.COMMON_AREA,
        Direction.EAST: Room.CREW_QUARTERS,
        Direction.WEST: Room.MEDICAL_BAY,
        'item': Item.SPACE_SNACKS
    },
    Room.MEDICAL_BAY: {
        Direction.NORTH: Room.BRIDGE,
        Direction.EAST: Room.GALLEY,
        'item': Item.FIRST_AID_KIT
    },
    Room.REACTOR: {
        Direction.EAST: Room.ENGINEERING,
        'item': Item.FLUX_CAPACITOR
    },
    Room.SCIENCE_LAB: {
        Direction.SOUTH: Room.COMMON_AREA,
        Direction.EAST: Room.CARGO_BAY,
        Direction.WEST: Room.ARMORY,
        'item': Item.SPACE_GLUE
    }
}

# A dictionary for storing the players current location and inventory list.
player = {
    'location': Room.COMMON_AREA,
    'inventory': []
}


def instruction_help():
    """Displays instructions on how to play the game"""
    # Prints a line of dashes before the instructions.
    print('-' * 68)
    # Displays instructions on how to play the game.
    print("Explore the game by using move commands to navigate around the map.")
    print("Move Commands: 'go North', 'go South', 'go East', 'go West'")
    print("Use the command 'exit' to quit the game.")
    # Prints a line of dashes after the instructions.
    print('-' * 68)


def slow_print(line_to_print):
    """Function for the fun of printing slowly like a message."""
    # Takes input parameter and loops through each line in the array.
    for line in line_to_print:
        # Then loops through each character in the line.
        # Puts a small delay between each print to create the effect.
        for char in line:
            print(char, end='')
            # todo: uncomment time.sleep delay
            # time.sleep(.02)
        # Prints two lines between each section
        print('\n')


def display_intro():
    """Displays game intro and instructions."""
    # Displays game title.
    print('Space Text Adventure Game')
    # Prints a line of dashes after the title.
    print('-' * 68)
    # Separated game introduction in separate sections.
    game_intro_line_one = "Your ship is under attack and you're adrift in space. Someone,\n" \
                          "or something, is running amuck causing systems to malfunction."
    game_intro_line_two = "You need to gather parts to get the ship up and running again as\n" \
                          "well as find supplies to deal with the uninvited guest. You will\n" \
                          "need to gather an access card from the bridge to get access to any\n" \
                          "locked areas, space glue from the science lab, a sonic screwdriver\n" \
                          "from engineering, and spare parts from the cargo bay to repair the\n" \
                          "ship, and snacks from the galley to keep you going."
    game_intro_line_three = "Lastly, you will need to get your suit of powered armor from the\n" \
                            "armory to escort the intruder from the ship how you see fit."
    # Puts each section of text into an array
    lines_to_print = [game_intro_line_one, game_intro_line_two, game_intro_line_three]
    # Passes the array to slow_print to display.
    slow_print(lines_to_print)
    # Calls instruction_help() to initially display the instructions to the user.
    instruction_help()


def display_status():
    """Displays the current location of the player."""
    # Prints a line of dashes before displaying the current status of the player.
    print('\n' + '-' * 36)
    # Prints the players current location by accessing the player dictionary using the location key.
    print(f"You are in the {player['location'].value}")
    # Prints a line of dashes before the move prompt.
    print('-' * 36)


def parse_enum(command, direction):
    """Matches parameters to enums, else returns empty strings"""
    # Loops through each member of the Command enum class.
    for command_member in Command:
        # Compares the entered string to the value of the current enum member.
        if command in command_member.value:
            # If it matches, assigns that member to command and breaks out of the loop.
            command = command_member
            break
    # If there is no match, assign an empty string to command.
    else:
        command = ''
    # Loops through each member of the Direction enum class.
    for direction_member in Direction:
        # Compares the entered string to the value of the current enum member.
        if direction in direction_member.value:
            # If it matches, assigns that member to direction and breaks out of the loop.
            direction = direction_member
            break
            # If there is no match, assign an empty string to command.
    else:
        direction = ''
    # Returns either the matching enum or an empty string.
    return command, direction


def player_input():
    """Takes the players input and splits it, and returns the command and direction."""
    # Gets the players input, strips leading & trailing whitespace.
    # Then splits it into two parts (command, direction).
    player_move = input('Enter your move => ').strip().split(' ', 1)
    # Assigns the player command and converts it all to lower case for future comparison.
    command = player_move[0].lower()
    # Checks that there is a second value in player_move to assign to direction.
    # If there isn't, then assign an empty string.
    # Otherwise, assign the direction and strip extra whitespace from between command and direction.
    # Then converts it to title case for future comparison.
    direction = player_move[1].strip().title() if len(player_move) > 1 else ''
    # Return the command and direction values.
    return command, direction


def get_player_action():
    """Gets the players input, validates it, and returns the command and direction."""
    # Calls player_input function and assigns the return values to command and direction.
    command, direction = player_input()
    # Passes command and direction to parse_enum to convert string to matching enum.
    command, direction = parse_enum(command, direction)
    # Checks for a valid command or a valid direction.
    # If either is not valid, then it enters the loop.
    while not command or direction not in rooms[player['location']].keys():
        # Checks if a valid command of exit was given, but an invalid direction was entered.
        if command == Command.EXIT:
            # Breaks out of the loop if the player wants to quit.
            break
        # If we get here, then we know the command isn't exit.
        # Checks if the command is for go.
        if not command:
            # At this point the command is neither exit nor go.
            # Inform the player that the command they entered is not valid.
            print('That is not a valid command!')
        # If we get here, then the command is valid which means the direction is not.
        else:
            # Inform the player that the direction they entered is not valid.
            print("You can't go that way")
        # Display the players current status and then get their input again.
        display_status()
        # If the player enters a valid move at this point it will break out of the loop.
        # Otherwise, the loop will continue.
        command, direction = player_input()
        command, direction = parse_enum(command, direction)
    # Return the validated command and direction.
    return command, direction


def move_player(move_direction):
    """Takes the players go direction and updates player to that location."""
    # The validated direction is passed into the function and used to update the player's location.
    # Use value of the players current location (player['location']) as key for the room dictionary.
    # Use the direction that was passed in as the key for the nested dictionary to get the new room.
    player['location'] = rooms[player['location']][move_direction]


def exit_game():
    """Gets and validates players input and returns True to quit or False to continue."""
    # Gets the players input, strips leading & trailing whitespace, and converts it to lower case.
    quit_game_input = input('Are you sure you want to quit? (yes/no) => ').strip().lower()
    # Checks for a valid input of yes, no, y, or n.
    # If the input is not valid, then it enters the loop.
    while quit_game_input not in ('yes', 'y', 'no', 'n'):
        # Informs the user of their invalid input and prompts them to try again.
        # Strips input of trailing or leading whitespace and converses it to lower for comparison.
        quit_game_input = input('Invalid input! Enter yes or no => ').strip().lower()
    # At this point, input is valid as either yes or no.
    # Assigns True to quit_game if input is yes.
    # Assigns False to quit_game if input is no.
    quit_game = quit_game_input in ('yes', 'y')
    # Return quit_game.
    return quit_game


def main():
    """Main function with the loop, function calls and game flow logic."""
    # Calls display_into to show the introduction and how to play the game.
    display_intro()
    # Variable used to store current play start of the game.
    # False: keep playing True: exit game.
    quit_game = False
    while not quit_game:
        # Calls display_status() to show the players current location.
        display_status()
        # Calls get_player_action() to get the players validated command and move.
        # Assigns the return values to player_command and player_direction.
        player_command, player_direction = get_player_action()
        # Checks if the players command is to exit the game.
        if player_command == Command.EXIT:
            # At this point, the player wants to quit.
            # Call exit_game() and set its return value to quit_game.
            # If exit_game() returns true, loop will end.
            # If exit_game() returns false, loop will continue.
            quit_game = exit_game()
        # At this point it means the player command is go.
        elif player_command == Command.GO:
            # Pass player_direction to move_player to update the player's location to a new room.
            move_player(player_direction)
    # After exiting the loop, display a line of dashes.
    # The display a goodbye message to the player.
    print('\n' + '-' * 46)
    print('Thanks for playing Space Text Adventure Game.')
    print('I hope you enjoyed it!!!')


# Calling the main function to start the program.
if __name__ == "__main__":
    main()
