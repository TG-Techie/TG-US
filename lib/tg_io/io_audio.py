#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 01/25/19

from tg_io.staging.pin_port import spkr, spkr_en

speaker = spkr

def mute():
    spkr_en.value = 0

def unmute():
    spkr_en.value = 1