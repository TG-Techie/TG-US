#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/05/18

from system.programs.__blank__app import init
exec(init)
wants_refresh = True

from tg_io.io_thermal_cam import get_image

def flipped_data():
    dat = get_image()
    dat.reverse()
    return dat



pan = container.add_panel()



pan.add(grid = gui.grid_display(cont_x, cont_y, 9*10, 9*10, flipped_data, (), border = 5))