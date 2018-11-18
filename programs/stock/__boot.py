#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/31/18

from tg_io.io_screen import disp
disp.text(0,0,'''Trico05A''', size =3  )

disp.text(0,3*8,

'''Rev:A00
Firmware Version: N/A
Serial: N/A''', size = 1 )


import sys_config as sc

from tg_io import io_rtc as rtc