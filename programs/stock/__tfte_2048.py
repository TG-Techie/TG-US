#import copy
import random


class Tile:
    array = []
    for i in range(4):
        array.append([])
        for j in range(4):
            array[i].append(0)
        #print(array[i])

    score = 0

    def __init__(self, value = 0):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return bool(self == other)

    def __add__(self, other):
        temp_self = int(self)
        temp_other = int(other)
        return temp_self + temp_other

    def __int__(self):
        return self.value

    #fill array with empty tiles
    def fill():
        for i in range(4):
            for j in range(4):
                Tile.array[i][j] = Tile()
        #print(Tile.array)

    #bring all tiles together in a direction
    def remove_spaces(direction):
        if direction == "w":
            for twice in range(2):
                for column in range(4):
                    for row in range(3):
                        if Tile.array[row][column] == 0:
                            row2 = 1
                            while row + row2 <= 3:
                                Tile.array[(row+row2)-1][column] = Tile.array[row+row2][column]
                                Tile.array[row+row2][column] = 0
                                row2 += 1
        elif direction == "s":
            for twice in range(2):
                for column in range(4):
                    for row in range(3,0,-1):
                        if Tile.array[row][column] == 0:
                            row2 = 1
                            while row - row2 >= 0:
                                Tile.array[(row-row2)+1][column] = Tile.array[row-row2][column]
                                Tile.array[row-row2][column] = 0
                                row2 += 1
        if direction == "a":
            for twice in range(2):
                for row in range(4):
                    for column in range(3):
                        if Tile.array[row][column] == 0:
                            column2 = 1
                            while column + column2 <= 3:
                                Tile.array[row][(column+column2)-1] = Tile.array[row][column+column2]
                                Tile.array[row][column+column2] = 0
                                column2 += 1
        elif direction == "d":
            for twice in range(2):
                for row in range(4):
                    for column in range(3,0,-1):
                        if Tile.array[row][column] == 0:
                            column2 = 1
                            while column - column2 >= 0:
                                Tile.array[row][(column-column2)+1] = Tile.array[row][column-column2]
                                Tile.array[row][column-column2] = 0
                                column2 += 1
    #add tiles together in a play's (or AI's) turn
    def move(direction):
        #temp_array = copy.deepcopy(Tile.array)
        temp_array = tuple(Tile.array)
        if direction == "w":
            Tile.remove_spaces("w")
            for column in range(4):
                for row in range(3):
                    if Tile.array[row][column] == Tile.array[row+1][column]:
                        Tile.score += int(Tile.array[row][column]) + int(Tile.array[row+1][column])
                        Tile.array[row][column] = int(Tile.array[row][column]) + int(Tile.array[row+1][column])
                        Tile.array[row+1][column] = 0
            Tile.remove_spaces("w")
        elif direction == "s":
            Tile.remove_spaces("s")
            for column in range(4):
                for row in range(3,0,-1):
                    if Tile.array[row][column] == Tile.array[row-1][column]:
                        Tile.score += int(Tile.array[row][column]) + int(Tile.array[row-1][column])
                        Tile.array[row][column] = int(Tile.array[row][column]) + int(Tile.array[row-1][column])
                        Tile.array[row-1][column] = 0
            Tile.remove_spaces("s")

        elif direction == "a":
            Tile.remove_spaces("a")
            for row in range(4):
                for column in range(3):
                    if Tile.array[row][column] == Tile.array[row][column+1]:
                        Tile.score += int(Tile.array[row][column]) + int(Tile.array[row][column+1])
                        Tile.array[row][column] = int(Tile.array[row][column]) + int(Tile.array[row][column+1])
                        Tile.array[row][column+1] = 0
            Tile.remove_spaces("a")
        else:
            Tile.remove_spaces("d")
            for row in range(4):
                for column in range(3,0,-1):
                    if Tile.array[row][column] == Tile.array[row][column-1]:
                        Tile.score += int(Tile.array[row][column]) + int(Tile.array[row][column-1])
                        Tile.array[row][column] = int(Tile.array[row][column]) + int(Tile.array[row][column-1])
                        Tile.array[row][column-1] = 0
            Tile.remove_spaces("d")

        if temp_array == Tile.array:
            return False
        else:
            #print("Safe move")
            return True
    #places new tiles randomly in array
    def new():
        #print("new called")
        x = random.randint(0,3)
        y = random.randint(0,3)
        #while not int(Tile.array[y][x]) == 0:
        while not (Tile.array[y][x]) == 0:
            x = random.randint(0,3)
            y = random.randint(0,3)
            #print(x, " ", y)
        value = random.randint(0,9)
        if value == 0:
            value = 4
        else:
            value = 2
        Tile.array[y][x] = Tile(value)

    #clears the board and starts a new game
    def new_game():
        Tile.fill()
        Tile.new()
        Tile.new()

    def is_valid(direction):
        #temp_array = copy.deepcopy(Tile.array)
        #temp_score = copy.copy(Tile.score)
        temp_array = tuple(Tile.array)
        temp_score = (Tile.score)
        if Tile.move(direction):
            Tile.score = temp_score
            Tile.array = temp_array
            return True
        else:
            Tile.score = temp_score
            Tile.array = temp_array
            return False

    #test to see if the game is over
    def game_over():
        #temp_array = copy.deepcopy(Tile.array)
        #temp_score = copy.copy(Tile.score)
        temp_array = tuple(Tile.array)
        temp_score = (Tile.score)
        if Tile.is_valid("w") == False and Tile.is_valid("a") == False and Tile.is_valid("s") == False and Tile.is_valid("d") == False:
            return True
        else:
            return False