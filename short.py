valin = int(input('1 or 0:'))
if valin:
    from programs.stock._SPC2048_SPC import *
else:
    from programs.stock.__tfte_2048 import *
    t = Tile
print(dir())