# The MIT License (MIT)
#
# Copyright (c) 2017 Radomir Dopieralski and Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
'simplified driver for st7735r'
based on
`adafruit_rgb_display.st7735`
====================================================
A decent driver for the ST7735R displays mweant for use with the TG_RGB library.
W/ ROTATION!!!!!!
This is a derivative of the dadfruit-circuitpython-rgb library 
* Author(s): Radomir Dopieralski, Michael McWethy, Jonah Yolles-Murphy
"""

__version__ = "1.0"

from TG_Modules.TG_RGB.rgb import DisplaySPI
try:
    import struct
except ImportError:
    import ustruct as struct
from micropython import const

__version__ = "0.1"
__repo__ = "https://github.com/TG-Techie/TG-RGB"

_NOP = const(0x00)
_SWRESET = const(0x01)
_RDDID = const(0x04)
_RDDST = const(0x09)

_SLPIN = const(0x10)
_SLPOUT = const(0x11)
_PTLON = const(0x12)
_NORON = const(0x13)

_INVOFF = const(0x20)
_INVON = const(0x21)
_DISPOFF = const(0x28)
_DISPON = const(0x29)
_CASET = const(0x2A)
_RASET = const(0x2B)
_RAMWR = const(0x2C)
_RAMRD = const(0x2E)

_PTLAR = const(0x30)
_COLMOD = const(0x3A)
_MADCTL = const(0x36)

_FRMCTR1 = const(0xB1)
_FRMCTR2 = const(0xB2)
_FRMCTR3 = const(0xB3)
_INVCTR = const(0xB4)
_DISSET5 = const(0xB6)

_PWCTR1 = const(0xC0)
_PWCTR2 = const(0xC1)
_PWCTR3 = const(0xC2)
_PWCTR4 = const(0xC3)
_PWCTR5 = const(0xC4)
_VMCTR1 = const(0xC5)

_RDID1 = const(0xDA)
_RDID2 = const(0xDB)
_RDID3 = const(0xDC)
_RDID4 = const(0xDD)

_PWCTR6 = const(0xFC)

_GMCTRP1 = const(0xE0)
_GMCTRN1 = const(0xE1)

class ST7735R(DisplaySPI):
    """A simple driver for the ST7735R-based displays."""
    _COLUMN_SET = _CASET
    _PAGE_SET = _RASET
    _RAM_WRITE = _RAMWR
    _RAM_READ = _RAMRD
    _INIT = (
        (_SWRESET, None),
        (_SLPOUT, None),

        (_MADCTL, b'\xc8'),
        (_COLMOD, b'\x05'),  # 16bit color
        (_INVCTR, b'\x07'),

        (_FRMCTR1, b'\x01\x2c\x2d'),
        (_FRMCTR2, b'\x01\x2c\x2d'),
        (_FRMCTR3, b'\x01\x2c\x2d\x01\x2c\x2d'),

        (_PWCTR1, b'\x02\x02\x84'),
        (_PWCTR2, b'\xc5'),
        (_PWCTR3, b'\x0a\x00'),
        (_PWCTR4, b'\x8a\x2a'),
        (_PWCTR5, b'\x8a\xee'),

        (_VMCTR1, b'\x0e'),
        (_INVOFF, None),

        (_GMCTRP1, b'\x02\x1c\x07\x12\x37\x32\x29\x2d'
                   b'\x29\x25\x2B\x39\x00\x01\x03\x10'), # Gamma
        (_GMCTRN1, b'\x03\x1d\x07\x06\x2E\x2C\x29\x2D'
                   b'\x2E\x2E\x37\x3F\x00\x00\x02\x10'),
    )
    _ENCODE_PIXEL = ">H"
    _ENCODE_POS = ">HH"


    #pylint: disable-msg=useless-super-delegation, too-many-arguments
    def __init__(self, spi, dc, cs, rst=None, hardware_width=160, hardware_height=160, rotation = 0):
        self.rotation = rotation
        if (rotation == 1) or (rotation == 3):
            self.width = 160
            self.height = 128
        else:
            self.width = 128
            self.height = 160
        super().__init__(spi, dc, cs, rst, hardware_width, hardware_height,baudrate=1000000000,)

    def init(self):
        super().reset()
        super().init()
        cols = struct.pack('>HH', 0, self.hardware_width - 1)
        rows = struct.pack('>HH', 0, self.hardware_height - 1)
        rot_num=bytearray(1)
        try:
            rot_num[0]= (0b11001000,0b10101000,0b00001000,0b01101000)[self.rotation]
        except IndexError:
            rot_num[0]=0b11001000
        #data[0]=0b10101000 is normal
        for command, data in (
                (_CASET, cols),
                (_RASET, rows),
                (_NORON, None),
                (_DISPON, None),
                #(_MADCTL, self.rotation),
                (_MADCTL, rot_num),
        ):
            self.write(command, data)
        #data=bytearray(1)
        #data[0]=0b10101000
        #self.write(_MADCTL,data)
            
        
        

        
