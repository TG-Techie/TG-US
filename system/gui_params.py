#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/15/18
''' a file made for each piece of hw that changes gui shape and behavior'''

from tg_io import io_screen as io

sys_bar_pos =  (0,0)
sys_bar_dims = (io.screen_width,10)
sys_bar_line_thickness = 2
sys_bar_line_color = io.white

nav_bar_height = 0

prog_pos = ( 0, sys_bar_pos[1] + sys_bar_line_thickness)
prog_dims = (io.screen_width - prog_pos[0], io.screen_height - prog_pos[1] - nav_bar_height)