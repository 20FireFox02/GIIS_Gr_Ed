from drawing.draw_module import lines,drawing_alg,draw
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

while True:
    for event in pg.event.get():

        if event.type is pg.QUIT:
            pg.quit()
            exit()
            
        elif event.type==pg.MOUSEBUTTONDOWN:
            if not mouse_click(event.pos):
                if 50<event.pos[0]<=1000:
                    if not draw_click:
                        lines.append(Line((event.pos[0]//PIXEL,event.pos[1]//PIXEL),vm.alg_num)) 
                    def click():
                        if drawing_alg[vm.alg_num].step<1:
                            drawing_alg[vm.alg_num].step+=1
                            lines[-1].new_point((event.pos[0]//PIXEL,event.pos[1]//PIXEL))
                            return True
                        else:
                            drawing_alg[vm.alg_num].ret_step()
                            return False
                    draw_click=click()
                else:
                    draw_click=False      
            else:
                draw(lambda:True)

        elif event.type==pg.MOUSEMOTION:
            
            if draw_click:
                if (abs(lines[-1].points[-1][0]-event.pos[0]//PIXEL)>=1 \
                   or abs(lines[-1].points[-1][1]-event.pos[1]//PIXEL)>=1)\
                    and 10<event.pos[0]//PIXEL:
                    lines[-1].points[-1]=(event.pos[0]//PIXEL,event.pos[1]//PIXEL)
                    
                    def sleep():
                        time.sleep(0.1)
                        pg.display.update()
                    if checkout_click:
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