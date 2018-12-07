#this is a hello world!

#this will set up the framework and standards for the system to interpret your app
from system.programs.__blank__app import init
exec(init)

#tell the system that your program does not need refreshing:
wants_refresh = False

#add a new page "panel" to teh window
my_page = container.add_panel()

#add a text object to the screen
#cont_x and cont_y must be included in x and y values(will be fixed later)
my_page.add( my_text = gui.text(cont_x+10, cont_y+10, cont_width, 20,'Hello World!'))