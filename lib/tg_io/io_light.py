#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/09/18

from tg_io.staging.tsl2591_setup import sensor as ts

###########inputs for your hardware############
contrast_ratio = 6000000000/1#big/littel
bit_len_vis = 32
bit_len_ir = 32
bit_len_ambi = 32

####################convention defs############

UNSUPPORTED = -03.1415926535
OUTOFRANGE = -13.1415926535
AHHHHHHH = -23.1415926535#seven "H"s


#############add in ur harware fetching code here########
###if ur harware does not support it return UNSUPPORTED
#if your sensor(s) don't measure that high return OUTOFRANGE
def get_ambi_brightness():
    return (ts.full_spectrum, 2**bit_len_ambi)

def get_vis_brightness():
    return (ts.visible, 2**bit_len_vis)

def get_ir_brightness():
    return (ts.infrared, 2**bit_len_ir)
    
def get_uv_brightness():
    return UNSUPPORTED


    