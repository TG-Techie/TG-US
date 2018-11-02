#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18

#############IMPORTS###############################################################################
#harware specific or user specific boot
import gc
gc.enable()
gc.collect()

#try:
from programs.__boot import *
gc.collect()
#except:
#    pass


# system boor (rtc and other stuff)
from system.boot import *
gc.collect()

#utilities
from tg_modules.tg_tools import holder
import time
gc.collect()

#io
from tg_io import io_button as button
gc.collect()


#ram handler and config of behavior
from system import sys_config, handler
init_prog = sys_config.init_prog_name
gc.collect()


#for ease of code / system container
system = holder()


#initial sys_bar setup
system.add('sys_bar', 
                    handler.load('sys_bar', path  = 'system.programs', to_system = True))
#handler.cur_cont.place()

###THE launcher####################################################################################
#import the inti program (usually launcher to the )
system.add( init_prog, handler.load( sys_config.init_prog_name, 
                                                    sys_config.init_prog_path, 
                                                    not sys_config.init_prog_index))


###THE LOOP########################################################################################
gc.collect()
last_sys_refresh = time.monotonic()
while 1:
    #print(gc.mem_free())
    gc.collect()
    #print(gc.mem_free())
    #print(time.monotonic())
    #print(time.monotonic() - last_sys_refresh)
    time.sleep(.1)
    if time.monotonic() - last_sys_refresh >= sys_config.system_refresh_interval:
        for process in system:
            process.container.refresh()
        last_sys_refresh = time.monotonic()
    
    if handler.cur_prog.wants_refresh:
        #print('moop')
        handler.cur_cont.refresh()
    
    cmd_list = []
    
    if sys_config.use_keyboard:
        valin = str(input('your cmd(wasd):')).lower()
        if valin == 'EXIT_SYSTEM'.lower():
            print('atempting exit')
            break
            break
            break
        for cmd in valin:
            #print(cmd)
            try:
                if cmd == 'h':
                    handler.load(init_prog)
                try:
                    cmd_list.append({'w':'^', 'a':'<', 's':'V', 'd':'>', 'e':'E'}[cmd[0]])
                except:
                    cmd_list.append(cmd[0])
                #time.sleep(.2)
            except:
                print('err')
    
    #get cap touched buttons
    cmd_list += button.get_commands()
    
    #print(cmd_list)
    #print(cmd_list)
    for cmd in cmd_list:
        if sys_config.use_keyboard: # debug 
            print(cmd)
        if cmd == 'H':  
            if handler.cur_prog == system.get(init_prog):
                pass # open app switcher
                #print('smap')
            else:
                handler.load(init_prog)
            
        handler.cur_cont.current.command(cmd)
        
    
    del cmd_list
    
    #time.sleep(.05)
    
    