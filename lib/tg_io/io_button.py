#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/28/18

try: from tg_io.staging.touch_brd0 import cap0
except: pass

try: from tg_io.staging.touch_brd0 import cap1
except: pass

#hardware specific code
cap0_num2cmd_dict = {0 : '<', 1:'E', 2:'>'}

def get_commands():
    #returning a list of cmds
    out_list = []
    
    #this is harware specific code too
    for pos in range(12):
        if cap0[pos].value:
            try:
               out_list.append(cap0_num2cmd_dict[pos])
            except KeyError:
                pass
    
    #print(out_list)
    return out_list
            