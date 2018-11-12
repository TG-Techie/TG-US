#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/28/18

from system.programs.__blank__app import init
exec(init)

def togl_bright():
    gui.io.set_backlight( (gui.io.get_backlight() + .2) % 1.1 )
    

page = container.add_panel()

page.add(list = gui.nidos(cont_x, cont_y, cont_width, cont_height,  1, 6, superior = page))

page.list.of(0,4).text = 'Brighness'
page.list.of(0,4).set_purpose(togl_bright, () )