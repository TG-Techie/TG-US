#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/26/18

#from system.programs.__blank__app import *
from system.programs.__blank__app import init
exec(init)

from os import listdir
from system import gui_params as params
from system import handler
from math import ceil
import time

#cusotmize move loop of launcher 
container.move_loop = params.launch_move_loop

#PAGE LABEL DEFS:
label_x  = cont_x
label_y = cont_y + 1
label_width = int(cont_width *3/7)
label_border = 1
label_height = 10 + label_border*2


#menu defs:
menu_x = cont_x
menu_y = cont_y + 1 +label_height
menu_width = cont_width
menu_height = cont_height - 1 - label_height


#list of progs
prog_list = listdir('./programs')

#find num pages
num_pages = ceil(len(prog_list)/(params.launch_cols* params.launch_rows))

next_prog = 0

for page_num in range(num_pages):
    pan_pointer = container.add_panel('page' + str(page_num))
    
    pan_pointer.add( label = gui.text(label_x, label_y, label_width,
                    label_height, 'Page:' + str(page_num + 1) + '/' + str(num_pages),
                    border = label_border))
    
    pan_pointer.add( menu = gui.nidos(menu_x, menu_y, menu_width, menu_height,
                                params.launch_cols, params.launch_rows)) 
    
    #time.sleep(3)
    #container.place()
    for but in pan_pointer.menu.contents:
        try:
            prog_name = prog_list[next_prog].replace('.py','')
            next_prog += 1
            #print(prog_name.replace('__', '\n'))
            #handler.load(prog_name)
            but.text = prog_name.replace('__', '\n')
            but.set_purpose(handler.load, (prog_name,))
        except:
            but.set_purpose(gui.button_error,(but,'No\nProg'))
            
            
        
        
    