#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/14/18

from tg_modules.gui_modules.gui_valued import grid_display, behave, io

class thermal_display(grid_display):
    '''units: none = 0, c=1, f=2, k=3'''
    def __init__(self, x, y, width, height, data_func, data_tup, units_in = 1, units_out = 2, border = 0, memory_tol = 1, color_mask = (1,0,0),place =  behave.should_place,
                    color_clear = io.background_color, background = io.standard_color):
                        
        super().__init__(x, y, width, height, data_func, data_tup, border, memory_tol, color_mask, place,
                    color_clear, background = io.standard_color)
    
        self.units_in = units_in
        self.units_out = units_out
    
    def _c2f(self,val):
        #print('moop')
        return (val*9/5) +32
    
    def _f2c(self,val):
        return (val-32)*5/9
        
    def _c2k(self, val):
        return val + 273
        
    def _k2c(self, val):
        return val - 273
        
    def refresh(self):
        data = super().refresh()
        
        maxin = data[0]
        minin = data[1]
        
        #print(self.units_in, self.units_out)
        if self.units_in != self.units_out:
            #print(maxin,minin)
            if self.units_in >= 2:
                maxin = (self._f2c,self._k2c)[self.units_in-2](maxin)
                minin = (self._f2c,self._k2c)[self.units_in-2](minin)
            #print(maxin,minin)
            if self.units_out >= 2:
                maxin = (self._c2f,self._c2k)[self.units_out-2](maxin)
                minin = (self._c2f,self._c2k)[self.units_out-2](minin)
            #print(maxin,minin)   
        
            
        
        line0 = 'Max: '+str(int(maxin)) + ('','C__degreesign__','F__degreesign__','K')[self.units_out] + '  '
        line1 = 'Min: '+str(int(minin)) + ('','C__degreesign__','F__degreesign__','K')[self.units_out] + '  '
        
        io.text(self.x, self.height + self.y,line0)
        io.text(self.x, 1+ self.height + self.y + io.text_dimensions(self.x, self.height + self.y,line0)[1],line1)