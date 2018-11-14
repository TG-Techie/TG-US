#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/09/18

from tg_io.staging.tsl2591_setup import sensor as ts

####################convention defs############

UNSUPPORTED = -03.1415926535
OUTOFRANGE = -13.1415926535
AHHHHHHH = -23.1415926535#seven "H"s

#############add in ur harware fetching code here########
###if ur harware does not support it return UNSUPPORTED
#if your sensor(s) don't measure that high return OUTOFRANGE
def get_vis_brightness():
    return ts.lux

def get_ir_brightness():
    pass 
    
def get_uv_brightness():
    return UNSUPPORTED
    