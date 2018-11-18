#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/28/18
import time
from tg_io.staging.touch_brd0 import cap0
cap0.reset()

try: from tg_io.staging.touch_brd0 import cap1
except: pass

#hardware specific code
cap0_num2cmd_dict = {3 : '<', 4:'E', 5:'>', 6:'H', 2:'S'}

def get_commands():
    #returning a list of cmds
    out_list = []
    
    #this is harware specific code too
    #cap0.reset()
    time.sleep(.005)
    data = cap0.touched()
    #print(bin(data))
    if data:
        for shifter in range(12):
            if 1<<shifter & data:
                try:
                    out_list.append(cap0_num2cmd_dict[shifter])
                except: pass
        time.sleep(.005)
    
        
        #print(out_list)
        del data
        return out_list
    else:
        return []