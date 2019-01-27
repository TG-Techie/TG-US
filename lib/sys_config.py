#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18

import supervisor
from tg_io.io_screen import disp

enable_sys_bar = 1
enable_nav_bar = 0

std_path = 'programs'

home_prog_path = 'system.programs'
home_prog_name = 'launcher'
#VV this VV is weather the prog should be put in system and hidden from the user or:
#show it in the app loaded apps
home_prog_index = False

military_time = 0

settings_active = 1
settings_prog = 'settings'
settings_path = 'system.programs'

prog_path = 'programs.user'

system_refresh_interval = 20


usb_connected = supervisor.runtime.serial_connected

#check if should use keyboard
if usb_connected :
    disp.text(10,10,'''answer
query over
serial port''',size = 2)
    valin = str(input('use keybaord as input?(yes or no):')).lower()
    if ('y'  in valin) or ( '1' in valin):
        use_keyboard = 1
        print('using keyboard')
    else:
        use_keyboard = 0
        print('not using keyboard')
    disp.fill(0)
else:
    use_keyboard = 0

DEBUG_module_locaiton_output = 1

# not implemented show_prog_error = 0