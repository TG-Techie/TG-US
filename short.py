from tg_modules.tg_rgb.ili9341 import ILI9341

import busio
import digitalio
import board
from tg_modules.tg_rgb.rgb import colorili
import tg_modules.tg_rgb.ili9341 as ili9341
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
display = ili9341.ILI9341(spi, cs=digitalio.DigitalInOut(board.D1),dc=digitalio.DigitalInOut(board.D2))
display.fill(colorili(0xff, 0x11, 0x22))
display.pixel(120, 160, 0)
print('done')