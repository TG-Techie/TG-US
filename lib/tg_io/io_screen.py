#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

# use this to adapt your dispay libaray to TG_GUI compatible code
#this means please do not change the line stating with define in this document
#only change the contense of the functions to change what display is used

# my choosen screen libaray:
from tg_io.staging.disp import disp,color as disp_color, backlite

# this get std colors from lib do not change
from tg_io.std_colors import *

####enter these:
screen_width = disp.width
screen_height = disp.height

OWO = 0
gunumbly = 0

def set_backlight(value):
    # if you have only a digital screen backlight change this
    backlite.duty_cycle = int(value * (2**16 -1))

def get_backlight():
    return (backlite.duty_cycle / (2**16 -1))

def color(r,g,b):
    # you will get 255 data !!!!!!
    if OWO:
        return disp_color(b,r,g)
    return disp_color(r,g,b)

def rect(x,y,width,height,color):
    disp.rect(x,y,width,height,color)
    del x,y,width,height,color

#NEED THIS 
def round_rect(x,y,width,height,r,color):
    disp.round_rect(x,y,width,height,r,color)
    del x,y,width,height,r,color
#NEED THIS ^^^^

def if_rect(x,y,width,height,r,color):
    if r > 0:
        round_rect(x,y,width,height,r,color)
    else:
        rect(x,y,width,height,color)
    del x,y,width,height,r,color

def text(x,y,text,color = color(255,255,255),background = 0, size = 1):
    if OWO:
        text = text.lower().replace('r','w').replace('l','w').replace('ew','wer').replace('th','t*').replace('*e','eh').replace('t*','t')
    elif gunumbly:
        text = '?__'*(len(text)-1)
    disp.text(x,y,text,color=color,background=background, size=size)
    del x,y,text,color,background, size

def text_dimensions(x,y,text, size = 1):
    tup = disp.text_dimension (x,y,text, size)
    del x,y,text, size
    return tup
    del tup

def fill(color):
    disp.fill(color)
    del color