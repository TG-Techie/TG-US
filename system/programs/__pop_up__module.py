#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/17/18

from system.programs.__blank__app import gui, cont_x, cont_y, cont_width, cont_height, collect

global pop_up

def return_to_parent(target):
    global pop_up
    #remove the panel from the target
    #target.contents.pop(target.contents.index(target.nav))
    #del target.pop
    
    #make the target's nav the recent-most navigable gui_obj
    for obj in reversed(target.contents):
        if obj.is_navigable:
            target.nav = obj
            break
    
    pop_up.yes_no.of(0,0).set_purpose(print,('TG:POP_UP: "BridgeKeeper: Who would cross the bridge of death must answer me these questions three ere the other side he see"',))
    
    target.place()
    
#shape define
width17 = (cont_width/11)
height15 = (cont_height/9)
#setup the yes_no restart panel    
pop_up = gui.panel(int(cont_x + width17), int(cont_y + height15), 
                    int(cont_width - width17*2), int(cont_height - height15*2), background = gui.io.blue)

pop_up.add( rect = gui.rect(int(cont_x + width17), int(cont_y + height15), 
                    int(cont_width - width17*2), int(cont_height - height15*2), gui.io.blue))

#test for popup
pop_up.add( text = gui.text(int(cont_x + width17), int(cont_y + height15), 
                    int(cont_width - width17*2), int(cont_height - height15*4), 'this is a pop up',background = gui.io.blue) )

#button container (nidos)
pop_up.add(yes_no = gui.nidos(int(cont_x + width17), 
                    int(cont_y +cont_height- height15*3),
                    int(cont_width - width17*2), int(height15*2), 2,1, background = gui.io.blue))

pop_up.yes_no.switch(1,0)

#setup the buttons
pop_up.yes_no.of(0,0).set_purpose(print,('TG:POP_UP: "BridgeKeeper: Who would cross the bridge of death must answer me these questions three ere the other side he see"',))
pop_up.yes_no.of(0,0).text = 'YES'

pop_up.yes_no.of(1,0).set_purpose(return_to_parent, (None))
pop_up.yes_no.of(1,0).text = 'NO'

def summon(target, yes_func, yes_tup, message, but1_text = 'YES', but2_text = 'NO'):
    global pop_up,return_to_parent
    
    #set message
    pop_up.text.value = message
    
    #set up thing to do when yes
    pop_up.yes_no.of(0,0).set_purpose(yes_func, yes_tup)
    
    #set parent to return to
    pop_up.yes_no.of(1,0).set_purpose(return_to_parent, (target,))
    
    #target.add( pop = pop_up)
    target._nav = pop_up.nav
    #print(pop_up.nav, target.nav)
    target._overwrite_cmd_dict()
    pop_up.place()
    