# The MIT License (MIT)
# -Copyright (c) 2017 Radomir Dopieralski and Adafruit Industries
# -Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#- The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""`TG-Modules.TG-RGB.rgb`
Base class for all RGB Display devices W/ TEXT!!!!!
This is a derivative of the dadfruit-circuitpython-rgb library 
Author(s):Radomir Dopieralski, Michael McWethy, and Jonah Yolles-Murphy"""
import time
from math import sqrt
from micropython import const
import struct  # import ustruct as struct
import adafruit_bus_device.spi_device as spi_device

from gc import collect as clean_mem



__version__ = "1.0"
__repo__ = "https://github.com/TG-Techie/TG-RGB"

# This is the size of the buffer to be used for fill operations, in 16-bit
# units. We use 256, which is 512 bytes — size of the DMA buffer on SAMD21.
_BUFFER_SIZE = const(256)

#def color565(r, g, b):
#    """ This converts red, green, blue (0-255) into 16-bit 565 values. this is
#        here to amke coding in colors easier"""
#    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3

def colorst(r, g, b):
    #same input as color565 but calculated like bgr
    #    this is for the st7735r display
    return (b & 0xf8) << 8 | (g & 0xfc) << 3 | r >> 3

color_white = colorst(255,255,255)
color_black = 0

class DummyPin:
    #"""Can be used in place of a ``Pin()`` when you don't want to skip it."""
    def init(self, *args, **kwargs):
        pass #Dummy Pin init

    def low(self):
        pass #Dummy low Pin method
        
    def high(self):
        pass #Dummy high Pin method
        
class Display: #pylint: disable-msg=no-member
    #"""Base class for all RGB display devices
    #        :param hardware_width: number of pixels wide
    #        :param hardware_height: number of pixels high"""
    _PAGE_SET = None
    _COLUMN_SET = None
    _RAM_WRITE = None
    _RAM_READ = None
    _INIT = ()
    _ENCODE_PIXEL = ">H"
    _ENCODE_POS = ">HH"
    _DECODE_PIXEL = ">BBB"

    def __init__(self, hardware_width, hardware_height, font = None, x_offset = 0, y_offset = 0):
        #hardware_width and height are for to the dram buffer size
        self.hardware_width = hardware_width 
        self.hardware_height = hardware_height 
        if font == None:
            from TG_Modules.TG_Fonts.font_01 import text_dict
        self.text_dict = text_dict
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.color_depth = 2
        self.init()
        self.rect(-x_offset, -y_offset, hardware_width, hardware_height, 0)

    def init(self):
        #"""Run the initialization commands."""
        for command, data in self._INIT:
            self.write(command, data)

    #pylint: disable-msg=invalid-name,too-many-arguments
    def _block(self, x0, y0, x1, y1, data=None):
        """Read or write a block of data."""
        self.write(self._COLUMN_SET, self._encode_pos(x0, x1))
        self.write(self._PAGE_SET, self._encode_pos(y0, y1))
        if data is None:
            size = struct.calcsize(self._DECODE_PIXEL)
            return self.read(self._RAM_READ,
                             (x1 - x0 + 1) * (y1 - y0 + 1) * size)
        self.write(self._RAM_WRITE, data)
        del x0, y0, x1, y1, data
        clean_mem()
        return None
    #pylint: enable-msg=invalid-name,too-many-arguments

    def _encode_pos(self, x, y):
        """Encode a postion into bytes."""
        return struct.pack(self._ENCODE_POS, x, y)
        del x,y
        clean_mem()

    def _encode_pixel(self, color):
        """Encode a pixel color into bytes."""
        return struct.pack(self._ENCODE_PIXEL, color)
        del color

    def _decode_pixel(self, data):
        """Decode bytes into a pixel color."""
        return colorst(*struct.unpack(self._DECODE_PIXEL, data))
        del data
        clean_mem()

    def pixel(self, x, y, color=None):
        x += self.x_offset 
        y += self.y_offset
        """Read or write a pixel at a given position."""
        if color is None:
            return self._decode_pixel(self._block(x, y, x, y))

        if 0 <= x < self.hardware_width and 0 <= y < self.hardware_height:
            self._block(x, y, x, y, self._encode_pixel(color))
        return None
        del x,y,color
        clean_mem()

    #pylint: disable-msg=too-many-arguments
    def rect(self, x, y, width, height, color):
        x += self.x_offset 
        y += self.y_offset
        x = min(self.hardware_width - 1, max(0, x))
        y = min(self.hardware_height - 1, max(0, y))
        hardware_width = min(self.hardware_width - x, max(1, width))
        hardware_height = min(self.hardware_height - y, max(1, height))
        self._block(x, y, x + width - 1, y + height - 1, b'')
        chunks, rest = divmod(width * height, _BUFFER_SIZE)
        pixel = self._encode_pixel(color)
        if chunks:
            data = pixel * _BUFFER_SIZE
            for _ in range(chunks):
                self.write(None, data)
        self.write(None, pixel * rest)
    #pylint: enable-msg=too-many-arguments

    def fill(self, color=0):
        #"""Fill the whole display with the specified color."""
        self.rect(0, 0, self.hardware_width, self.hardware_height, color)
        del color
        clean_mem()

    def hline(self, x, y, width, color):
        #"""Draw a horizontal line."""
        self.rect(x, y, width, 1, color)


    def vline(self, x, y, height, color):
        #"""Draw a vertical line."""
        self.rect(x, y, 1, height, color)

    def text_dimension(self,xin,yin,text,size = 1):
        xin += self.x_offset 
        yin += self.y_offset
        max_width = 0
        cur_width = 0
        line_count = 1
        text = (text.upper()).split('__')
        while len(text):
            try:
                cur_width += 1
                cur_width += len(self.text_dict['__'+text[0]+'__'])
            except KeyError:
                while len(text[0]): # for each section
                    #--------------------------------------------------------
                        #check for enter character
                        if (text[0][0] == '''
'''): # this is the enter character
                            line_count += 1 
                            if cur_width > max_width:
                                max_width = cur_width
                                cur_width = 0
                            if (len(text) == True):
                                text[0] = text[0][1:]
                            continue
                    #--------------------------------------------------------
                        # check if the text will spill over the side of the display
                        try:
                            next_x_end = (cur_width*size + xin -1 +
                                          len(self.text_dict[(text[0][0]).upper()]))
                            if (next_x_end > self.width):
                                if (len(text) == True):
                                    del next_x_end
                                    line_count += 1
                                    if cur_width > max_width:
                                        max_width = cur_width
                                        cur_width = 0 
                                continue
                        except KeyError:
                           pass
                    #--------------------------------------------------------
                        #make the comp_list additions
                        cur_width += 1
                        try:
                            cur_width += len(self.text_dict[text[0][0]])
                        except KeyError:
                            cur_width += len(self.text_dict["__?__"])
                        text[0] = text[0][1:]
                    #--------------------------------------------------------
            if len(text):
                text.pop(0)
            if cur_width > max_width:
                max_width = cur_width
            return (max_width*size,line_count*self.text_dict['Height']*size)


                
    
    def _byte_coord(self, grid_width, x,y):
        return self.color_depth*(grid_width*y + x)

    def text(self,xin,yin,text,color = color_white, background = color_black, size = 1, rect_extension = 0, italics = 0):
        xin += self.x_offset 
        yin += self.y_offset
        comp_list = []
        enter_stat = False
        if type(text) != list:
            text = (text.upper()).split('__')
        while len(text):
            try:
                comp_list.append(0)
                comp_list += self.text_dict['__'+text[0]+'__']
            except KeyError:
                while len(text[0]): # for each section
                    #--------------------------------------------------------
                        #check for enter character
                        if (text[0][0] == '''
'''): # this is the enter character
                            enter_stat = True
                            if (len(text) == True):
                                text[0] = text[0][1:]
                                next_text = text.copy() #make next_text the rest of the text (list form)
                            break
                    #--------------------------------------------------------
                        # check if the text will spill over the side of the display
                        try:
                            next_x_end = (len(comp_list)*size + xin -1 +
                                          len(self.text_dict[(text[0][0]).upper()]))
                            if (next_x_end > self.width):
                                if (len(text) == True):
                                    del next_x_end
                                    next_text = text.copy() #make next_text the rest of the text (list form)
                                break
                        except KeyError:
                           pass
                    #--------------------------------------------------------
                        #make the comp_list additions
                        comp_list.append(0)
                        try:
                            comp_list += self.text_dict[text[0][0]]
                        except KeyError:
                            comp_list += self.text_dict["__?__"]
                        text[0] = text[0][1:]
                    #--------------------------------------------------------
            if len(text):
                text.pop(0)
        clean_mem()
        width = len(comp_list)
        height = self.text_dict['Height']
        
        global array
        array = bytearray(width * height  *self.color_depth )# 2 if for color depth
        for x_pos in range(width): #cycle through stripes
            for y_pos in (range(height)): # cycle through bits in stripes
                        #calc 1st bit position
                        pos = self._byte_coord(width, x_pos , y_pos)
                        #figureout witch color
                        if (comp_list[x_pos] & 2**(height-y_pos-1)):
                            cur_color = color
                        else:# elif background:
                            cur_color = background
                        #change array
                        for byte_offset in (range(self.color_depth)):
                            array[pos+self.color_depth-1-byte_offset] = ((cur_color) >> byte_offset*8) & 255 #(0b11111111)
        #put background around
        self.rect(xin , yin, width +1, height +1 + rect_extension, background)
        #print(width, height)
        if size > 1:
            array_out = bytearray(0)
            for y_pos in range(height*2):# for row in array
                for i in range(size): # add multiple lines
                    row_array = bytearray(0)
                    for x_pos in range(int(width)):# for pixel in row
                        pos0 = width*2*y_pos + x_pos*2
                        #print(pos0)
                        array_out += array[pos0 : pos0+2]*size
                    array_out += row_array*size
                
        else:
            array_out = array
            
        self._block(xin , yin+1 , xin-1+ width*size +italics, yin-1+ height*size +1, array_out)
        try:
            self.text(xin - self.x_offset ,yin - self.y_offset +1+rect_extension+7*size,next_text,
                                      color = color,
                                      background = background, size = size,
                                      rect_extension = rect_extension,
                                      italics = italics)
        except NameError:
            pass
        del xin,yin,comp_list, enter_stat, text, next_x_end, next_text, width, height, array, array_out,x_pos, y_pos, pos, pos0
        clean_mem()
            

    def scroll(self,x,y,str, color = colorst(255,255,255), background = None, size = 1):
        comp_list = []
        for section in (str.upper()).split('__'):
            try:
                comp_list.append(0)
                comp_list += self.text_dict['__'+section+'__']
            except KeyError:
                for char in section:
                    comp_list.append(0)
                    try:
                        comp_list += self.text_dict[char]
                    except KeyError:
                        comp_list += self.text_dict["__?__"]
            #comp_list += self.text_dict[" "]
        #print(comp_list) # debug concated list
        x_pos = 0
        y_pos = 0
        for stripe in comp_list[1:]:
            y_pos = size
            if background != None:
                self.rect(x+x_pos,y-1+y_pos,size,
                              self.text_dict['Height']*size +1,background)
            #stripe_text = bin(stripe)[3:10]
            #print(stripe_text) # print out bits being striped
            for j in reversed(range(7)): 
                if (stripe & 2**j):
                    self.rect(x+x_pos,y+y_pos,size,size,color)
                y_pos += size
            x_pos += size
        del x,y,str,size,color, comp_list, x_pos, y_pos
        clean_mem()

    def round_rect(self,x,y,width,height,r,color):
        #calc gaps
        gap_list = ()
        for j in range(r):
            gap_list += ((int(r + .5 -sqrt(  (r**2) - ((r-j*.85)**2)  ))),)
        #stripe top
        for j in range(r):
            self.hline(x+gap_list[j],y+j,width - 2*gap_list[j],color)
        #place mid rect chunk
        self.rect(x,y+r,width,height-2*r,color)
        #place mid rect
        for j in reversed(range(r)):
            self.hline(x+gap_list[j],y+height-j-1,width - 2*gap_list[j],color)
        del gap_list
        #clean_mem()

class DisplaySPI(Display):
    #"""Base class for SPI type devices"""
    #pylint: disable-msg=too-many-arguments
    def __init__(self, spi, dc, cs, rst=None, hardware_width=1, hardware_height=1, baudrate=12000000, polarity=0, phase=0, x_offset = 0, y_offset = 0):
        
        #spi device
        self.spi_device = spi_device.SPIDevice(spi, cs, baudrate=baudrate,
                                               polarity=polarity, phase=phase)
        self.dc_pin = dc
        self.rst = rst
        self.dc_pin.switch_to_output(value=0)
        if self.rst:
            self.rst.switch_to_output(value=0)
            self.reset()
        
        #disp device
        super().__init__(hardware_width, hardware_height, x_offset = x_offset, y_offset = y_offset)
    #pylint: enable-msg=too-many-arguments

    def reset(self):
        #"""Reset the device"""
        self.rst.value = 0
        time.sleep(0.050)  # 50 milliseconds
        self.rst.value = 1
        time.sleep(0.10)  # 50 milliseconds

    def write(self, command=None, data=None):
        #"""SPI write to the device: commands and data"""
        if command is not None:
            self.dc_pin.value = 0
            with self.spi_device as spi:
                spi.write(bytearray([command]))
        if data is not None:
            self.dc_pin.value = 1
            with self.spi_device as spi:
                spi.write(data)

    def read(self, command=None, count=0):
        #"""SPI read from device with optional command"""
        data = bytearray(count)
        self.dc_pin.value = 0
        with self.spi_device as spi:
            if command is not None:
                spi.write(bytearray([command]))
            if count:
                spi.readinto(data)
        return data