#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

# a simple program that takes all the modules in gui_modules
# and imports them all under the name tg_gui

#with a list of imported guis 

from os import listdir

modules = []

modules_list = listdir('./lib/tg_modules/gui_modules')
for module in modules_list:
    if (module[0:2] != '._' and module[0:2] !=  '__') and ( '.py' in module):
        #try:
            modules.append(module.replace('.py',''))
            #print('from tg_modules.gui_modules.'+ module.replace('.py','') +' import *')
            #print(module[0:2])
            #print('from tg_modules.gui_modules.'+ module.replace('.py','') +' import *')
            exec('from tg_modules.gui_modules.'+ module.replace('.py','') +' import *')
        #except ImportError:
            #raise ImportError('TG: Failed: from tg_modules.gui_modules.'+ module.replace('.py','') +' import *')