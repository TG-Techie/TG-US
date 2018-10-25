#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/18/18

from tg_modules import tg_gui as gui
from system import gui_params as params

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
    nextval = ''.join(random.choice(string.lowercase) for x in range(X))
    print(nextval)
    bar_obj.text = nextval

#print(x,y,width,height)

#add the text (across whole top bar) and the line to sepreate it
panel.add(text = gui.text(x, y, width, height, '12345678901234567890123453',color = line_color))
#print(panel.text.char_width)
panel.add(line = gui.rect(x,height,width, line_height, line_color))

panel.add(refresher = gui.operator(change_bar_text, ()))