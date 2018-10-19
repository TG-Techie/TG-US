#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/17/18

from tg_modules.tg_tools import holder
import time

from system import sys_config
from system import handler

system = holder()

system.add('sys_bar', handler.load('sys_bar', path  = 'system.programs', to_system = True))
handler.cur_cont.place()


time.sleep(3)