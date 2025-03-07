from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Algoritm

class Parab_alg(Algoritm):
    
    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=0

    def draw_line(self,points,check):
        b=points[1][1]-points[0][1]
        
        if b!=0:
            if b<0:ty=-1
            else:ty=1
            a=points[1][0]-points[0][0]
            lim=points[1][1]
            delta=2*abs(b)-4*a**2
            x,y=points[0]
            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

            def deqz(x,y,delta):
                return x+1,y+ty,delta-4*a**2+2*abs(b)*(2*(x-points[0][0])+1)
            while y*ty<lim*ty:
                check()

                if delta>0:
                    d=2*delta+4*a**2
                    if d>=0:
                        y+=ty
                        delta=delta-4*a**2                   
                    else:x,y,delta=deqz(x,y,delta)
                elif delta<0:
                    d=2*delta-2*abs(b)*(2*(x-points[0][0])+1)
                    if d<0:
                        x+=1
                        delta=delta+2*abs(b)*(2*(x-points[0][0])+1)
                    else:x,y,delta=deqz(x,y,delta)
                else:x,y,delta=deqz(x,y,delta)
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((points[0][0]-x+points[0][0])*PIXEL,y*PIXEL,PIXEL,PIXEL))