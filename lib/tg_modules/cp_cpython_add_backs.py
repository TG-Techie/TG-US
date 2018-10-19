#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

'''This is a module made to add currently missing features back to
adafruit's circuit python. It is a poor substitue b/c it will take 
up more memory and it isn't in the base firmware. i find it better than nothing'''

def delattr(target,name): #Credit: Jonah Yolles-Murphy
    exec('del str_target.'+name, {'str_target':target})
