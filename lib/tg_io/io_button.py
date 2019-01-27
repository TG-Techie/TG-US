#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/28/18
import time, math
from tg_io.staging.touch_brd0 import cap0, cap1
cap0.reset()
cap1.reset()
#try:
#from tg_io.staging.touch_brd0 import cap1
#except: pass


#hardware specific code
num2cmd_dict = { 3 : '<', 4:'E', 5:'>', 6:'H', 2:'S' , 16 : 'SPKR', 17 : 'EMRG', 12: 'F4', 23:'F5', 22:'F6', 21:'F7'}

reset_counter = 0
reset_num = 13
def get_commands(debug = False):
    global reset_counter
    #print(cap1.touched())
    #returning a list of cmds
    out_list = []

    #this is harware specific code too
    #cap0.reset()
    time.sleep(.005)
    data = (cap0.touched() )+ (cap1.touched()<<12)
    reset_counter +=1
    if reset_counter == reset_num:
        cap0.reset()
        cap1.reset()
        reset_counter = 0
    if data:
        for shifter in range(24):
            if 1<<shifter & data:
                try:
                    out_list.append(num2cmd_dict[shifter])
                except: pass

        #print(out_list)
        del data
        return out_list
        if debug:
            print(data)
            print(out_list)
    else:
        return []