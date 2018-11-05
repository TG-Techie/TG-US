#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/31/18

from system.programs.__blank__app import init
exec(init)


def add_numed_pages(num): #contianer is already defined so it doesn't need to be passed
    but_list = []
    for page_num in range(num):
        pointer = container.add_panel()
        pointer.add( label = gui.text(cont_x,cont_y, cont_width, 12,
                    'page:('+str(page_num+1)+'/'+str(num)+')'))
        pointer.add( menu = gui.nidos(cont_x, cont_y + 13, cont_width, cont_height - 13, 3,3,
                    superior = container))
        but_list += pointer.menu.contents
    
    bod_list = """BRIDGE
KEEPER: Stop! Who would cross the Bridge of Death must answer me these ques-
tions three, ere the other side he see
LANCLT: Ask me the ques-
tions, bridge
keeper. I am not afraid.
BRIDGE
KEEPER: What... is your name?
LANCLT: My name is 'Sir Lance-
lot of Camelt'.
BRIDGE
KEEPER: What... is your quest?
LANCLT: To seek the Holy Grail.
BRIDGE
KEEPER: What... is your favorite color?
LANCLT: Blue.
BRIDGE
KEEPER: Right. Off you go. 
LANCLT: Oh, thank you. Thank you very much.""".split()
    for pos in range(len(bod_list)):
        try: 
            but_list[pos].text = bod_list[pos]
            but_list[pos].error_message = '__?__\n'+bod_list[pos]
        except: pass
        
    container.switch(0)
    #print('gunumbly')
    

#make the intial screen three buttons to chose nubmer of pages
#pagei stands for initial page
pagei = container.add_panel(should_index = 0)

pagei.add( choose = gui.nidos(0,50,160,30,3,1))
pagei.add( text = gui.text(0,35,cont_width,12,'choose the nubmer of pages in the example'))


choose = pagei.choose
choose.of(0,0).text = '3 pages'
choose.of(0,0).set_purpose(add_numed_pages, (3,))

choose.of(1,0).text = '6 pages'
choose.of(1,0).set_purpose(add_numed_pages, (5,))

choose.of(2,0).text = '7 pages'
choose.of(2,0).set_purpose(add_numed_pages, (7,))