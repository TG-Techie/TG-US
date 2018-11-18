#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/14/18

#print(__name__)

import time
from tg_io.io_screen import disp

disp.text(0,6*8,'''--------
TG-US Version: ''' + str(0)+'''

Created By:
TG-Techie - Jonah Y-M

Thanks To:
K. Keough   Martin Y.
Joseph M.  Arlene Y.
J. Podel   J. Whalen''', size = 1 )

time.sleep(.25)

del time, disp

#r = RTC()
#rtc.set_time_source(r)