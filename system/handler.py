#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18

#for errors, not currently implemented#from tg_io import io_screen as io # for error programs\
from tg_modules.tg_tools import del_dict_value
import time 

#all programs by key
buffer = {}

#ordered prog lists sperated by type (user or system)
programs = []
system = []

# make accesing the current program esier by user (well coder)
global cur_prog, cur_cont
cur_prog = 7
cur_cont = 7

def load(name, path = 'programs', to_system = 0, err_func = None, err_tup = () ):
    try:
        #try to import if given name is not already loaded 
        if name not in buffer:
            exec('from '+path+' import ' + name)
            #put into the all programs buffer
            buffer[name] = eval(name)
        
        #ease of coding
        pointer = eval(name)
        
        # pick which list to add the add the module too 
        list_pointer = (programs, system)[int(bool(to_system))]
        
        #remove from list 
        try:
            list_pointer.pop(list_pointer.index(pointer))
        except ValueError:
           pass
        
        #place at  back of list (the most recent prog spot) 
        list_pointer.append(pointer)
        
        #set the ease of use variables
        global cur_prog, cur_cont
        cur_prog = buffer[name]
        cur_cont = cur_prog.container
        #print(cur_prog,cur_cont)

        '''try:
            all_progs.append( all_progs.pop( all_progs.index(pointer) ))
        except ValueError:
            all_progs.append(pointer)
        
        if index and not system:
            try:
                loaded_progs.append( loaded_progs.pop( loaded_progs.index(pointer) ))
            except ValueError:
                loaded_progs.append(pointer)
        elif system:
            try:
                index.append( index.pop( index.index(pointer) ))
            except ValueError:
                index.append(pointer)'''
            
        return eval(name)
        
    except MemoryError:
        target = programs.pop(0)
        del_dict_value(buffer,target)
        load(name, path = path, to_system = to_system, err_func = err_func,
                err_tup = err_tup)
    """except ImportError:
        if err_func:
            err_func(*err_tup)
        else:
            #raise the initial error (debugging purposes)
            exec('from '+path+' import ' + name) 
    except:
        #eventually implement an on screen error thing
        if err_func:
            err_func(*err_tup)
        else:
            exec('from '+path+' import ' + name) 
        '''io.text(cur_cont.cont_x,cur_cont.cont_y,'program load error', color = io.white,
                        background = io.red)
        
        time.sleep(.5)
        cur_cont.place()'''"""
            
            