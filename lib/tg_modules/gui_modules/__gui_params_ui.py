from tg_modules.gui_modules.gui_navigation import button, nidos, io, behave

class list(nidos):
    
    def __init__(self,x,y,width,height,rows,radius = 0, move_mode = (1,1), superior = navigable(0,0,0,0,place = 0),
                    x_gap = 3, y_gap = 3,
                    place = behave.should_place, select = 1,
                    color_clear = io.background_color,
                    background = io.background_color,
                     button_color = io.button_color_norm,
                     button_color_sel = io.button_color_sel,
                     button_text_color = io.text_color_norm,
                     button_text_color_sel = io.text_color_sel):
        self._set_id()
        