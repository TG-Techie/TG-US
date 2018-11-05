#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/18/18

from tg_modules import tg_gui as gui
from system import gui_params as params
import random, time

x = params.sys_bar_pos[0]
y = params.sys_bar_pos[1]
width = params.sys_bar_dims[0]
height = params.sys_bar_dims[1]
line_height = params.sys_bar_line_thickness
line_color = params.sys_bar_line_color

# the window
container = gui.window(x,y,width,height + line_height)

panel = container.add_panel()

def change_bar_text(bar_obj):
    nextval = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for x in range(26))
    #print(nextval)
    bar_obj.value = nextval

#print(x,y,width,height)

#add the text (across whole top bar) and the line to sepreate it
panel.add(text = gui.text(x, y, width, height, '123 this is 26 long 123453',color = line_color))
#print(panel.text.char_width)
panel.add(line = gui.rect(x,height,width, line_height, line_color))

panel.add(refer = gui.operator(change_bar_text, (panel.text,)  ))

#panel.place()
#change_bar_text(panel.text)
#print(panel.contents)
#time.sleep(.5)
#panel.refer.refresh()
#panel.refresh()
#time.sleep(7)