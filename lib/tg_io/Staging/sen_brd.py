#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

#list of chips:
    #ccs811
    #mcp9808
    #tsl2591
    #veml6070
    #as7262
    #amg8833
    #bme280
    #ir_tx led
    #ir_rx led w/ filter
    #neopixel x1
    #neopixel x5

from staging.pin_port import i2c_port

#################################
#amg8833 thermal mini camera
from adafruit.adafruit_amg88xx import AMG88XX

amg = AMG88XX(i2c_port)

'''##################################
# gas sensor ccs811
try:
    from adafruit.adafruit_ccs811 import CCS811

    ccs = CCS811(i2c_port)
except:
    pass'''
