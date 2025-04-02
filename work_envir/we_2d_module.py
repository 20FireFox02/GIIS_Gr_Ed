import time
from wind_init_module import pg

from constant_module import PIXEL,FPS,WHITE

from classes.line_module import Line
from mouse_click_module import mouse_click
from drawing.draw_module import lines,DRAWING_ALG,draw

from work_envir.work_env_module import work_env


class work_env_2d(work_env):
    def __init__(self):
        self.draw_click,self.checkout_click=False,False
        self.alg_num=0

    def work(self):
        for event in pg.event.get():

            if event.type is pg.QUIT:
                pg.quit()
                exit()

            elif event.type==pg.MOUSEBUTTONDOWN:
                if not mouse_click(event.pos):
                    if 50<event.pos[0]<=1000:
                        if self.draw_click:DRAWING_ALG[self.alg_num].add_point(lines[-1],[event.pos[0]//PIXEL,event.pos[1]//PIXEL])
                        else:lines.append(Line([[event.pos[0]//PIXEL,event.pos[1]//PIXEL],\
                                        [event.pos[0]//PIXEL,event.pos[1]//PIXEL]],self.alg_num))
                        self.draw_click=DRAWING_ALG[self.alg_num].draw(self.draw_click)

                else:
                    draw(lambda:True)
                break

            elif event.type==pg.MOUSEMOTION:
            
                if self.draw_click:
                    if (abs(lines[-1].points[1][0]-event.pos[0]//PIXEL)>=1 \
                        or abs(lines[-1].points[1][1]-event.pos[1]//PIXEL)>=1)\
                        and 50<event.pos[0]:
                        lines[-1].upd_point([event.pos[0]//PIXEL,event.pos[1]//PIXEL])
                    
                        def sleep():
                            time.sleep(0.1)
                            pg.display.update()
                        if self.checkout_click:
                            draw(lambda:sleep())
                        else:
                            draw(lambda:True)
                break
                 
            elif event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    if self.draw_click:
                        self.draw_click=False
                        lines[-1].points.pop()
                    else:
                        try:
                            lines.pop()
                        except:
                            pass
                    draw(lambda:True)
                elif event.key==pg.K_TAB:
                    self.checkout_click=not self.checkout_click
                break

        super().work()