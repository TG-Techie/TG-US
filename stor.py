import adafruit_si7021
import board
import busio
import digitalio
import gc
import math
import microcontroller
import neopixel
import time

# PINs
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel[0] = (0, 0, 10)
redled = digitalio.DigitalInOut(board.D13)
redled.direction = digitalio.Direction.OUTPUT
sgnd = digitalio.DigitalInOut(board.D5) # make this pin ground for si7021 sensor
sgnd.direction = digitalio.Direction.OUTPUT
sv0 = digitalio.DigitalInOut(board.D6) # make this pin one of the two powers
sv0.direction = digitalio.Direction.OUTPUT
svin = digitalio.DigitalInOut(board.D9) # make this pin one of the two powers
svin.direction = digitalio.Direction.OUTPUT
redled.value = True
sgnd.value = False # set ground
sv0.value = True # set power
svin.value = True # set power

# si7021 sensor
time.sleep(1)
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

# calculate current Vapour-pressure deficit
def vpd(temp, rh):
    # Estimated Saturation Pressures
    # Saturation Vapor Pressure method 1
    es1 = 0.6108 * math.exp(17.27 * temp / (temp + 237.3))
    # Saturation Vapor Pressure method 2
    es2 = 6.11 * 10**((7.5 * temp) / (237.3 + temp)) / 10
    # Saturation Vapor Pressure method 3
    es3 = 6.112 * math.exp(17.62 * temp / (temp + 243.12)) / 10
    # Saturation Vapor Pressure mean
    es = (es1 + es2 + es3) / 3
    # actual partial pressure of water vapor in air
    ea = rh / 100 * es
    # return Vapour-pressure deficit
    vpd = es - ea
    return vpd

# write to FLASH, use similar to a print()
def sdwrite(sdlog):
    with open("/vpd.txt", "a") as fp:  # open to add line to log.txt
        redled.value = True  # turn on Red LED when SD in use
        print(sdlog)  # print what your about to write to SD
        fp.write(sdlog)  # write to SD
        fp.flush()  # what does this do, hope it helps????
        redled.value = False  # turn off Red LED when SD is done

pixel[0] = (0, 0, 0)
print("Basic Logging of Vapour-pressure Deficit to filesystem")
# write at start or reset
sdwrite('-Reset-\r\n')
sdwrite('\r\n')

while True:
    try:
        pixel[0] = (10, 0, 10)
        # CPU temperature
        cput = microcontroller.cpu.temperature
        # write to text filesystem
        sdwrite('CPU Temp = {}\r\n'.format(round(cput, 1)))
        sdwrite('Sensor: C {}'.format(round(sensor.temperature, 1)))
        sdwrite(', F {}'.format(round((sensor.temperature * 1.8 + 32), 1)))
        sdwrite(', {}%\r\n'.format(round(sensor.relative_humidity), 1))
        currentVPD = vpd(sensor.temperature, sensor.relative_humidity)
        sdwrite('VPD = {}\r\n'.format(round(currentVPD, 2)))
        sdwrite('\r\n')
        pixel[0] = (0, 0, 0)
        gc.collect()
        print(gc.mem_free())
        
        # blink and neopixel yellow after writing for 3 seconds
        for i in range(3):
            redled.value = True
            pixel[0] = (0, 0, 0)
            time.sleep(0.5)
            pixel[0] = (2, 2, 0)
            redled.value = False
            time.sleep(0.5)
         
        # Blink and neopixel green while waiting 9.5 mins before writing again
        for i in range(270):
            pixel[0] = (0, 0, 0)
            time.sleep(1)
            pixel[0] = (0, 5, 0)
            time.sleep(1)
        
        # Blink and neopixel green faster for 27 sec when about to write
        for i in range(67):
            pixel[0] = (0, 0, 0)
            time.sleep(0.2)
            pixel[0] = (0, 5, 0)
            time.sleep(0.2)

        # blink and neopixel red faster for 3 sec when about to write
        for i in range(8):
            redled.value = True
            pixel[0] = (0, 0, 0)
            time.sleep(0.2)
            pixel[0] = (5, 0, 0)
            redled.value = False
            time.sleep(0.2)
            
    # skip errors but try to print them
    except OSError as oe:
        print('OSError = ', oe)
        time.sleep(1)
        pass
    except RuntimeError as re:
        print('RuntimeError = ', re)
        time.sleep(1)
        pass
