#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/05/18

from system.programs.__blank__app import init
exec(init)
#print(gui.modules, dir(gui), dir())
gui.add_module('gui_thermal_cam')
#print(gui.modules, dir(gui), dir())
wants_refresh = True

from tg_io.io_thermal_cam import get_image, units
import time

def flipped_data_func():
    dat = get_image()
    dat.reverse()
    return dat
    
def toggle_units(target):
    target.units_out += 1
    if target.units_out == 4:
        target.units_out = 1

#global wants_refresh

def toggle_prog_refresh(but):
    global wants_refresh
    wants_refresh = not wants_refresh
    #print(('Toggle\nRefresh:\nOFF','Toggle\nRefresh:\nON')[wants_refresh])
    but.text = ('Toggle\nRefresh:\nOFF','Toggle\nRefresh:\nON')[wants_refresh]
    #time.sleep(.2)

#add panel
pan = container.add_panel()

#add grid and menus
pan.add(menu = gui.nidos(cont_x+100, cont_y, cont_width - 100, cont_height, 1, 3, x_gap = 5, y_gap =5) )
pan.add(grid = gui.thermal_display(cont_x+5, cont_y+5, 9*10, 9*10, flipped_data_func, (), border = 5,units_in = units, units_out = 1))


pan.menu.of(0,0).set_purpose(toggle_units,(pan.grid,))
pan.menu.of(0,0).text = 'Toggle\nUnits'

pan.menu.of(0,1).set_purpose(toggle_prog_refresh,(pan.menu.of(0,1),) )
pan.menu.of(0,1).text = 'Toggle\nRefresh'#:\nON'

pan.menu.of(0,2).set_purpose(pan.grid.refresh,())
pan.menu.of(0,2).text = 'Refresh'
    