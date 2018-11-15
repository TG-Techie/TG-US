#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/15/18

from system.programs.__blank__app import init
exec(init)
wants_refresh = False #tell teh system not to refresh the app, making it only event based

def empty_func():
    return 0

def incre_bar_val(target, valin):
    target.value = (target.value + valin) % 110
    

page = container.add_panel()

page.add(label = gui.text(cont_x, cont_y, cont_width, cont_height, 'value_bar Example:'))

page.add(my_bar = gui.value_bar(cont_x + 5, int(cont_height/3), cont_width - 10, 20,empty_func, (),
            radius = 5, border = 2))

page.add( val_setter = gui.nidos(cont_x, cont_height - 30, cont_width, 30, 6, 1))