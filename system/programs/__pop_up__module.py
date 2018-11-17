#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/17/18

from system.programs.__blank__app import gui, cont_x, cont_y, cont_width, cont_height, collect


def return_to_parent(target):
    #remove the panel from the target
    #target.contents.pop(target.contents.index(target.nav))
    #del target.pop
    
    #make the target's nav the recent-most navigable gui_obj
    for obj in reversed(target.contents):
        if obj.is_navigable:
            target.nav = obj
            break
    
    target.place()
    

width17 = (cont_width/7)
height15 = (cont_height/5)
#setup the yes_no restart panel    
pop_up = gui.panel(int(cont_x + width17), int(cont_y + height15), 
                    int(cont_width - width17*2), int(cont_height - height15*2), background = gui.io.blue)

#test for popup
pop_up.add( text = gui.text(int(cont_x + width17), int(cont_y + height15), 
                    int(cont_width - width17*2), int(cont_height - height15*3), 'this is a pop up',background = gui.io.blue) )

#button container (nidos)
pop_up.add(yes_no = gui.nidos(int(cont_x + width17), 
                    int(cont_y +cont_height- height15*2),
                    int(width17*5), int(height15), 2,1, background = gui.io.blue))
#setup the buttons
pop_up.yes_no.of(0,0).set_purpose(print,('TG:POP_UP: "BridgeKeeper: Who would cross the bridge of death must answer me these questions three ere the other side he see"',))
pop_up.yes_no.of(0,0).text = 'YES'

pop_up.yes_no.of(1,0).set_purpose(return_to_parent, (None))
pop_up.yes_no.of(1,0).text = 'NO'

def summon_pop_up(target, yes_func, yes_tup, message):
    global pop_up
    
    #set message
    pop_up.text = message
    
    #set up thing to do when yes
    pop_up.yes_no.of(0,0).set_purpose(yes_func, yes_tup)
    
    #set parent to return to
    pop_up.yes_no.of(1,0).purpose_tup = (target,)
    
    #target.add( pop = pop_up)
    target._nav = pop_up.nav
    pop_up.place()
    