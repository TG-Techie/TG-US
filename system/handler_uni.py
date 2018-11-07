#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18

#for errors, not currently implemented#from tg_io import io_screen as io # for error programs
import sys_config
from tg_modules.tg_tools import del_dict_value #ease of life thing
from tg_modules.tg_gui import window
import time#,sys
from gc import collect

#ordered prog lists sperated by type (user or system)
global system, programs
programs = []
system = []

# make accesing the current program esier by user (well coder)
#global cur_prog, cur_cont, cur_name
cur_prog = 7
cur_cont = 7
cur_name = 'filler_string'


def load(name, path = sys_config.std_path, to_system = 0, place = 1):
    global system, programs, cur_prog, cur_cont, cur_name
    #print(cur_name)
    #print(cur_prog)
    #print([x[1] for x in system])
    if cur_prog in [x[1] for x in system]:
        try:
            cur_prog._save()
        except:pass
        
        '''try:
            asdf;kljfgd
            
            cur_cont.clear()
        except: pass'''
        
    else:
        try:
            cur_prog._save()
        except:pass
        
        try:
            cur_cont.clear()
        except: pass
        
        try:
            del cur_prog
            del cur_cont
            exec('del '+cur_name)
        except: pass
        
    #if teh given name is in system place it from system and then return
    if name in [x[0] for x in system]:
        for mod_tup in system:
            if mod_tup[0] == name:
                cur_name = name
                cur_prog = mod_tup[1]
                cur_cont = mod_tup[1].container
                if place:
                    cur_cont.place()
                collect()
                return mod_tup[1]
    
    
    
    exec('from '+path+' import ' + name )
    if to_system:
        system.append((name, eval(name)))
    
    cur_prog = eval(name)
    cur_cont = eval(name).container
    
    if place:
        cur_cont.place()
    
    collect()
        
    return cur_prog
    
    
    
    
    
'''def load(name, path = sys_config.std_path, to_system = 0, err_func = None, err_tup = (), place = 1, _raise = 0):
    global system, programs, cur_prog, cur_cont
    try:
        if name not in buffer:
            #import the module b/c it is not in ram
            exec('from '+path+' import ' + name)
            
            buffer[name] = eval(name)
            
            if to_system:
                system.append(buffer[name])
            else:
                programs.append(buffer[name])
            #print(programs,system)
        
        pointer = eval(name)
        
        if pointer in programs:
            programs.append(programs.pop(programs.index(pointer)))
        elif pointer in system:
            system.append(system.pop(system.index(pointer)))
        
        if cur_prog == pointer:
            # this means no change is needed
            #clean up ram then return to user
            collect()
            return cur_prog
        #else:
            #if (type(cur_cont) == window) and (cur_prog in programs):
                #cur_cont.clear()
            
        #save the previous program
        try: cur_prog.save()
        except: pass
        
        cur_cont = pointer.container
        cur_prog = pointer
        
        if place:
            cur_cont.place()
        
        collect()
        return cur_prog
        
    except MemoryError:
        print('TG: handler memeory error, unable to laod: '+name)
        try:
            unload(programs.pop(0))
        except:
            print('TG:MemoryError, try rebooting unable to unload more modules')
        collect()
        pass
    collect()


            
def unload(name):
    if type(name) == str:
        programs.pop(programs.index(buffer[name]))
        del buffer[name]
        collect()
    else:
        try:
            programs.pop(programs.index(name))
        except: pass
        try:
            del_dict_value(buffer, name)
        except:pass
    collect()

def loaded():
    return [_get_name(x) for x in programs]'''

'''def _get_name(module):
    for key in buffer:
        if system[key] == module:
            return key
    raise KeyError('TG: Program not loaded')'''

def unload(arg):
    pass

def loaded():
    return ['no buffer in apps']
    
def get_name(arg):
    try:
        return arg.__name__
    except:
        return 'HANDLER_UNI ERRORfmoop - unsupported inpuprtpojgsdojsg  ww2e3fksfkpp340-86uy0u8w-u9472935h-[0]PIRGJNVLJ '