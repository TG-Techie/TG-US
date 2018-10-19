#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

# set std colors for the hardware
from tg_io.staging.disp import color


# Defaults:
#general:
red = color(255,0,0)
orange = color(255,128,0)
yellow = color(255,255,0)
green = color(0,255,0)
blue = color(0,0,255)
purple = color(255,0,255)
white = color(255,255,255)
black = color(0,0,0)

standard_color =  color(5,85,110)
standard_color_sel =  color(128,255,255)
background_color =  color(0,0,0)


#menus and nidos' (navigatable informat  dispensing object systems)
nidos_background =  background_color

#buttons:
button_color_norm = standard_color
button_clear_color = nidos_background
button_color_sel =  standard_color_sel

text_color_norm =  color(255,255,255)
text_color_sel =  color(0,0,0)