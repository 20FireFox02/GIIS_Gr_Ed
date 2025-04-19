<<<<<<< HEAD
from drawing.draw_module import lines,drawing_alg,draw
from sys import exit
import time
=======
#from drawing.draw_module import lines,DRAWING_ALG,draw
#from sys import exit
#import time
>>>>>>> temp-branch

from wind_init_module import pg,clock,display
#from drawing.draw_menu_module import draw_menu

#from classes.line_module import Line
from constant_module import PIXEL,FPS,WHITE
#from mouse_click_module import mouse_click
#import var_module as vm

#from lab_4.cube_module import Cube
#from lab_4.read_file_module import read_file
#import math

import work_envir.var_work as vw
#draw_click,checkout_click=False,False

#draw_menu()
'''
T_SPEED=math.pi/40
R=5
SIN_T_P,SIN_T_N,COS_T=math.sin(T_SPEED),math.sin(-T_SPEED),math.cos(T_SPEED)

a=read_file("lab_4/figure.txt")'''

while True:
    vw.work_env.work()
    '''
    for event in pg.event.get():

        if event.type is pg.QUIT:
            pg.quit()
            exit()

        elif event.type==pg.MOUSEWHEEL:
            a.scaling(1-event.precise_y)
            display.fill(WHITE)
            a.draw()
            break
                 
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
            break
    

    if pg.key.get_pressed()[pg.K_a]:
        a.turn_y(SIN_T_P,COS_T)
        display.fill(WHITE)
        a.draw()
    elif pg.key.get_pressed()[pg.K_d]:
        display.fill(WHITE)
        a.turn_y(SIN_T_N,COS_T)    
        a.draw()
    elif pg.key.get_pressed()[pg.K_w]:
        display.fill(WHITE)
        a.turn_x(SIN_T_P,COS_T)    
        a.draw()
    elif pg.key.get_pressed()[pg.K_s]:
        display.fill(WHITE)
        a.turn_x(SIN_T_N,COS_T)    
        a.draw()
    elif pg.key.get_pressed()[pg.K_q]:
        display.fill(WHITE)
        a.turn_z(SIN_T_P,COS_T)    
        a.draw()
    elif pg.key.get_pressed()[pg.K_e]:
        display.fill(WHITE)
        a.turn_z(SIN_T_N,COS_T)    
        a.draw()

    elif pg.key.get_pressed()[pg.K_LEFT]:
        a.moving(-R,0,0)
        display.fill(WHITE)
        a.draw()
    elif pg.key.get_pressed()[pg.K_RIGHT]:
        a.moving(R,0,0)
        display.fill(WHITE)
        a.draw()
    elif pg.key.get_pressed()[pg.K_UP]:
        a.moving(0,-R,0)
        display.fill(WHITE)
        a.draw()
    elif pg.key.get_pressed()[pg.K_DOWN]:
        a.moving(0,R,0)
        display.fill(WHITE)
        a.draw()
    
    #elif pg.key.get_pressed()[pg.K_DOWN]
    '''
    #pg.display.update()
    #clock.tick(FPS)

    '''elif event.type==pg.MOUSEBUTTONDOWN:
            if not mouse_click(event.pos):
                if 50<event.pos[0]<=1000:
<<<<<<< HEAD
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
=======
                    if draw_click:DRAWING_ALG[vm.alg_num].add_point(lines[-1],[event.pos[0]//PIXEL,event.pos[1]//PIXEL])
                    else:lines.append(Line([[event.pos[0]//PIXEL,event.pos[1]//PIXEL],\
                                    [event.pos[0]//PIXEL,event.pos[1]//PIXEL]],vm.alg_num))
                    draw_click=DRAWING_ALG[vm.alg_num].draw(draw_click)

>>>>>>> temp-branch
            else:
                draw(lambda:True)

        elif event.type==pg.MOUSEMOTION:
            
            if draw_click:
<<<<<<< HEAD
                if (abs(lines[-1].points[-1][0]-event.pos[0]//PIXEL)>=1 \
                   or abs(lines[-1].points[-1][1]-event.pos[1]//PIXEL)>=1)\
                    and 10<event.pos[0]//PIXEL:
                    lines[-1].points[-1]=(event.pos[0]//PIXEL,event.pos[1]//PIXEL)
=======
                if (abs(lines[-1].points[1][0]-event.pos[0]//PIXEL)>=1 \
                   or abs(lines[-1].points[1][1]-event.pos[1]//PIXEL)>=1)\
                    and 50<event.pos[0]:
                    lines[-1].upd_point([event.pos[0]//PIXEL,event.pos[1]//PIXEL])
>>>>>>> temp-branch
                    
                    def sleep():
                        time.sleep(0.1)
                        pg.display.update()
                    if checkout_click:
                        draw(lambda:sleep())
                    else:
                        draw(lambda:True)'''