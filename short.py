from system import handler
import sys_config
sys_config.use_keyboard = 1
from system.sys_main import *
text = input('what program to test load?:')
print(len(text))
if len(text) == 0:
    text = 'example_ENT_SPC_SPC_SPC2'
print('loading:')
print(text)
handler.load(text)