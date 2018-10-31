
import time
from tg_io.staging.pin_port import i2c_port
from adafruit_bus_device.i2c_device import I2CDevice
# Import MPR121 module.
from adafruit import adafruit_mpr121

# Create MPR121 class.
cap0 = adafruit_mpr121.MPR121(i2c_port)
#cap1 = adafruit_mpr121.MPR121(i2c_port, address=0x91)

# Note you can optionally change the address of the device:
#mpr121 = adafruit_mpr121.MPR121(i2c, address=0x91)
