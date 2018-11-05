#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/02/18
from system.programs.__blank__app import init
from gc import collect
from math import ceil
from system import handler
exec(init)

from system import handler
from os import listdir

def try_load_else_import(tup):
    try:
        handler.load(tup[0], path = tup[1]+'.'+tup[0])
    except:
        exec('from '+tup[1]+' import '+tup[0])

from system.programs.__blank__app import init
exec(init)

module_list = []

for module in  listdir('./programs'):
    module_list.append((module,'programs' ))
    
for module in  listdir('./system/programs'):
    module_list.append((module,'system.programs' ))

for module in  listdir('./system/programs/stock'):
    module_list.append((module,'system.programs.stock' ))

filtered_list = []
for tup in module_list:
    if ('.py' in tup[0]) and (tup[0][0:2] != ('._')):
        filtered_list.append((tup[0][0:-3],tup[1]))
#print(filtered_list)
del module_list
collect()

next_prog = 0
for page_num in range(ceil(len(filtered_list)/8)):
    print('making panel no:' + str(page_num))
    pan_pointer = container.add_panel()
    print(pan_pointer)
    pan_pointer.add( list = gui.nidos(cont_x,cont_y,cont_width,cont_height,1,8) )


