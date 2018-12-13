#a scrolling text demo for the tg_gui

#setup framework
from system.programs.__blank__app import init
exec(init)
#print(init)
wants_refresh = True

#when called move the target text over one
#text must be the peice of the string you are trying to move
def move_right(target, text):
    target.value = ' '+target.value
    if len(target.value.replace(' ','')) == 0:
        target.value = text



my_page = container.add_panel()



my_page.add(my_text = gui.text(cont_x,  cont_height - 20, cont_width,  20, 'I should not be scrolling'))


my_page.add(my_s_text = gui.scrolling_text(cont_x,  cont_height - 40, cont_width,  20 ,'I should be scrolling',direction  = -1, delay = 10))

my_page.add(my_s_text = gui.scrolling_text(cont_x,  cont_height - 60, cont_width,  20 ,'And I forwards',direction  = 1, delay = 10))