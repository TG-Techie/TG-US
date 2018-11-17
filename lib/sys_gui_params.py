#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/15/18
''' a file made for each device that changes gui shape and behavior'''

from tg_io import io_screen as io
try:
    from sys_config import enable_sys_bar as enable_sb
    from sys_config import enable_nav_bar as enable_nb
except:
    enable_sb = 0
    enable_nb = 0



#touch screen nav bar
nav_bar_height = 0

#top system bar shape and size
sys_bar_pos =  (0*enable_sb,0*enable_sb)
sys_bar_dims = (io.screen_width*enable_sb,10*enable_sb)
sys_bar_line_thickness = 2*enable_sb
sys_bar_line_color = io.white

launch_cols = 3
launch_rows = 2
launch_move_loop = 0

#program windows size and stds
move_loop = 0 #should user be able to go from the last panel in window to the first
prog_pos = ( sys_bar_pos[0], sys_bar_pos[1] + sys_bar_line_thickness + sys_bar_dims[1])
prog_dims = (io.screen_width - prog_pos[0], io.screen_height - prog_pos[1] - nav_bar_height)
prog_color_clear = io.background_color
prog_background = io.background_color

#this tells the program handler if the program wants refreshing in blank app
wants_refresh = False