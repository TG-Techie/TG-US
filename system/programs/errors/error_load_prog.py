#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/09/18
from system.sys_main import handler

from system.programs.__blank__app import init
exec(init)

page = container.add_panel()
page.background = color.white

message = '''ERROR: program unloadable

!!!NO WORRIES: just go home
to leave this screen!

>>> there was an error
loading a program

plug into a serial com
port for error output'''

page.add( text = gui.text(cont_x,cont_y,cont_width, cont_height, message, background = color.blue))