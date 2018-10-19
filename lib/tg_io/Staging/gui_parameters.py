#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

from tg_modules import screen_io as io

screen_width = io.screen_width
screen_height = io.screen_height

gui_background = io.background_color
gui_standard_color = io.standard_color
gui_white = io.white 

gui_move_mode = 1

sys_bar_x = 0
sys_bar_y = 0
sys_bar_height = 12
sys_bar_width = screen_width
sys_bar_color = io.background_color
sys_bar_line_color = gui_white
sys_bar_line_height = 2

prog_cont_x = 0
prog_cont_y = sys_bar_height

prog_cont_width = screen_width
prog_cont_height = screen_height - sys_bar_height

init_select = 1

launcher_cols = 3
launcher_rows = 3
