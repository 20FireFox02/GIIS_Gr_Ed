from drawing.draw_module import lines,draw
from sys import exit
import time

from wind_init_module import pg,clock
from drawing.draw_menu_module import draw_menu

from classes.line_module import Line
from constant_module import PIXEL,FPS
from mouse_click_module import mouse_click
import var_module as vm

draw_click,checkout_click=False,False

draw_menu()
draw(lambda:True)
while True:
    for event in pg.event.get():

        if event.type is pg.QUIT:
            pg.quit()
            exit()
            
        elif event.type==pg.MOUSEBUTTONDOWN:
            if not mouse_click(event.pos):
                if 50<event.pos[0]<=1000:
                    draw_click=not draw_click
                else:
                    draw_click=False
                if draw_click:
                    lines.append(Line([[event.pos[0]//PIXEL,event.pos[1]//PIXEL],\
                                  [event.pos[0]//PIXEL,event.pos[1]//PIXEL]],vm.alg_num))       
            else:
                draw(lambda:True)

        elif event.type==pg.MOUSEMOTION:
            
            if draw_click:
                if (abs(lines[-1].end_crd[0]-event.pos[0]//PIXEL)>=1 \
                   or abs(lines[-1].end_crd[1]-event.pos[1]//PIXEL)>=1)\
                    and 10<event.pos[0]//PIXEL:
                    lines[-1].end_crd=(event.pos[0]//PIXEL,event.pos[1]//PIXEL)
                    
                    def sleep():
                        time.sleep(0.1)
                        pg.display.update()
                    if checkout_click:
                        print("HERE")
                        draw(lambda:sleep())
                    else:
                        draw(lambda:True)

        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                try:
                    lines.pop()
                    draw(lambda:True)
                except:
                    pass
            elif event.key==pg.K_TAB:
                checkout_click=not checkout_click
   
    pg.display.update()
    clock.tick(FPS)