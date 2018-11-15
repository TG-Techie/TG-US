#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/14/18


from tg_io.staging.mcp9808_setup import mcp

##here are some tools ######################################
def c2f(val):
    return (val*9/5) +32

def f2c(val):
    return (val-32)*5/9
    
def c2k(val):
    return val + 273
    
def k2c(val):
    return val - 273


###fill in harware reporint values##########

max = 125 # max fo sensor in degree c!
min = -25

def get_temp_c():
    return mcp.temperature

def get_temp_f():
    return c2f(mcp.temperature)

def get_temp_k():
    return c2k(mcp.temperature)
    