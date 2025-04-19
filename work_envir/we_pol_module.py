import time
from wind_init_module import pg,display

from constant_module import PIXEL,BLACK,BLUE

from classes.line_module import Line

from polygon.polygon_module import Polygon

from polygon.pol_alg import Pol_alg
from polygon.greh_alg import Greh_alg
from polygon.djarw_alg import Djarw_alg

from mouse_click_module import mouse_click
from drawing.draw_module import polygons,points,draw,draw_menu

from work_envir.work_env_module import work_env

DRAW_ALG=[Pol_alg,Greh_alg,Djarw_alg]

class work_env_pol(work_env):
    def __init__(self):
        self.draw_click=False
        self.alg_num=0
        #points=[]

    def work(self):
        '''def draw():
            display.fill(WHITE)
            for pol in polygons:pol.draw_pol()
            for point in points:pg.draw.rect(display,BLACK,(point[0]*PIXEL,point[1]*PIXEL,PIXEL,PIXEL))
            draw_menu()'''
        for event in pg.event.get():

            if event.type is pg.QUIT:
                pg.quit()
                exit()

            elif event.type==pg.MOUSEBUTTONDOWN:
                if not mouse_click(event.pos):
                    if 50<event.pos[0]<=1000:
                        def check():
                            for pol in polygons:
                                if pol.find_point(int(event.pos[0]//PIXEL),int(event.pos[1]//PIXEL)):
                                    #print(True)
                                    return True
                            return False
                        if not check():
                            self.draw_click=True
                            points.append([int(event.pos[0]/PIXEL),int(event.pos[1]/PIXEL)])
                draw(lambda:True)
                for point in points:pg.draw.circle(display,BLUE,(point[0]*PIXEL,point[1]*PIXEL),5)
                break

                '''elif event.type==pg.MOUSEMOTION:
            
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
                break'''
                 
            elif event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    if self.draw_click:
                        points.pop()

                    else:
                        polygons.pop()
                    
                elif event.key==pg.K_RETURN:
                    self.draw_click=False
                    polygons.append(DRAW_ALG[self.alg_num].find_pol(points))
                    points.clear()
                draw(lambda:True)
                for point in points:pg.draw.rect(display,BLACK,(point[0]*PIXEL,point[1]*PIXEL,PIXEL,PIXEL))
                break

        super().work()