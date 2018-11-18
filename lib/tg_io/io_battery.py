#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/14/18

import random

temp = 100.33333333333333333333333333333333333333333
def get_percentage():
    global temp
    temp = (temp -.333) % 101
    return temp/100

def is_charging():
    val = random.choice([True, False,False,False,False,False,False,False,False])
    #print(val)
    return val