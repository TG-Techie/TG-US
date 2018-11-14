#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/28/18

from system.programs.__blank__app import init
exec(init)

(.2,.4,.5,.8,1)
def togl_bright(target):
    val = ((gui.io.get_backlight() - .2) % 1)
    if not val:
        val += .2
    gui.io.set_backlight( val )

    target.text = 'Brightness:'+str(round(val*5))+'/5'

    

page = container.add_panel()

page.add(list = gui.nidos(cont_x, cont_y, cont_width, cont_height,  1, 6, superior = page))

page.list.of(0,2).text = 'Brighness'
page.list.of(0,2).set_purpose(togl_bright, (page.list.of(0,2),) )
