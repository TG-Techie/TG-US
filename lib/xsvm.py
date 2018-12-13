#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 12/03/18

from adafruit import adafruit_fram as fram_module

from tg_io.staging.pin_Port import i2c_port

size = 32*1000

ByteArray  = fram_module.FRAM_I2C(i2c_port)
