#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

import board, busio, time
from tg_modules import make_ios as ezio

time.sleep(.1)
#metro m4 express:
#['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'D0', 'RX', 'D1', 'TX', 'D2', 'D3',
#'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'SDA',
#'SCL', 'AREF', 'NEOPIXEL', 'SCK', 'MOSI', 'MISO', 'LED_RX', 'LED_TX']

#i2c
try:
    sda = board.SDA
    scl = board.SCL
    i2c_port = busio.I2C(scl, sda)
except Exception as e:
    print('TG:HW: unable to create i2c port')
    print(e)

#uart port for gps
try:
    utx = board.TX
    urx = board.RX
    uart_port = busio.UART(utx, urx, baudrate=9600, timeout=3000)
except Exception as e:
    print('TG:HW: unable to create uart port')
    print(e)

#spi for display
try:
    backlight = board.D9
    disp_sck = board.SCK
    disp_mosi = board.MOSI
    disp_miso = board.MISO
    disp_cs = board.D8
    disp_dc = board.D7
    disp_rst = board.D10
    disp_spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
except Exception as e:
    print('TG:HW: unable to create DISP SPI port')
    print(e)

try:
    spkr_pin = board.A1
    spkr_en_pin = board.A2
    spkr_en = ezio.dio(spkr_en_pin, 0)
    spkr = ezio.sndio(spkr_pin)
except Exception as e:
    print('TG:HW: unable to create spkr pins')
    print(e)

time.sleep(.1)