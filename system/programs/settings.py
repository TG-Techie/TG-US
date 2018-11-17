#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/28/18  ****i misstyped before, it should have been 10/28/18 instead of 11/28/18 

'''try:
    from sys_config import DEBUG_module_locaiton_output as should_out
except:
    should_out = 0
if should_out:
    print('System Entered: ',__name__)'''


from system.programs.__blank__app import init
exec(init)

import sys_config, microcontroller as ctrl, system.programs.__pop_up__module as pop_up


(.2,.4,.5,.8,1)
def togl_bright(target):
    val = ((gui.io.get_backlight() - .2) % 1)
    if not val:
        val += .2
    gui.io.set_backlight( val )
    target.text = 'Brightness:'+str(round(val*5))+'/5'
    
    

#1st main panel for the menu
page0 = container.add_panel()

###setup nidos
page0.add(list = gui.nidos(cont_x, cont_y, cont_width, cont_height,  1, 6, superior = page0))


page0.list.of(0,2).set_purpose(togl_bright, (page0.list.of(0,2),) )
page0.list.of(0,2).text = 'Brighness'

page0.list.of(0,-2).set_purpose(pop_up.summon, (page0, ctrl.reset, (), 'Restart Device?'))
page0.list.of(0,-2).text = 'Restart'