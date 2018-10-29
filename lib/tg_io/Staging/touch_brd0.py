
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

# Loop forever testing each input and printing when they're touched.
'''def test( duration = 12):
    init_time = time.monotonic()
    # Loop through all 12 inputs (0-11).
    while 1:
        if (time.monotonic()-init_time <= duration):
            for i in range(12):
                # Call is_touched and pass it then number of the input.  If it's touched
                # it will return True, otherwise it will return False.
                if mpr121[i].value:
                    print('Input {} touched!'.format(i))
            #time.sleep(0.25)  # Small delay to keep from spamming output messages.'''