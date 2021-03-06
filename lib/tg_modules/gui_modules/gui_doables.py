#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/26/18

from tg_modules.gui_modules.gui_base import refreshable, io, behave

class on_refresh(refreshable):
    
    def __init__(self, func, tup):
        self._set_id()
        
        self.func = func
        self.tup = tup
        
        self.active = 0
        
    
    def place(self):
        self.active = 1
        pass
    
    def clear(self):
        self.active = 0
        pass
    
    def refresh(self):
        if self.active:
            #print(1)
            #print(self.tup)
            #sprint(2)
            #print(type(self.tup))
            self.func(*self.tup)

class on_place(refreshable):
    
    def __init__(self, func, tup, clear_func, clear_tup):
        self._set_id()
        
        self.func = func
        self.tup = tup
        self.clear_func = clear_func
        self.clear_tup = clear_tup
        
        self.active = 0
        
    
    def place(self):
        self.active = 1
        self.func(*self.tup)
    
    def clear(self):
        self.active = 0
        self.clear_func(*self.clear_tup)
        