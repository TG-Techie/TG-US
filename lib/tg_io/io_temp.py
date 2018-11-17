#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/14/18


from tg_io.staging.mcp9808_setup import mcp

#####constanst based on chip capabilities####
MAX = 125 # max fo sensor in degree c!
MIN = -25

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

def get_temp_c():
    #print(mcp.temperature)
    return mcp.temperature

def get_temp_f():
    return c2f(mcp.temperature)

def get_temp_k():
    return c2k(mcp.temperature)
    