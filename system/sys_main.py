#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18
'''NOTE: this was reverted to a no-switcher state for stability purposes:
these commits had the switcher: 823d71df1a2ddeef2c82163d846af495fa4a6dfa,
8af393393fb44851fb2e37c5fa3feb598e3eec07'''

#############IMPORTS###############################################################################
#harware specific or user specific boot
from gc import enable, collect
enable()
collect()

#try:
from programs.user import __boot  
collect()
#except:
#    pass

#harware specific inits (like setting rtcs and other stuff)
from programs.stock import __boot  
collect()


# system boor (rtc and other stuff)
from system.boot import *
collect()

#utilities
from tg_modules.tg_tools import holder
import time
collect()

#io
from tg_io import io_button as button
collect()


#prog handler
#***handler uni only ever allows one program to be loaded!
#thus the switcher should be turned of or not implemented
#from system import handler_no_lap_uni as handler
from system import handler_uni as handler

#config and behavior
import sys_config# (in lib)
init_prog = sys_config.init_prog_name
collect()


#for ease of code / system container
system = holder()


#initial sys_bar setup
system.add('sys_bar', 
                    handler.load('sys_bar', path  = 'system.programs',
                    to_system = True, place = 1))
#handler.cur_cont.place()

###THE launcher####################################################################################
#import the inti program (usually launcher to the )
system.add( init_prog, handler.load( sys_config.init_prog_name, 
                                                    sys_config.init_prog_path, 
                                                    not sys_config.init_prog_index))


###THE LOOP########################################################################################
collect()
last_sys_refresh = time.monotonic()
prev_cmds = []
while 1:
    #print(gc.mem_free())
    collect()
    
    if not hasattr(handler.cur_prog, 'validation_ticket'):
        hanldler.load(init_prog)
    
    time.sleep(.1)
    if time.monotonic() - last_sys_refresh >= sys_config.system_refresh_interval:
        for process in system:
            process.container.refresh()
            
        last_sys_refresh = time.monotonic()
    
    #print('checking if shoulf refresh system')
    #print(handler.cur_prog)
    if handler.cur_prog.wants_refresh:
        handler.cur_cont.refresh()
        
    
    cmd_list = []
    
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
                    handler.load(init_prog)
                try:
                    cmd_list.append({'w':'^', 'a':'<', 's':'V', 'd':'>', 'e':'E'}[cmd[0]])
                except:
                    cmd_list.append(cmd[0])
                #time.sleep(.2)
            #except:
                #print('err')
    
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
    
    #try:handler.unload('example')
    #except: print('dsflkjs')
    
    del cmd_list
    
    #time.sleep(.05)
    
    