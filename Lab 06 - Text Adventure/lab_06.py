class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
def main():
    room_list = []
    room = Room('entrance', 2, None, None, None)
    room_list.append(room)
    room1 = Room('Hall Room', 5, 3, 1, None)
    room_list.append(room1)
    room2 = Room('Dining Room', None, 4, None, 2)
    room_list.append(room2)
    room3 = Room('Kitchen', None, None, None, 3)
    room_list.append(room3)
    room4 = Room('Bed Room', None, None, 2, 6)
    room_list.append(room4)
    room5 = Room('Bath Room', None, 5, None, None)
    room_list.append(room5)
    current_room = 0
    print(room_list[current_room].description)

main()