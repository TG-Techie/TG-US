#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/15/18


from tg_modules.gui_modules.gui_base import valued,io
from tg_modules.gui_modules import __behavior as behave
from math import floor

class rect(valued):
    
    def __init__(self,x,y,width,height,color, radius = 0, place = behave.should_place, color_clear = io.background_color):
        self._set_id()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.color_clear = color_clear
        
        #set initial value as color
        self._value = color
        
        self.active = 0
        
        self.radius = radius
        
        if place:
            self.place()
    
    def place(self):
        self.active = 1
        io.if_rect(self.x, self.y, self.width, self.height, self.radius,self.value)
    
    def clear(self):
        self.active = 0
        io.if_rect(self.x, self.y, self.width, self.height, self.radius,self.color_clear)
        
    @property
    def color(self):
        return self._value
        
    @color.setter
    def color(self,new_val):
        if new_val != self._value:
            #self.clear() #SHOULD HAVE THIS??
            self._value = new_val
            if self.active:
                self.place()

class text(valued):
    
    def __init__(self,x,y,width,height, value , color = io.white, size = 1, border = 0, place = behave.should_place,
                top_down = 1, clip_top = 1, color_clear = io.background_color, background = io.black):
        self._set_id()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.color_clear = color_clear
        self.background = background
        
        self.size = size
        self.border = border
        
        self.active = 0
        
        self.top_down = top_down
        self.clip_top = clip_top
        
        #errors
        #dims = io.text_dimensions(0,0,'   /n   ', size)
        dims = (5*3*self.size + self.size*3 ,7*2*self.size + self.size*2)# temp error fix
        self.char_width = int(dims[0]/3)
        self.char_height = int(dims[1]/2)
        #print(self.char_width, self.char_height)
        
        #set initial value as color
        self._value = ' '
        self._color = color
        
        #define possbile cols and chars of text
        self._textx = self.x + self.border
        self._texty = self.y + self.border
        
        self._text_cols = floor((self.width - self.border*2 - 1)/self.char_width)
        self._text_rows = floor((self.height - self.border*2 -1 )/self.char_height) -1
        #print(self._text_cols)
        
        # configureing value
        self.value = value
        '''# this defines internal vars like text len, height etc
        self.value = value'''
        
        if place:
            self.place()
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,valin):
        valin = str(valin)
        if valin != self._value:

            valin = valin.split('\n')

            if not self.top_down:
                valin = valin[-1::]
            
            valin = valin[0:self._text_rows + 1]
            
            # break into lines by enter and add as list components 
            nextval = []
            for line in valin:
                #valin.index(line)
                #print(line)
                nextval.append(line[0:self._text_cols])
            #print(nextval)
            
            valout = ''
            for line in nextval:
                valout += '\n' + line 
            
            self._value = valout[1::]
            
            if self.active:
                self.sub_place()
    
    @property
    def color(self):
        return self._color
        
    @color.setter
    def color(self,new_val):
        if new_val != self._color:
            #self.clear() #SHOULD HAVE THIS??
            self._color = new_val
            if self.active:
                self.sub_place()
    
    def clear(self):
        self.active = 0
        
        io.rect(self.x,self.y,self.width, self.height, self.color_clear)
    
    def place(self):
        self.active = 1
        
        #print(self.char_width,self.char_height, self._text_cols,self._text_rows)
        if self.border:
            io.rect(self.x,self.y,self.width,self.height, self._color)
        
        io.rect(self.x + self.border,self.y + self.border,
                self.width - self.border*2, self.height - self.border*2, self.background)
        
        self.sub_place()
        
    def sub_place(self):
        #width = io.text_dimensions(self.x+self.border,self.y+self.border,self.value)
        #io.rect(self.x+self.border + width,self.y+self.border, self.width - width, self.height)
        
        #place  rect to clear any place where new text won't go
        minx = self.width
        for line in self.value.split('\n'):
            minx = min(minx, io.text_dimensions(self.x,self.y,line)[0] )
        
        io.rect(self.x+self.border + minx, self.y+self.border, 
                self.width - self.border*2 - minx,
                self.height - self.border*2,
                self.background)
    
        io.text(self.x + self.border,self.y + 1 + self.border, self.value, color = self.color,
                background = self.background)

#def cmd_box():
    