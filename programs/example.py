##from system.programs.__blank__app import *
from system.programs.__blank__app import init
exec(init)

page = container.add_panel()

def change_rect_color(obj, col):
    obj.color = col


###########set up a menu that changes the 
page.add( rect = gui.rect(40, 30, 75 ,35, gui.io.red ))

page.add( menu = gui.nidos(10,80,140,40,2,2))

page.menu.of(0,0).set_purpose(change_rect_color,(page.rect, gui.io.green))
page.menu.of(0,0).text = 'Green'

page.menu.of(1,0).set_purpose(change_rect_color,(page.rect, gui.io.red))
page.menu.of(1,0).text = 'Red'

page.menu.of(0,1).set_purpose(change_rect_color,(page.rect, gui.io.blue))
page.menu.of(0,1).text = 'Blue'

page.menu.of(1,1).set_purpose(change_rect_color,(page.rect, gui.io.yellow))
page.menu.of(1,1).text = 'Yellow'