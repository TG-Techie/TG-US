#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/05/18

from gc import collect
from tg_io.staging.pin_port import i2c_port


#####SETUP THE HARWARE ()################################################################
from adafruit import adafruit_amg88xx as amg
collect()

chip = amg.AMG88XX(i2c_port)

for i in range(3):
    (chip.pixels)
    collect()
######################################
#This library only outputs Celsius so here are some tools 
######################################
def c2f(val):
    return (val*9/5) +32

def f2c(val):
    return (val-32)*5/9
    
def c2k(val):
    return val + 273
    
def k2c(val):
    return val - 273
        
### None = 0, c = 1, f = 2 k = 3###
units = 1

def get_image():
    #harware specific
    # make it usable like: list[x][y]
    return chip.pixels