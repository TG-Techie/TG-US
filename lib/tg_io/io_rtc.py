#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/14/18
import time,rtc
#setup here

from tg_io.staging.ds3231_setup import ds_rtc

###helpers and tools



###HEY!! #### set the same of your rtc hardware intance to chip
#like:
#chip = ds3231_instance
chip = ds_rtc

#harware speciifc returns

def push_to_local():
    global chip
    rtc.set_time_source(chip)

def set_time(year = 2000, month =1, day_of_month =1,
            hour = 1, minute = 1, second = 1,
            day_of_week = 6, day_of_year = 1, day_light_savings = -1):

    global chip,push_to_local

    x = (year, month, day_of_month, hour, minute,second , day_of_week, day_of_year, day_light_savings,)
    chip.datetime = time.struct_time()

    push_to_local()

def talk_set_time():
    year = int(input('year:'))
    month = int(input('month:'))
    day_of_month = int(input('day_of_month:'))
    day_of_week = int(input('day_of_week, 0 = monday:'))
    day_of_year = int(input('day_of_year:'))
    day_light_savings = int(input('is daylight savings, (1,0, -1 = ?):'))
    hour = int(input('hour:'))
    minute = int(input('minute:'))
    second = int(input('second:'))

    x = (year, month, day_of_month, hour, minute,second , day_of_week, day_of_year, day_light_savings,)
    chip.datetime = time.struct_time()

    push_to_local()

push_to_local()