from tg_modules.gui_modules.gui_base import refreshable, io, behave

class grid_display(refreshable):
    def __init__(self, x, y, width, height, data_func, data_tup, border = 0, place =  behave.should_place,
                    color_clear = io.background_color, background = io.standard_color):
        
        #physical params
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        
        #stuff
        self.data_func = data_func
        self.data_tup = data_tup
        
        #color
        self.color_clear = color_clear
        self.background = background
        
        # sample for dims
        data = self.data_func(*self.data_tup)
        
        #num pixels in x,y
        self.grid_width = len(data)
        self.grid_height = len(data[0])
        
        #num width of one pixel
        self.pixel_width = int((self.width - self.border*2) / self.grid_width)
        self.pixel_width = int((self.height - self.border*2) / self.grid_height)
        
        # exact position of grid 00 start
        self.grid_x = int((self.width - self.pixel_width*self.grid_width)/2) + self.width
        self.grid_y = int((self.height - self.pixel_height *self.grid_height)/2) + self.height
        
        #comparative
        self.prev = [[0]*grid_height]*grid_width
        
        self.active = 0
        
        if place:
            self.place()
    
    def place(self):
        self.active = 1
        io.rect(self.x, self.y, self.width, self.height, self.background)
        self.refresh()
        
    def refresh(self):
        if self.active:
            data = self.data_func(*self.data_tup)
            
            x_pos = self.grid_x
            for x in range(self.grid_width):
                y_pos = self.grid_y
                for y in range(self.grid_height):
                    pass