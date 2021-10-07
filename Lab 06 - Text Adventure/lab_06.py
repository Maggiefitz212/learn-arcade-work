class Room:
    """
    This is a class that represents the attributes of the room.
    """
    def __init__(self, description, north, east, south, west):
        """ This is a method that sets up the variables in the object. """
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    """This is my main program function"""
    room_list = []
    # Create an address
    room = Room("You are in the Kent Campus Center. You can head South.", None, None, 1, None)
    room_list.append(room)
    room = Room("You are in Kresge Residence Hall. You can head North or South.", 0, None, 2, None)
    room_list.append(room)
    room = Room("You are in Pfeifer, the dining hall with mediocre food. You can head any direction.", 1, 4, 6, 3)
    room_list.append(room)
    room = Room("You are at the firepit. Someone's making s'mores. You can only head East.", None, 2, None, None)
    room_list.append(room)
    room = Room("You are in McNeil, a building with classrooms. You can head South or West.", None, None, 5, 2)
    room_list.append(room)
    room = Room("You are in Carver Hall. There is a dinosaur skeleton. You can head North or West.", 4, None, None, 6)
    room_list.append(room)
    room = Room("You are in the chapel. It has stained glass windows. You can only head East.", None, 5, None, None)
    room_list.append(room)
    current_room = room_list[0]
    done = False
    while not done:
        print("")
        print(current_room.description)
        user_choice = input("What do you want to do?")
        print(user_choice)
        if user_choice.lower == "north" or user_choice.lower == "n" or user_choice.lower == "head north" or user_choice.lower == "go north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room
            print(next_room.description)
        elif user_choice.lower == "east" or user_choice.lower == "e" or user_choice.lower == "head east" or user_choice.lower == "go east":
            next_room = room_list[current_room].east
            print(next_room.description)
        elif user_choice.lower == "south" or user_choice.lower == "s" or user_choice.lower == "head south" or user_choice.lower == "go south":
            next_room = room_list[current_room].south
            print(next_room.description)
        elif user_choice.lower == "west" or user_choice.lower == "w" or user_choice.lower == "head south" or user_choice.lower == "go south":
            next_room = room_list[current_room].west
            print(next_room.description)
        else:
            next_room = None
            print("I don't understand that.")
            user_choice = input("Enter a different input.")
            print(user_choice)


main()
