#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18

#############IMPORTS###############################################################################
#harware specific or user specific boot
import gc

try:
    from programs.__boot import *
except:
    pass


# system boor (rtc and other stuff)
from system.boot import *

#utilities
from tg_modules.tg_tools import holder
import time

#ram handler and config of behavior
from system import sys_config, handler

#for ease of code / system container
system = holder()

#initial sys_bar setup
system.add('sys_bar', 
                    handler.load('sys_bar', path  = 'system.programs', to_system = True))
#handler.cur_cont.place()



system.add( sys_config.init_prog_name, handler.load( sys_config.init_prog_name, 
                                                    sys_config.init_prog_path, 
                                                    not sys_config.init_prog_index))

###THE LOOP########################################################################################

last_sys_refresh = time.monotonic()
while 1:
    #print(time.monotonic() - last_sys_refresh)
    time.sleep(.1)
    if time.monotonic() - last_sys_refresh >= sys_config.system_refresh_interval:
        for process in system:
            process.container.refresh()
        last_sys_refresh = time.monotonic()
    
    handler.cur_cont.refresh()
    
    if sys_config.use_keyboard:
        valin = str(input('your cmd(wasd):')).lower()
        for cmd in valin:
            print(cmd)
            try:
                try:
                    handler.cur_cont.current.command({'w':'^', 'a':'<', 's':'V', 'd':'>', 'e':'E'}[cmd[0]])
                except:
                    handler.cur_cont.current.command(cmd[0])
                time.sleep(.2)
            except:
                print('err')
    
    time.sleep(.1)
    
    