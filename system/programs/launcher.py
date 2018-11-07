#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/26/18

#from system.programs.__blank__app import *
from system.programs.__blank__app import init
from gc import collect
exec(init)
#print(container._gui_id)
wants_refresh = 0

from os import listdir
import sys_gui_params as params
#from system import handler
from system import handler_uni as handler
import sys_config
from math import ceil
import time

#cusotmize move loop of launcher 
container.move_loop = params.launch_move_loop

#dimension math
#PAGE LABEL DEFS:
label_x  = cont_x + 3
label_y = cont_y + 1
label_width = int(cont_width ) - 6
label_border = 1
label_height = 10 + label_border*2
#menu defs:
menu_x = cont_x
menu_y = cont_y + 1 +label_height
menu_width = cont_width
menu_height = cont_height - 1 - label_height


#list of progs
prog_list = []

#add system stock programs 
for name in listdir('./programs/stock'):
    #print(name[0:2])
    if not (name[0:2] == ('._' or '__')):
        prog_list.append((name,'programs.stock'))
#print(prog_list)

#add user exposed programs
for name in listdir('./' + sys_config.prog_path.replace('.','/')):
    #print(name[0:2])
    if not (name[0:2] == ('._' or '__')):
        prog_list.append((name,sys_config.prog_path))
  
#print(prog_list)

for prog in prog_list.copy():
    #print(prog, prog[0:2])
    #boolean
    should_exclude = 0
    
    #check if is set aside for something else  or is hidden file (by os)
    should_exclude += prog[0][0:2] == ('__' or '._')
    
    if should_exclude:
        prog_list.pop(prog_list.index(prog))
collect()
#print(prog_list)


#find num pages always on the high side (meaning blank buttons)
num_pages = ceil(len(prog_list)/(params.launch_cols* params.launch_rows))

next_prog = 0
for page_num in range(num_pages):
    pan_pointer = container.add_panel('page' + str(page_num))
    
    pan_pointer.add( label = gui.text(label_x, label_y, label_width,
                    label_height, 'Applets:       Page:' + str(page_num + 1) + '/' + str(num_pages),
                    border = label_border))
    
    #print('the given object:')
    #print((container._gui_id))
    pan_pointer.add( menu = gui.nidos(menu_x, menu_y, menu_width, menu_height,
                                params.launch_cols, params.launch_rows, container, 0)) 
    #print(pan_pointer.menu.superior._gui_id)
    
    #time.sleep(3)
    #container.place()
    for but in pan_pointer.menu.contents:
        try:
            if (prog_list[next_prog][0] == '_SPCroot_SPC_ENTloader.py') and not (next_prog == len(prog_list)-1 ):
                prog_list.append(prog_list.pop(next_prog))
        except: pass
        try:
            prog_name = prog_list[next_prog][0].replace('.py','')
            prog_path = prog_list[next_prog][1]
            next_prog += 1
            #print(prog_name.replace('__', '\n'))
            #handler.load(prog_name)
            but.text = prog_name.replace('_ENT', '\n').replace("_SPC",' ')
            but.set_purpose(handler.load, (prog_name,prog_path))
        except:
            but.set_purpose(gui.button_error,(but,'No\nProg'))
            

    