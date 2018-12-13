#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18
'''NOTE: this was reverted to a no-switcher state for stability purposes:
these commits had the switcher: 823d71df1a2ddeef2c82163d846af495fa4a6dfa,
8af393393fb44851fb2e37c5fa3feb598e3eec07'''

#############IMPORTS###############################################################################
#harware specific or user specific boot
from gc import enable, collect, mem_free
enable()
import time
from supervisor import reload
collect()

#######################inits########################user and stock
try:
    from programs.user import __boot  
except: pass
collect()

try:
    from programs.stock import __boot  
except: pass
collect()

############system bootup screen#######################
#system  boot up screen
from system.boot import *
collect()


######setting up system#####################
#utilities
from tg_modules.tg_tools import holder
collect()

#io
try:
    from tg_io import io_button as button
    button_active = 1
except:
    button_active = 0
collect()

from system import handler_uni as handler

import sys_config

home_prog = sys_config.home_prog_name
collect()

if sys_config.use_keyboard:
    print('TG: keyboard active! use wasd and e keys')

#for ease of code / system container
system = holder()


#initial sys_bar setup
if sys_config.enable_sys_bar:
    system.add('sys_bar', 
                    handler.load('sys_bar', path  = 'system.programs',
                    to_system = True, place = 1))
#handler.cur_cont.place()

###THE launcher####################################################################################
#import the inti program (usually launcher to the )
system.add( home_prog, handler.load( sys_config.home_prog_name, 
                                                    sys_config.home_prog_path, 
                                                    not sys_config.home_prog_index))



###THE LOOP########################################################################################
collect()
last_sys_refresh = time.monotonic()
prev_cmds = []
while 1:
    try:
        #print(mem_free())
        collect()
        
        time.sleep(.1)
        if time.monotonic() - last_sys_refresh >= sys_config.system_refresh_interval:
            for process in system:
                process.container.refresh()
                
            last_sys_refresh = time.monotonic()
        
        if handler.cur_prog.wants_refresh:
            handler.cur_cont.refresh()
        
        #inputed commands
        cmd_list = []
        
        #interpert keyboard as button inputs
        if sys_config.use_keyboard:
            valin = str(input('your cmd(wasd):')).lower()
            #print(valin[0:5])
            if valin == 'EXIT_SYSTEM'.lower():
                print('atempting exit')
                break
            
            elif valin[0:5] == 'EXEC_'.lower():
                exec(valin[5:])
                continue
            elif valin == 'keyboard_off':
                sys_config.use_keyboard = 0
                print('turned off')
            for cmd in valin:
                #print(cmd)
                #try:
                    if cmd == 'h':
                        collect()
                        handler.load(home_prog)
                    try:
                        cmd_list.append({'w':'^', 'a':'<', 's':'V', 'd':'>', 'e':'E', 'p':'S'}[cmd[0]])
                    except:
                        cmd_list.append(cmd[0])
                    #time.sleep(.2)
                #except:
                    #print('err')
        
        #get pressed buttons
        if button_active:
            cmd_list += button.get_commands()
        
        #do touch system refresh here:
        #not implemented!
        
        #interpret commands
        for cmd in cmd_list:
                if sys_config.use_keyboard: # debug 
                    print(cmd)
                if cmd == 'H':  
                    collect()
                    if handler.cur_prog == system.get(home_prog):
                        pass # open app switcher
                        #print('smap')
                    else:
                        handler.load(home_prog)
                elif (cmd == 'S') and sys_config.settings_active:
                    if handler.cur_name == sys_config.settings_prog:
                        pass
                    else:
                        handler.load(sys_config.settings_prog, sys_config.settings_path)
                    
                handler.cur_cont.current.command(cmd)
        
        #try:handler.unload('example')
        #except: print('dsflkjs')
        
        del cmd_list
    except MemoryError:
        print('memory error! this is going to be fixed but currently is not')
        try:
            handler.cur_prog._save()
        except: pass
        reload()
    #time.sleep(.05)