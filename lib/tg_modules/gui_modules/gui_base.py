#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

from tg_io import io_screen as io
from time import monotonic


_last_id = 0

class gui_obj():
    is_gui_obj = True
    
    def _set_id(self):
        global _last_id
        _last_id += 1
        self._gui_id = _last_id 
        #print(self._id)
    
    def __init__(self,x,y,width,height, place = 1, color_clear = io.background_color):
        self._set_id() # YOU MUST DO THIS
        #save them to class instance 
        self.active = 0
        
        if place:
            self.place()
            
        pass
    
    #put the item on the screen
    def place(self):
        self.active =1
        raise NotImplementedError('TG: place method not implemented for:'+str(type(self)))
    
    #cover the item with the "color_clear"
    def clear(self):
        self.active = 0
        raise NotImplementedError('TG: clear method not implemented for:'+str(type(self)))
    
class valued(gui_obj):
    has_value = True
    is_selectable = False
    is_navigable = False
    is_refreshable = False
    
    
    def __init__(self,x,y,width,height,value, place = 1, color_clear = io.background_color):
        self._set_id() # YOU MUST DO THIS
        self._value = value
        #save rest to the class instance as the same name
        self.active = 0
        pass
    
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self,new_val):
        if new_val != self._value:
            #self.clear() #SHOULD HAVE THIS??
            self._value = new_val
            if self.active:
                self.place()
        

class selectable(gui_obj):
    has_value =  False
    is_selectable = True
    is_navigable = False
    is_refreshable = False
    
    def __init__(self,x,y,width,height,purpose_func = None,purpose_tup = (), place = 1, 
                color_clear = io.background_color):
        self._set_id() # YOU MUST DO THIS
        
        if purpose_func: # boolean logic checker
            self.purpose_func = purpose_func
            self.purpose_tup = purpose_tup
        else:
            self.purpose_func = 'you_put_function_here' 
            #!!!!!!#put default func ^^^^^^^
            self.purpose_tup = (self,) 
        
        #save rest to the class instance as the same name
        
        #selectable states
        self.selected = 0
        self.active = 0
        
        if place:
            self.place()
        
    def set_purpose(self, func, tup):
        self.purpose_func = func
        self.purpose_tup = tup
    
    def place(self):
        self.active = 1
        #check selected state and and place accordingly
        raise NotImplementedError('TG: place method not implemented for:'+str(type(self)))

        
    def clear(self):
        self.active = 0
        #cover with self.color_clear
        raise NotImplementedError('TG: clear method not implemented for:'+str(type(self)))
    
    def select(self):#, place = 1):
        if self.active:
            self.clear()
            self.selected = 1
            self.place()
            return
        self.selected = 1
    
    def deselect(self, place = 1):
        if self.active:
            self.clear()
            self.selected = 0
            self.place()
            return
        self.selected = 0
    
    def press(self):
        if self.active and self.selected:
            self.purpose_func(*self.purpose_tup)
    

class navigable(gui_obj):
    has_value = False
    is_selectable = False
    is_navigable = True
    is_refreshable = False
    
    
    
    def __init__(self,x,y,width,height, move_mode = (1,1), superior = None, place = 1, 
                    color_clear = io.background_color):
        self._set_id() # YOU MUST DO THIS
        #save them to class instance  except MAKE SUPERIOR AN EMPTY NAVIGABLE
        #move mode toggles allowed movement axisis
        self.active = 0
        
        if place:
            self.place()
        pass
    
    def move(self, dir_1, dir_2 = None):
        #check move mode
        #take the dirs and move acordingly, not not all systemns have up and down
        # call superior.move with a try and except if you want to switch panels 
        raise NotImplementedError('TG: move method not implemented for:'+str(type(self)))
    
    def switch(self, coord_1, coord_2 = None):
        #instead of moving switch directly to the coords
        raise NotImplementedError('TG: switch method not implemented for:'+str(type(self)))
    
    
    #optional
    def press(self):
        # execute the currently selected thing that has been navigated to
        raise NotImplementedError('TG: switch method not implemented for:'+str(type(self)))



'''class refreshable(gui_obj):
    has_value = False
    is_selectable = False
    is_navigable = False
    is_refreshable = True
    
    def __init__(self,x,y,width,height, data_fetch_func, data_fetch_tup, place = 1, clear_color = io.background_color):
        self._set_id() # YOU MUST DO THIS
        #save inputs to class instance 
        self.active = 0
        if place:
            self.place()
        pass'''