#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/18/18

import time

'''from sys_config import DEBUG_module_locaiton_output as should_out
if should_out:
    print('System Entered: ',__name__)'''
#print(tc.get_image())

from system.programs import settings as s

#s.restart_query(s.page0)


import sys_config as sc

sc.init_prog_name = 'settings'
'''
from system.programs import __pop_up__module as pp

gui = pp.gui

cont = gui.window(pp.cont_x,pp.cont_y,pp.cont_width,pp.cont_height, background = gui.io.yellow)
x = cont.add_panel()
cont.place()

pp.summon(x,print,('POP_UP: BridgeKeeper: Who would cross the bridge of death must answer me these questions three ere the other side he see',),'This is a MP pop up')


#x.nav.move(1,0)
x.nav.press()

time.sleep(1)'''

from system import sys_main