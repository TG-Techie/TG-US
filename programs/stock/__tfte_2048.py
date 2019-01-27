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
        Tile.move = Tile._move

    def _show():
        for i in Tile.array:
            print(i)

    def __repr__(self):
        return str(self.value)

    '''def __eq__(self, other):
        self = int(self)
        other = int(other)
        return self == other'''

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
                #print(i,j)
                Tile.array[i][j] = Tile()
        #print(Tile.array)

    #bring all tiles together in a direction
    '''def remove_spaces(direction):
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
                                column2 += 1'''


    def _null(*args, **kwargs):
        pass

    def move(*args, **kwargs):
        pass#only for init

    def _move(direction):
        def rotate_coord(x,y,direc, width):
            width -= 1
            return {'d':(x,y), 'w':(y,width-x), 'a':(width-x,width-y), 's':(width-y,x) }[direc]

        buffed_array = []
        for x in range(4):
            buffed_array.append([])
            for i in range(4):
                buffed_array[x].append(0)

        for x in range(4):
            for y in range(4):
                new_coord = rotate_coord(x, y, direction, 4)
                #print(x,y,new_coord)
                buffed_array[new_coord[0]][new_coord[1]] = (Tile.array[x][y].value)

        for row in buffed_array:
            out = []
            for i in row:
                if i:
                    out.append(i)
            while len(out) < 4:
                out = [0] + out
            buffed_array[buffed_array.index(row)] = out

        for row_num in range(4):
            row = buffed_array[row_num]
            for pos_num in reversed(range(1,4)):
                if row[pos_num] == row[pos_num-1]:
                    row[pos_num] *= 2
                    row[pos_num-1] = 0
                    Tile.score += row[pos_num]

        for row in buffed_array:
            out = []
            for i in row:
                if i:
                    out.append(i)
            while len(out) < 4:
                out = [0] + out
            buffed_array[buffed_array.index(row)] = out

        is_same = True
        for x in range(4):
            for y in range(4):
                buf_coords = rotate_coord(x,y,direction,4)
                if Tile.array[x][y].value == buffed_array[buf_coords[0]][buf_coords[1]]:
                    pass
                else:
                    is_same = False


        #push to Tile
        for x in range(4):
            for y in range(4):
                buf_coords = rotate_coord(x,y,direction,4)
                Tile.array[x][y].value = buffed_array[buf_coords[0]][buf_coords[1]]

        if not is_same:
            Tile.new()



    """def move(direction):
        print('move entered', direction)
        #temp_array = copy.deepcopy(Tile.array)

        '''
        temp_array = tuple(Tile.array)
        print(Tile.array)
        print(temp_array)'''
        #buffed_array = []
        for x in range(4):
            buffed_array.append([])
            for y in range(4):
                buffed_array[x].append(Tile.array[x][y])
            buffed_array[x] = tuple(buffed_array[x])
        buffed_array = tuple(buffed_array)

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
            Tile.remove_spaces("d")"""

    #places new tiles randomly in array
    def new():
        while 1:
            x = random.randint(0,3)
            y = random.randint(0,3)
            #print((Tile.array[y][x]))
            #print(type((Tile.array[y][x])))
            if not Tile.array[y][x].value:
                break
        value = random.randint(0,9)
        if value == 0:
            value = 4
        else:
            value = 2
        Tile.array[y][x] = Tile(value)

    #clears the board and starts a new game
    def new_game():
        Tile.score = 0
        Tile.move = Tile._move
        Tile.fill()
        Tile.new()
        Tile.new()

    '''def is_valid(direction):
        buffed_array = []
        for x in range(4):
            buffed_array.append([])
            for i in range(4):
                buffed_array[x].append(0)

        for x in range(4):
            for y in range(4):
                #new_coord = rotate_coord(x, y, direction, 4)
                #print(x,y,new_coord)
                buffed_array[x][y] = (Tile.array[x][y].value)

        #lock
        for row_num in range(4):
            buffed_array[row_num] = tuple(buffed_array[row_num])
        buffed_array = tuple(buffed_array)

        print(' tile ')
        Tile._show()

        print(' locked buffed ')
        for i in buffed_array:
            print(i)

        Tile.move(direction)
        print(' moved tile ')'''


    '''def is_valid(direction):
        def rotate_coord(x,y,direc, width):
            width -= 1
            #sawd
            return {'d':(x,y), 'w':(y,width-x), 'a':(width-x,width-y), 's':(width-y,x) }[direc]

        buffed_array = []
        for x in range(4):
            buffed_array.append([])
            for i in range(4):
                buffed_array[x].append(0)

        for x in range(4):
            for y in range(4):
                new_coord = rotate_coord(x, y, direction, 4)
                #print(x,y,new_coord)
                buffed_array[x][y] = (Tile.array[new_coord[0]][new_coord[1]].value)



        for row in buffed_array:
            out = []
            for i in row:
                if i:
                    out.append(i)
            while len(out) < 4:
                out = [0] + out
            buffed_array[buffed_array.index(row)] = out



        is_same = True
        for x in range(4):
            for y in range(4):
                if not buffed_array[x][y] == Tile.array[x][y].value:
                    is_same = False

        return not is_same'''



    #test to see if the game is over
    '''def game_over():
        #temp_array = copy.deepcopy(Tile.array)
        #temp_score = copy.copy(Tile.score)
        temp_array = tuple(Tile.array)
        temp_score = (Tile.score)
        if Tile.is_valid("w") == False and Tile.is_valid("a") == False and Tile.is_valid("s") == False and Tile.is_valid("d") == False:
            return True
        else:
            return False'''

    def game_over():

        can_move = False
        for x in range(1,4):
            for y in range(1,4):
                #print(x,y)
                try:
                    if Tile.array[x][y].value == Tile.array[x+1][y].value:
                        can_move = True
                    #print( x+1, y, Tile.array[x][y].value == Tile.array[x+1][y].value)
                except:
                    pass
                    #print('failed', x+1 , y)

                try:
                    if Tile.array[x][y].value == Tile.array[x-1][y].value:
                        can_move = True
                    #print( x-1, y, Tile.array[x][y].value == Tile.array[x-1][y].value)
                except:
                    pass
                    #print('failed', x-1 , y)

                try:
                    if Tile.array[x][y].value == Tile.array[x][y+1].value:
                        can_move = True
                    #print( x, y+1, Tile.array[x][y].value == Tile.array[x][y+1].value)
                except:
                    pass
                    #print('failed', x , y+1)

                try:
                    if Tile.array[x][y].value == Tile.array[x][y-1].value:
                        can_move = True
                    #print( x, y-1, Tile.array[x][y].value == Tile.array[x][y-1].value)
                except:
                    pass
                    #print('failed', x , y-1)
                #print('-----')
        if not can_move:
            Tile.move = Tile._null
        return not can_move