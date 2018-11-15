#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/18/18

from tg_modules import tg_gui as gui
import sys_gui_params as params
import random, time
from tg_io import io_battery as bat
from gc import collect 

wants_refresh = 1
validation_ticket = 42

x = params.sys_bar_pos[0]
y = params.sys_bar_pos[1]
width = params.sys_bar_dims[0]
height = params.sys_bar_dims[1]
line_height = params.sys_bar_line_thickness
line_color = params.sys_bar_line_color
text_width = width - 14

# the window
container = gui.window(x,y,width,height + line_height)

panel = container.add_panel()

'''def change_bar_text(bar_obj):
    nextval = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for x in range(26))
    #print(nextval)
    bar_obj.value = nextval'''

def num_2_time(val):
    if val < 10:
        return'0' + str(val)
    else:
        return str(val)

def place_bat(valin = None):
    if type(valin) == float:
        if bat.is_charging():
            gui.io.text(text_width , y + 1, '__batachrg__')
        else:
            gui.io.text(text_width , y + 1, '__bata'+str(round(valin*6))+'__')
    else:
        gui.io.text(text_width , y + 1, '  ')

def change_bar_text(target):
    global place_bat
    #time section
    current = time.localtime()
    #config hour
    hour = num_2_time(current[3])
    
    #config minute
    minu = num_2_time(current[4])

    #config seconds
    #sec = num_2_time(current[5])
    
    #battery section
    valin  = bat.get_percentage()
    per = str(round(valin*100))
    while len(per) < 3:
        per = ' '+per
    
    target.value = '['+ hour +':'+ minu +']'+ target.value[7:-4] + per + '%' 
    
    if target.active:
        place_bat(valin)
    
    collect()
    
'''
    valin  = bat.get_percentage()
    per = round(valin*100)
    if per < 10:
        txt = '  ' + str(per)
    elif per <100:
        txt = ' ' + str(per)
    else:
        txt = str(per)'''
    
#print(x,y,width,height)

#add the text (across whole top bar) and the line to sepreate it
panel.add(text = gui.text(x, y, text_width, height, ' '*int(text_width/6),color = line_color))

change_bar_text(panel.text)
panel.add(line = gui.rect(x,height,width, line_height, line_color))

panel.add(refer = gui.on_refresh(change_bar_text, (panel.text,)  ))
panel.add(bat = gui.on_place(place_bat, (bat.get_percentage(),), place_bat, (None,),))

#panel.place()
#change_bar_text(panel.text)
#print(panel.contents)
#time.sleep(.5)
#panel.refer.refresh()
#panel.refresh()
#time.sleep(7)