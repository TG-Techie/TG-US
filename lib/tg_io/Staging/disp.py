#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

from gc import collect as clean_mem
import time
#import pins
from tg_io.staging.pin_port import disp_spi,disp_cs, disp_dc, disp_rst, backlight
clean_mem()
# import easy digital io
from tg_modules.make_ios import dio, pwm
clean_mem()


#start backlight in off position
#backlite = dio(backlight,0,False)
#backlite.value = False
backlite = pwm(backlight, 0)
del backlight
clean_mem()

#imports
from TG_Modules.TG_RGB.rgb import colorst as color
from TG_Modules.TG_RGB.st7735r import ST7735R

#setup the display as a car named "disp"
disp = ST7735R(disp_spi, cs=dio(disp_cs),dc=dio(disp_dc),rst=dio(disp_rst),rotation = 1 )

#reset again
disp.reset()
disp.init()

del disp_spi,disp_cs, disp_dc, disp_rst
clean_mem()



#start with black screen and elimiate noise
disp.fill(0)
#backlite.value = True
backlite.duty_cycle = 2**16 -1 


      