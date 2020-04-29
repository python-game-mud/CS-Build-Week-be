class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"

    def connect_rooms(self, connecting_room, direction):
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)

    def get_room_in_direction(self, direction):
        return getattr(self, f"{direction}_to")

    def get_coordinates(self):
        return [self.x, self.y]

# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.counter = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x
        # Start from lower-left corner (0,0)
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0
        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west
        # While there are rooms to be created...
        previous_room = None
        # room_direction = []
        # while room_count < num_rooms:
        #     # Calculate the direction of the room to be created
        #     if direction > 0 and x < size_x - 1:
        #         room_direction = "e"
        #         x += 1
        #         # print(x)
        #         # print("y values", y)
        #         # if x % 3 == 0:
        #         #     print(x)
        #         #     room_direction = "n"
        #             # room_direction = "e"
        #             # y += 1
        #             # direction *= -1
        #     elif direction < 0 and x > 0:
        #         room_direction = "w"
        #         x -= 1
        #         # if x % 3 == 0:
        #         #     room_direction = "s"
        #     else:
        #         # If we hit a wall, turn north and reverse direction
        #         room_direction = "n"
        #         y += 1
        #         direction *= -1
        while self.counter < self.width * self.height:

        while self.counter > self.width * self.height:
           
            # Create a room in the given direction
            room = Room(room_count, f"Room: {room_count}", f"This room has path: {room_direction}.", x, y)

            # Note that in Django, you'll need to save the room after you create it
            # Save the room in the World grid
            self.grid[y][x] = room
            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connect_rooms(room, room_direction)
            # if previous_room is not None:
            #     ne_room.connect_rooms(room, room_direction)
            # Update iteration variables
            previous_room = room
            self.counter += 1
            room_count += 1

            if room.id == 0:
                print("0 n", room.n_to)
                print("0 e", room.e_to)
                print("0 w", room.w_to)
                print("0 s", room.s_to)
                print("---------------")
            if room.id == 11:
                print("11 n", room.n_to)
                print("11 e", room.e_to)
                print("11 w", room.w_to)
                print("11 s", room.s_to)
                print("---------------")
            if room.id == 28:
                print("28 n", room.n_to)
                print("28 e", room.e_to)
                print("28 w", room.w_to)
                print("28 s", room.s_to)
                print("---------------")
            if room.id == 29:
                print("29 n", room.n_to)
                print("29 e", room.e_to)
                print("29 w", room.w_to)
                print("29 s", room.s_to)
                print("---------------")
            if room.id == 30:
                print('30 n', room.n_to)
                print("30 e", room.e_to)
                print("30 w", room.w_to)
                print("30 s", room.s_to)
                print("---------------")
            if room.id == 31:
                print("31 n",room.n_to)
                print("31 e",room.e_to)
                print("31 w",room.w_to)
                print("31 s",room.s_to)
                print("---------------")
            if room.id == 224:
                print("224 n",room.n_to)
                print("224 e",room.e_to)
                print("224 w",room.w_to)
                print("224 s",room.s_to) 
    def print_rooms(self):
        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"
        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"
        # Print string
        print(str)

w = World()
width = 10
height = 10
num_rooms = height * width
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
print(w.counter)