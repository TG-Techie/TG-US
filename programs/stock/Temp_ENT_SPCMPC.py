from system.programs.__blank__app import init
exec(init)
wants_refresh = 1

from tg_io import io_screen as io
from adafruit import adafruit_mcp9808
from tg_io.staging.pin_port import i2c_port
mcp = adafruit_mcp9808.MCP9808(i2c_port)

page = container.add_panel()

units = 1
delayer = 0
last_temp = ''
def temp_updater( bypass = False):
    global delayer, last_temp
    temp = mcp.temperature
    if units == 1:
        temp  =  str(  int(10*((temp/100)*(180) + 32)) /10) + 'F__degreesign__'
    elif units == 2:
        temp = str(int(10*(temp + 273))/10) + 'K'
    else:
        temp = str( int(10*temp)/10)+'C__degreesign__'

    if (not delayer and not last_temp == temp) or (bypass):
        io.rect(cont_x + 40, cont_y +30, 90, 40, 0)
        io.text(cont_x + 40, cont_y +30, temp, size = 2)
    delayer += 1
    delayer = delayer%5
    last_temp = temp

def set_units(valin):
    global units
    units = valin
    temp_updater(bypass = True)

page.add( temp_refresher = gui.on_refresh(temp_updater, ()))

page.add( unit_sel = gui.nidos(cont_x, cont_y + 90, cont_width, cont_height - 90, 3, 1))

pointer_menu = page.unit_sel

pointer = pointer_menu.of(0,0)
pointer.text = 'C__degreesign__'
pointer.set_purpose(set_units, (0,))

pointer = pointer_menu.of(1,0)
pointer.text = 'F__degreesign__'
pointer.set_purpose(set_units, (1,))

pointer = pointer_menu.of(2,0)
pointer.text = 'K'
pointer.set_purpose(set_units, (2,))