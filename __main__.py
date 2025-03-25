from drawing.draw_module import lines,DRAWING_ALG,draw
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

n=0
while True:
    for event in pg.event.get():

        if event.type is pg.QUIT:
            pg.quit()
            exit()
            
        elif event.type==pg.MOUSEBUTTONDOWN:
            if not mouse_click(event.pos):
                if 50<event.pos[0]<=1000:
                    if draw_click:lines[-1].points.append([event.pos[0]//PIXEL,event.pos[1]//PIXEL])
                    else:lines.append(Line([[event.pos[0]//PIXEL,event.pos[1]//PIXEL],\
                                    [event.pos[0]//PIXEL,event.pos[1]//PIXEL]],vm.alg_num))
                    draw_click=DRAWING_ALG[vm.alg_num].draw(draw_click)      
            else:
                draw(lambda:True)

        elif event.type==pg.MOUSEMOTION:
            
            if draw_click:
                if (abs(lines[-1].points[1][0]-event.pos[0]//PIXEL)>=1 \
                   or abs(lines[-1].points[1][1]-event.pos[1]//PIXEL)>=1)\
                    and 10<event.pos[0]//PIXEL:
                    lines[-1].points[-1]=[event.pos[0]//PIXEL,event.pos[1]//PIXEL]
                    
                    def sleep():
                        time.sleep(0.1)
                        pg.display.update()
                    if checkout_click:
                        draw(lambda:sleep())
                    else:
                        draw(lambda:True)

        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                if draw_click:
                    draw_click=False
                    lines[-1].points.pop()
                else:
                    try:
                        lines.pop()
                    except:
                        pass
                draw(lambda:True)
            elif event.key==pg.K_TAB:
                checkout_click=not checkout_click
   
    pg.display.update()
    clock.tick(FPS)