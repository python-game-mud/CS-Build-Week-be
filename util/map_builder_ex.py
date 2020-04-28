import sys
from models import *

class Map:
    def __init__(self, height, width, player_x, player_y, paths):
        self.height = height
        self.width = width
        self.x = player_x
        self.y = player_y
        self.paths = paths

    def move(self, direction):
        if direction == "n":
            if ((self.x, self.y - 1), (self.x, self.y)) not in self.paths:
                print("Cannot go north")
            else:
                self.y -= 1
        if direction == "s":
            if ((self.x, self.y), (self.x, self.y + 1)) not in self.paths:
                print("Cannot go south")
            else:
                self.y += 1
        if direction == "e":
            if ((self.x, self.y), (self.x + 1, self.y)) not in self.paths:
                print("Cannot go east")
            else:
                self.x += 1
        if direction == "w":
            if ((self.x - 1, self.y), (self.x, self.y)) not in self.paths:
                print("Cannot go west")
            else:
                self.x -= 1

    def print_map(self):
        for y in range(0, self.height):
            # print the yth row of rooms
            for x in range(0, self.width):
                if self.x == x and self.y == y:
                    sys.stdout.write("[u]")  # this is the player's room
                else:
                    sys.stdout.write("[ ]")  # empty room
                # now see whether there's a path to the next room
                if ((x, y), (x + 1, y)) in self.paths:
                    sys.stdout.write("-")
                else:
                    sys.stdout.write(" ")
            # now that we've written the rooms, draw paths to next row
            print("")  # newline
            for x in range(0, self.width):
                sys.stdout.write(" ")  # spaces for above room
                if ((x, y), (x, y + 1)) in self.paths:
                    sys.stdout.write("|  ")
                else:
                    sys.stdout.write("   ")
            print("")


# position (x, y), connect to (x +/- 1, y) or (x, y +/- 1)
'''
room = (x, y)
room_connection = ((), ())
for each room where room = room_connection[0]
room_connection[1][0] = random number between x-- and x++ inclusive
room_connection[1][1] = random number between y-- and y++ inclusive

Option 2
for each room in rooms:
coords = ((roomA), (roomB))
roomA = current room
if currroom has n_to:
    roomB = room.n_to
if currroom has s_to:
    roomB = room.s_to
if currroom has e_to:
    roomB = room.e_to
if currroom has w_to:
    roomB = room.w_to
else 
# need a condition where the largest x coord is not larger than width
# need a condition where the largest y coord is not larger than height
return coords
'''

# paths = [((0, 0), (1, 0)),
#          ((0, 0), (0, 1)),
#          ((1, 3), (2, 3)),
#          ((2, 3), (3, 3)),]

m = Map(10, 10, 5, 5, paths)

while True:
    m.print_map()
    direction = input("What direction do you want to move? [n/e/s/w] ")
    m.move(direction)