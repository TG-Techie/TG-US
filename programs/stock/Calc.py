#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/17/18

from system.programs.__blank__app import init
exec(init)
import time

page0 = container.add_panel()

cont_y += 1 #add seperation bewteen top bar and text

page0.add(text = gui.text(cont_x, cont_y , cont_width, 14, ' ' , border = 1))

def enter_char(char):
    global page0
    page0.text.value += str(char)

def del_char():
    global page0
    page0.text.value = page0.text.value[0:-1]
   

def eval_exp():
    global page0
    try:
        page0.text.value = str(eval(page0.text.value.replace(' ','')))
    except Exception as e:
        #print(e)
        page0.text.value = 'ERR'
        time.sleep(.2)
        page0.text.value = str(e)

def clear_exp():
    global page0
    page0.text.value = ' '
    


page0.add(keypad = gui.nidos(cont_x, cont_y + 14, cont_width, cont_height - 14 -1, 4, 5))
page0.keypad.switch(1,2)

pad = page0.keypad

###numbers##################
pad.of(0,1).text = '1'
pad.of(0,1).set_purpose(enter_char,(1,))

pad.of(1,1).text = '2'
pad.of(1,1).set_purpose(enter_char,(2,))

pad.of(2,1).text = '3'
pad.of(2,1).set_purpose(enter_char,(3,))

pad.of(0,2).text = '4'
pad.of(0,2).set_purpose(enter_char,(4,))

pad.of(1,2).text = '5'
pad.of(1,2).set_purpose(enter_char,(5,))

pad.of(2,2).text = '6'
pad.of(2,2).set_purpose(enter_char,(6,))

pad.of(0,3).text = '7'
pad.of(0,3).set_purpose(enter_char,(7,))

pad.of(1,3).text = '8'
pad.of(1,3).set_purpose(enter_char,(8,))

pad.of(2,3).text = '9'
pad.of(2,3).set_purpose(enter_char,(9,))

pad.of(0,4).text = '0'
pad.of(0,4).set_purpose(enter_char,(0,))

###and deciaml point

pad.of(1,4).text = '.'
pad.of(1,4).set_purpose(enter_char,('.',))

######### operations #########
pad.of(3,1).text = '+'
pad.of(3,1).set_purpose(enter_char,('+',))

pad.of(3,2).text = '-'
pad.of(3,2).set_purpose(enter_char,('-',))

pad.of(3,3).text = '*'
pad.of(3,3).set_purpose(enter_char,('*',))

pad.of(3,4).text = '/'
pad.of(3,4).set_purpose(enter_char,('/',))

####### parents
pad.of(2,0).text = '('
pad.of(2,0).set_purpose(enter_char,('(',))

pad.of(3,0).text = ')'
pad.of(3,0).set_purpose(enter_char,(')',))
###### enter  clear del####

pad.of(2,4).text = 'Del'
pad.of(2,4).set_purpose(del_char,())

pad.of(0,0).text = '='
pad.of(0,0).set_purpose(eval_exp,())

pad.of(1,0).text = 'Clr'
pad.of(1,0).set_purpose(clear_exp,())