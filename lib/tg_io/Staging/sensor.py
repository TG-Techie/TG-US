#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

#TODOS:
#fix 
from staging import sen_brd, mother_brd

###################################
#thermal cam api and data adjustvc
def thermal_cam_data():
   return sen_brd.amg.pixels

#####################################
#gps chip ada
def gps_set_frequency(new = 1000):
    mother_brd.gps_chip.send_command(b'PMTK220,1000')
    
#####################################

def voc_data():
    return sen_brd.ccs.tvoc

def eco_data():
    return sen_brd.ccs.eco2

##################################

'''def time():
    return (tm_year=2000, tm_mon=1, tm_mday=1, tm_hour=0,
            tm_min=4, tm_sec=41, tm_wday=5, tm_yday=1, tm_isdst=-1)'''
