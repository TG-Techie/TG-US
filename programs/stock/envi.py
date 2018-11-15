#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/14/18

from system.programs.__blank__app import init
exec(init)
wants_refresh = 1

from tg_io import io_temp, io_light

page0 = container.add_panel()
page1 = container.add_panel()

bar_width = cont_width
bar_height = 10

####################################################
###page 0

cur_y = cont_y + 2
increment_val = 10

page0.add( but = gui.nidos(cont_x, cont_y +cont_width-3, cont_width, 3, 1,1, x_gap = 0, y_gap = 0, superior = container))

###temp#############
label_t_g = '-temp / gas'
page0.add(label_t_g = gui.text(cont_x, cur_y,len(label_t_g)*7, increment_val, label_t_g ))
cur_y += increment_val

temp_text = 'Temp(c):'
page0.add(temp_text = gui.text(cont_x, cur_y,len(temp_text)*7, increment_val, temp_text ))
cur_y += increment_val

page0.add( temp_bar = gui.value_bar(cont_x,cur_y, bar_width, bar_height, io_temp.get_temp_c, ()) )
cur_y += increment_val

###voc##############





####################################################################################################################
# page 1
####################################################################################################################

cur_y = cont_y + 2
increment_val = 10

page1.add( but = gui.nidos(cont_x, cont_y +cont_width-3, cont_width, 3, 1,1, x_gap = 0, y_gap = 0, superior = container))

###light##############
label_light = '-light'
page1.add(light_label = gui.text(cont_x, cur_y,len(label_light)*7, increment_val, label_light ))
cur_y += increment_val

#ambi
ambi_text = 'Ambi:'
page1.add(ambi_text = gui.text(cont_x, cur_y,len(ambi_text)*7, increment_val, ambi_text ))
print('moop')
cur_y += increment_val

page1.add( ambi_bar = gui.value_bar(cont_x,cur_y, bar_width, bar_height, io_light.get_ambi_brightness, ()) )
cur_y += increment_val

#vis
visual_text = 'visual:'
page1.add(visual_text = gui.text(cont_x, cur_y,len(visual_text)*7, increment_val, visual_text ))
cur_y += increment_val

page1.add( vis_bar = gui.value_bar(cont_x,cur_y, bar_width, bar_height, io_light.get_vis_brightness, ()) )
cur_y += increment_val

# ir
ir_text = 'IR:'
page1.add(ir_text = gui.text(cont_x, cur_y,len(ir_text)*7, increment_val, ir_text ))
cur_y += increment_val

page1.add( ir_bar = gui.value_bar(cont_x,cur_y, bar_width, bar_height, io_light.get_ir_brightness, ()) )
cur_y += increment_val

#uv
uv_text = 'UV: not supported'
page1.add(uv_text = gui.text(cont_x, cur_y,len(uv_text)*7, increment_val, uv_text ))
cur_y += increment_val

'''
page1.add( uv_bar = gui.value_bar(cont_x,cur_y, bar_width, bar_height, io_light.get_uv_brightness, ()) )
cur_y += increment_val
'''
