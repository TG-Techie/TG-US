#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

import digitalio, pulseio, analogio#, touchio #, audioio


def dio(pin, direction = None, init_val = None):
    io = digitalio.DigitalInOut(pin)
    if direction != None:
        if direction:
            io.direction = digitalio.Direction.INPUT
            #io.value = init_val
        else:
            io.direction = digitalio.Direction.OUTPUT
            io.value = init_val
    return(io)
    
def pwm(pin, init_val = None, init_freq = None):
    io = pulseio.PWMOut(pin)
    
    if init_val:
        io.duty_cycle = init_val
    else:
        io.duty_cycle = 0
    
    if init_freq:
        io.frequency = init_freq
        
    return io
        