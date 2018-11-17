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
    print(name)
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
        
        '''try:
            del cur_prog
            del cur_cont
            exec('del '+cur_name)
        except: pass'''
        
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
  
    fmoop = 5
    print(cur_prog)
    #exec('from '+path+' import ' + name )
    print((('from '+path+' import ' + name + ' as cur_prog' ,)))
    exec('from system.programs import sys_bar')
    print(cur_prog)
    exec('from '+path+' import ' + name + ' as cur_prog', {'cur_prog':cur_prog})
    print(cur_prog)
    print(name, cur_prog)
    if to_system:
        #system.append((name, eval(name)))
        system.append((name, cur_prog))
    
    #cur_prog = eval(name)
    #cur_cont = eval(name).container
    cur_cont = cur_prog.container
    
    if place:
        cur_cont.place()
    
    collect()
        
    return cur_prog
    
    

def unload(arg):
    pass

def loaded():
    return ['no buffer in apps']
    
def get_name(arg):
    try:
        return arg.__name__
    except:
        return 'HANDLER_UNI ERRORfmoop - unsupported inpuprtpojgsdojsg  ww2e3fksfkpp340-86uy0u8w-u9472935h-[0]PIRGJNVLJ '