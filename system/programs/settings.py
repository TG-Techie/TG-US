#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/28/18  ****i misstyped before, it should have been 10/28/18 instead of 11/28/18 

from system.programs.__blank__app import init
exec(init)

import sys_config, microcontroller as ctrl



(.2,.4,.5,.8,1)
def togl_bright(target):
    val = ((gui.io.get_backlight() - .2) % 1)
    if not val:
        val += .2
    gui.io.set_backlight( val )
    target.text = 'Brightness:'+str(round(val*5))+'/5'

def query_restart(page):
    width17 = int(cont_width/7)
    height15 = int (cont_height/5)
    pop = gui.panel(cont_x + width17, cont_y + height15, 
                    cont_width - width17*2, cont_height - height15*2, background = gui.io.blue)
    pop.add(yes_no = 7)
    page.add( pop = pop)
    page.nav = pop.yes_no
    

#1st main panel for the menu
page0 = container.add_panel()

###setup nidos
page0.add(list = gui.nidos(cont_x, cont_y, cont_width, cont_height,  1, 6, superior = page0))

page0.list.of(0,2).text = 'Brighness'
page0.list.of(0,2).set_purpose(togl_bright, (page0.list.of(0,2),) )

page0.list.of(0,-2).text = 'Restart'
page0.list.of(0,-2).set_purpose(query_restart, (page0))