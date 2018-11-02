#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18

#for errors, not currently implemented#from tg_io import io_screen as io # for error programs
from system import sys_config
from tg_modules.tg_tools import del_dict_value #ease of life thing
import gc,time,sys

#all programs by key
buffer = {}

#ordered prog lists sperated by type (user or system)
programs = []
system = []

# make accesing the current program esier by user (well coder)
global cur_prog, cur_cont
cur_prog = 7
cur_cont = 7

def load(name, path = sys_config.std_path, to_system = 0, err_func = None, err_tup = (), place = 1, _raise = 0):
    while (len(buffer) >8) and not _raise:
        unload(_get_name(programs[0]))
        
    try:
        if _raise:
            raise MemoryError()
        #print(name)
        #print('atmpt load: ', name)
        #try to import if given name is not already loaded 
        if name not in buffer:
            #print("it wasn't in buffer", buffer, '\n')
            #see if can be imported
            #try:
            for i in [1]:
                #try: 
                    exec('from '+path+' import ' + name)
                #except: exec('from '+'programs'+' import ' + name)
            #except:
                #raise ImportError("""TG:RUNTIME: either the given program to laod is not 
#present or there is an error in the given program""")
            
            #put into the all programs buffer
            buffer[name] = eval(name)
            #print('added to buffer', buffer, '\n')
        
        #ease of coding
        pointer = eval(name)
        #print(pointer, '\n')
        
        # pick which list to add the add the module too 
        list_pointer = (programs, system)[int(bool(to_system))]
        
        #remove from list 
        try:
            list_pointer.pop(list_pointer.index(pointer))
        except ValueError:
           pass
        
        #place at  back of list (the most recent prog spot) 
        list_pointer.append(pointer)
        
        global cur_prog, cur_cont
        
        # clear and close the current prog
        # if loading a program that is already present dont 
        #replaceit else clear the current program
        if pointer == cur_prog:
            return pointer
        
        #save (not implemented)
        try: cur_prog.save()
        except: pass
        
        #print(name, buffer[name],buffer[name].container)
        
        #print(cur_prog, cur_cont)
        
        #set the ease of use variables
        cur_cont = buffer[name].container
        cur_prog = buffer[name]
        
        #print(cur_prog, cur_cont)
        
        cur_cont = cur_prog.container
        #print(cur_prog,cur_cont)
        #print(cur_prog, cur_cont)
        
        #if place:
        cur_cont.place()
        #time.sleep(2)
        
        gc.collect()
        return eval(name)
        
    except MemoryError:
        target = programs.pop(0)
        del_dict_value(buffer,target)
        
        try: exec('del ')
        except: pass
        
        if not _raise:
            load(name, path = path, to_system = to_system, err_func = err_func,
                err_tup = err_tup)
        gc.collect()
    gc.collect()
            
def unload(name = None ):
    load(name , _raise = 1)

def _get_name(module):
    for key in buffer:
        if buffer[key] == module:
            return key
    raise KeyError('TG: Program not loaded')

def loaded():
    pass