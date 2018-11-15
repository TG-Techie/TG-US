#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/14/18

#in actuality import teh io_time to set the rtc
import rtc,time

class RTC(object):
    @property
    def datetime(self):
        return time.struct_time((2018,11,14,9,55,70,2,317,1,))

#r = RTC()
#rtc.set_time_source(r)