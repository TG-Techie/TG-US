
###### a port of 2048 developed by D Raymon, adapted by TG-TEchie#####
#adaption date: 012619

from system.programs.__blank__app import init
from programs.stock import __tfte_2048 as tfte
exec(init)


page = container.add_panel()

board_height = cont_height - 20

num_to_color = {0:(204,191,180),2:(240,232,223),4:(240,228,209),8:(242,178,121),16:(250,152,102),32:(247,126,101),
                64:(250,97,62),128:(240,211,117),256:(242,205,104),512:(235,201,80),1024:(242,197,63),2048:(242,198,53),
                4096:(255,64,67),8192:(255,38,38)}

for i in num_to_color:
    num_to_color[i] = color.color(*num_to_color[i])

#print(num_to_color)

page.add(board = gui.nidos(cont_x, cont_y, board_height, board_height, 4,4))

def place_board():
    for i in range(4):
        print(tfte.Tile.array[i])

def new_game():
    tfte.Tile.new_game()
    place_board()







page.add(menu = gui.nidos(cont_x, cont_y + board_height, cont_width, cont_height - board_height, 5, 1))

page.menu.of(0,0).text == '<'
page.menu.of(0,0).set_purpose(tfte.Tile.move, 'a')

page.menu.of(0,0).text == '^'
page.menu.of(0,0).set_purpose(tfte.Tile.move, 'w')

page.menu.of(0,0).text == 'V'
page.menu.of(0,0).set_purpose(tfte.Tile.move, 's')

page.menu.of(0,0).text == '>'
page.menu.of(0,0).set_purpose(tfte.Tile.move, 'd')

page.menu.of(0,0).text == 'NuGM'
page.menu.of(0,0).set_purpose(new_game, ())

new_game()