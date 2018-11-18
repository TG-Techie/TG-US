#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/18/18

import time, sys

from tg_io.io_screen import disp

try:
    disp.text(0,0,'TGT', size =2  )
except Exception as e:
    sys.print_exception(e)
    print(e)
    print('failed')

#time.sleep(10000000000)
from system import sys_main