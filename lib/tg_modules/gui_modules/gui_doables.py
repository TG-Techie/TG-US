from tg_modules.gui_modules.gui_base import refreshable, io, behave

class operator(refreshable):
    
    def __init__(self, func, tup):
        self._set_id()
        
        self.func = func
        self.tup = tup
        
    
    def place(self):
        pass
    
    def clear(self):
        pass
    
    def refresh(self):
        self.func(*self.tup)
        