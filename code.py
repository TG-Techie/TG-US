#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/18/18

import time, sys
from tg_io import io_screen as disp


#time.sleep(100)
try:
    from system import sys_main
except:
    disp.fill(disp.color(255,0,0))
    disp.fill(disp.color(0,0,0))
    disp.text(0,0,'''ERROR:''', size = 2)
    disp.text(0,20,'''check the
repl''', size = 1)