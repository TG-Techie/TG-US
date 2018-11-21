#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

import storage

storage.remount("/", readonly=True)

m = storage.getmount("/")
m.label = "CIRCUITPY"

storage.remount("/", readonly=False)