
#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/18/18
init = """
from tg_modules import tg_gui as gui
import sys_gui_params as params
from gc import collect

validation_ticket = 1

#make color referencing easier
color = gui.io

#define window size locally
#cont = container
cont_x = params.prog_pos[0]
cont_y = params.prog_pos[1]
cont_width = params.prog_dims[0]
cont_height = params.prog_dims[1]

wants_refresh = params.wants_refresh

container = gui.window(cont_x, cont_y, cont_width, cont_height, move_loop = params.move_loop,
                    color_clear = params.prog_color_clear, background = params.prog_background)
collect()

"""

exec(init)