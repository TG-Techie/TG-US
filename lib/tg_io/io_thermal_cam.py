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

def get_image():
    #harware specific
    # make it usable like: list[x][y]
    return chip.pixels