#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/05/18

from tg_modules.gui_modules.gui_base import refreshable, io, behave
import time
from math import floor
from gc import collect

class grid_display(refreshable):
    def __init__(self, x, y, width, height, data_func, data_tup, border = 0, memory_tol = 1, color_mask = (1,0,0),place =  behave.should_place,
                    color_clear = io.background_color, background = io.standard_color):
        self._set_id()
        
        #physical params
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        
        #stuff to get data
        self.data_func = data_func
        self.data_tup = data_tup
        
        #color
        self.color_mask = (not color_mask[0],not color_mask[1],not color_mask[2])
        self.color_clear = color_clear
        self.background = background
        
        # sample for dims
        data = self.data_func(*self.data_tup)
        
        #num pixels in x,y
        self.grid_width = len(data)
        self.grid_height = len(data[0])
        
        #num width of one pixel
        self.pixel_width = int((self.width - self.border*2) / self.grid_width)
        self.pixel_height = int((self.height - self.border*2) / self.grid_height)
        
        # exact position of grid 00 start
        self.grid_x = int((self.width - self.pixel_width*self.grid_width)/2) + self.width
        self.grid_y = int((self.height - self.pixel_height *self.grid_height)/2) + self.height
        
        self.active = 0
        
        #comparative
        #the previos loaded data grid
        self.prev = []
        for valx in range(self.grid_width):
            self.prev.append([])
            for valy in range(self.grid_height):
                self.prev[valx].append(2**31)
        #the difference in tep required for screen change
        self.memory_tol = memory_tol
        
        if place:
            self.place()
    
    def place(self):
        self.active = 1
        io.rect(self.x, self.y, self.width, self.height, self.background)
        self.refresh()
        
    def refresh(self):
        if self.active:
            data = self.data_func(*self.data_tup)
            
            #find max and min
            max_val = -100000 #init 
            min_val = 100000 # crazy
            for row in data:
                for val in row:
                    max_val = max(max_val, val)
                    min_val = min(min_val, val)
            color_range = max_val - min_val +1
            
            x_pos = self.grid_x
            for x in range(self.grid_width):
                y_pos = self.grid_y
                for y in range(self.grid_height):
                    #check if screen needs refresh! (only chagne prev if screen is to be writen to!)
                    if abs(data[x][y] - self.prev[x][y]) >= self.memory_tol/2:
                        #change the previous stored value
                        self.prev[x][y] = data[x][y]
                        
                        color_val = max(0, int(floor(((data[x][y] - min_val)**3/color_range**3)*10) * 255/10) - int( color_range**2/ (data[x][y]*1.01 - min_val )**3))
                        
                        io.rect(self.x + self.border + x*self.pixel_width,
                                self.y + self.border + y*self.pixel_width,
                                self.pixel_width, self.pixel_height, io.color(255-color_val*self.color_mask[0],#r
                                                                                255-color_val*self.color_mask[1],#g
                                                                                255-color_val*self.color_mask[2]))#b
            
            del data, x_pos, y_pos
            collect()
            return(max_val, min_val, color_range)
                        
                        

class thermal_display(grid_display):
    def __init__(self, x, y, width, height, data_func, data_tup, border = 0, memory_tol = 1, color_mask = (1,0,0),place =  behave.should_place,
                    color_clear = io.background_color, background = io.standard_color):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        