from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Algoritm

class Ellipse_alg(Algoritm):
    
    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=0

    def draw_line(self,points,check):
        a=points[1][0]-points[0][0]
        b=points[1][1]-points[0][1]
        lim=points[0][1]

        delta=a**2*(1-2*abs(b))+b**2
        x=points[0][0]
        y=points[0][1]+abs(b)
        pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
        pg.draw.rect(display,BLACK,(x*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
        def deqz(x,y,delta):
            return x+1,y-1,delta+(2*(x-points[0][0])+1)*b**2+(-2*(y-points[0][1])+1)*a**2
        while y>lim:
            check()
            
            if delta<0:
                d=2*delta+2*(y-points[0][1])*a**2-1
                if d<=0:
                    x+=1
                    delta=delta+b**2*(2*(x-points[0][0])+1)
                else:x,y,delta=deqz(x,y,delta)
            elif delta>0:
                d=2*delta-2*(x-points[0][0])*b**2-1
                if d>0:
                    y-=1
                    delta=delta+a**2*(-2*(y-points[0][1])+1)
                else:x,y,delta=deqz(x,y,delta)
            else:x,y,delta=deqz(x,y,delta)

            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,(x*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,y*PIXEL,PIXEL,PIXEL))