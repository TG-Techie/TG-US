
###### a port of 2048 developed by D Raymon, adapted by TG-TEchie#####
#adaption date: 012619

from system.programs.__blank__app import init
from tg_io.io_button import num2cmd_dict
from programs.stock.__tfte_2048 import Tile
import time
exec(init)

gui.io.rect(cont_x, cont_y, cont_width, cont_height, color.black)
gui.io.text(cont_x + 5, cont_y + 5, '''
Created by:
Daniel R.

Ported by:
Jonah Y-M''')
time.sleep(.5)


page = container.add_panel()

board_height = cont_height - 20

num_to_color = {0:(204,191,180),2:(240,232,223),4:(240,228,209),8:(242,178,121),16:(250,152,102),32:(247,126,101),
                64:(250,97,62),128:(240,211,117),256:(242,205,104),512:(235,201,80),1024:(242,197,63),2048:(242,198,53),
                4096:(255,64,67),8192:(255,38,38)}
for i in num_to_color:
    num_to_color[i] = color.color(*num_to_color[i])

#print(num_to_color)

page.add(board = gui.nidos(cont_x, cont_y, board_height, board_height, 4,4))
page.board.of(0,0).deselect()
page.add( score_label = gui.text(cont_x+board_height, cont_y + 5, cont_width - board_height, 15, 'Score:'))
page.add( score = gui.text(cont_x+board_height, cont_y + 20, cont_width - board_height, 20, '', border = 2))

def place_board(place = 1, force = False):
    for i in range(4):
        for j in range(4):
            pointer = page.board.of(i,j)
            number = Tile.array[j][i].value
            pointer.active = False
            pointer.text = str(number)
            pointer.color = num_to_color[number]
            #if place:
                #pointer.place()
    if place:
        for i in page.board.contents:
            i.place()
    page.score.value = str(Tile.score)

def new_game(place = 1, force = False):
    Tile.new_game()
    place_board(place,force)

def move(direction):
    if not Tile.game_over():
        Tile.move(direction)
        place_board()

    else:
        for i in range(8):
            page.board.contents[i].text = str('GameOver'[1])
    #print(Tile.score)

page.add(menu = gui.nidos(cont_x, cont_y + board_height, cont_width, cont_height - board_height, 5, 1))

#setup on screen buttons
page.menu.of(0,0).text = '<'
page.menu.of(0,0).set_purpose(move, 'a')

page.menu.of(1,0).text = '^'
page.menu.of(1,0).set_purpose(move, 'w')

page.menu.of(2,0).text = 'V'
page.menu.of(2,0).set_purpose(move, 's')

page.menu.of(3,0).text = '>'
page.menu.of(3,0).set_purpose(move, 'd')

page.menu.of(4,0).text = 'NuGM'
page.menu.of(4,0).set_purpose(new_game, ())

#set up hrdware buttons if possible
possib_Fs = []
for cmd in num2cmd_dict:
    if 'F' in num2cmd_dict[cmd]:
        possib_Fs.append(num2cmd_dict[cmd].replace('F',''))
possib_Fs.sort()
#print(possib_Fs)

Fkey_text = """"""
for i in range(4):
    try:
        num = possib_Fs.pop(0)
        page.cmd_dict['F'+num] = ((move, 'a'),(move, 'w'),(move, 's'),(move, 'd'))[i]
        Fkey_text += ('<','^','V','>')[i] + '=F'+num+'\n'
    except:
        pass

page.add(func_text = gui.text(cont_x+board_height, cont_y + 50, cont_width - board_height, 40, Fkey_text))


new_game(place = 0, force = True)