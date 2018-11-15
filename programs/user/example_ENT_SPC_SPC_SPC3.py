#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/15/18

from system.programs.__blank__app import init
exec(init)
wants_refresh = False #tell teh system not to refresh the app, making it only event based

value_for_bar = 0

def get_val():
    global value_for_bar
    #for inti debug#return int(input('val:'))
    print(value_for_bar)
    return value_for_bar

def incre_bar_val(target, valin):
    global value_for_bar
    value_for_bar = (value_for_bar + valin) % 105####HEY! note it is treaded with modulo
    target.refresh()

def set_bar_val(target, valin):
    global value_for_bar
    value_for_bar = valin % 110####HEY! note it is treaded with modulo
    target.refresh()
    
page = container.add_panel()

page.add(label = gui.text(cont_x, cont_y, cont_width, cont_height, 'value_bar Example:'))

page.add(my_bar = gui.value_bar(cont_x + 5, int(cont_height/3), cont_width - 10, 20,get_val, (),
            radius = 7, border = 2))



page.add( setter = gui.nidos(cont_x, cont_y -30 + cont_height, cont_width, 30, 6, 1))

page.setter.of(0,0).set_purpose(incre_bar_val,(page.my_bar,5,))
page.setter.of(0,0).text = '+'

page.setter.of(1,0).set_purpose(incre_bar_val,(page.my_bar,-5,))
page.setter.of(1,0).text = '-'

for i in range(4):
    cur_but = page.setter.contents[i+2]
    cur_num = int(i*33.3333)
    cur_but.text = str(cur_num)
    cur_but.set_purpose(set_bar_val, (page.my_bar,cur_num))