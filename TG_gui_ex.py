
#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18


from tg_modules import tg_gui as gui
#print('gui modules loaded: ', gui.modules)
import time, sys

gui.io.fill(gui.io.blue)

win = gui.window(5,5,150,118, move_loop = True)
page1 = win.add_panel()
page2 = win.add_panel() 
repl = win.add_panel(should_index = False)

page1.add(label = gui.text(5,5,150,15,'Page:1\ncan you see this?', place = False, border = 2))
page2.add(label = gui.text(5,5,150,15,'Page:2\ncan you see this?', place = False, border = 2))

page1.add(menu = gui.nidos(5,20,150,103,3,4,3, place = False, select = True, move_mode = (1,0), superior = win))
page2.add(menu = gui.nidos(5,20,150,103,3,4,3, place = False, select = True, move_mode = (1,0), superior = win ))

page1.menu.of(0,0).text = 'page1\nmenu'
page2.menu.of(0,0).text = 'page2\nmenu'

repl.add(text_box = gui.text(5,5,150,118,'>>>', place = False, border = 2))

win.place()

win.switch(repl)

"""####################################################################
#reple example
#########################
win.switch(2)
print(repl.text_box.text_rows)
while 1:
    repl.text_box.value =  repl.text_box.value + str(input('next line?:')) +'\n>>>'""" 



##############################################################
#page commadn examples
##############################
w = '^'
s = 'V'
a = '<'
d = '>'
e = 'E'
while 1:
    cmd = (input('your command:'))
    
    if  cmd == 'X':
        break
        
    if not len(cmd):
        print('invalid input: just enter?')
        continue
    
    cmd = cmd[0]
    
    if cmd == ' ':
        cmd = 'e'
    #try:
    win.current.command(eval(cmd))#*{'a':(-1,0), 'd' : (1,0), 'w' : (0,-1), 's' : (0,1)}[cmd]))
    #except:
        #print('you input wrong')


#import system.boot
#from tg_modules import tg_gui as gui


'''from tg_modules import gui, gui_sensors
#from staging import sen_brd as sensor
from middle import sensor
import time

gui.io.fill(gui.io.color(0,0,255))

therm = gui_sensors.thermal_display(5,5,96,96,sensor.thermal_cam_data, (),
                                    border = 4, flip_x = 1, units_out = 2)

temp = 0
while temp <=500:
    temp = therm.refresh()[1]
therm.clear()

time.sleep(2)'''