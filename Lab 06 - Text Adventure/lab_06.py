# created a room class and attributes
class Room:

    def __init__(self, description, north, east, south, west):
        # Attributes associated to the classroom
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

# main function the runs the program
def main():

    # Created a list to add the different rooms to.
    room_list = []

    # Create the rooms and how they are attached to the other rooms, directional wise.
    room = Room('You are at the entrance. \nThere is a passage to the north', 1, None, None, None)
    room_list.append(room)
    room1 = Room('You have entered the hall room. \nYou see doors to the north, east and south', 4, 2, 0, None)
    room_list.append(room1)
    room2 = Room('Welcome to the dining room. \nThere is an archway to the east and a door to the west', None, 3, None, 1)
    room_list.append(room2)
    room3 = Room('You have entered the kitchen. \nThere is an archway that leads west', None, None, None, 2)
    room_list.append(room3)
    room4 = Room('You are now in the bed room \nThere is a door to the west and another one to the south', None, None, 1, 5)
    room_list.append(room4)
    room5 = Room('Congrats you have found the bathroom! \nYou can exit to the east.', None, 4, None, None)
    room_list.append(room5)

    # Set the starting point at the first room created or in the case room 0
    current_room = 0
    done = False

    # Run the code over until the user wishes to quit
    while not done:
        print()
        # Print out the description of the current room
        print(room_list[current_room].description)

        # Get user input
        user_choice = input('What direction would you like to go?')

        # Based on what the user inputs direct the user to the new room
        if user_choice.upper() == 'N' or user_choice.upper() == 'NORTH':
            next_room = room_list[current_room].north
            # If the user directs to game a none existing directions tell them to try again,
            # else set the current room the one desired.
            if next_room is None:
                print('There is nothing in that direction.')
            else:
                current_room = next_room

        elif user_choice.upper() == 'E' or user_choice.upper() == 'EAST':
            next_room = room_list[current_room].east
            if next_room is None:
                print('There is nothing in that direction.')
            else:
                current_room = next_room

        elif user_choice.upper() == 'S' or user_choice.upper() == 'SOUTH':
            next_room = room_list[current_room].south
            if next_room is None:
                print('There is nothing in that direction.')
            else:
                current_room = next_room

        elif user_choice.upper() == 'W' or user_choice.upper() == 'WEST':
            next_room = room_list[current_room].west
            if next_room is None:
                print('There is nothing in that direction.')
            else:
                current_room = next_room

        # Allow the user to quit the game
        elif user_choice.upper() == 'QUIT' or user_choice.upper() == 'Q':
            print('Thanks for Playing!')
            done = True

        # If nothing the user types corresponds to game directions ask to try again
        else:
            print('Sorry input not recognized, please try again.')


main()
