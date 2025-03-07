from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Algoritm

class Dda(Algoritm):
    
    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=0

    def draw_line(self,points,check):
        
        x,y=points[0]
        lenght=max(abs(points[1][0]-x),abs(points[1][1]-y))
        try:
            dx=(points[1][0]-x)/lenght
            dy=(points[1][1]-y)/lenght
        except:
            dx,dy=0,0
        x+=0.5*round(dx,0)
        y+=0.5*round(dy,0)

        pg.draw.rect(display,BLACK,(int(x)*PIXEL,int(y)*PIXEL,PIXEL,PIXEL))
        i=0
        while i<=lenght:
            check()

            pg.draw.rect(display,BLACK,(int(x)*PIXEL,int(y)*PIXEL,PIXEL,PIXEL))
            x+=dx
            y+=dy
            i+=1