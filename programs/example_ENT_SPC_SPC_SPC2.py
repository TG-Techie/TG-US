#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/31/18

from system.programs.__blank__app import init
exec(init)


def add_numed_pages(num): #contianer is already defined so it doesn't need to be passed
    for page_num in range(num):
        pointer = container.add_panel()
        pointer.add( label = gui.text(cont_x,cont_y, cont_width, 12,
                    'page:('+str(page_num+1)+'/'+str(num)+')'))
        pointer.add( menu = gui.nidos(cont_x, cont_y + 13, cont_width, cont_height - 13, 3,3,
                    superior = container))
    
    container.switch(0)
    #print('gunumbly')
    

#make the intial screen three buttons to chose nubmer of pages
#pagei stands for initial page
pagei = container.add_panel(should_index = 0)

pagei.add( choose = gui.nidos(0,50,160,30,3,1))
pagei.add( text = gui.text(0,35,cont_width,12,'choose the nubmer of pages in the example'))


choose = pagei.choose
choose.of(0,0).text = '2 pages'
choose.of(0,0).set_purpose(add_numed_pages, (2,))

choose.of(1,0).text = '3 pages'
choose.of(1,0).set_purpose(add_numed_pages, (3,))

choose.of(2,0).text = '5 pages'
choose.of(2,0).set_purpose(add_numed_pages, (5,))