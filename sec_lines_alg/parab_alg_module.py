from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

class Parab_alg(Line_Alg):

    def draw(self, draw_click):
        return super().draw(draw_click)
    
    def draw_line(self,points,check):
        b_crd,e_crd=points
        b=e_crd[1]-b_crd[1]
        
        if b!=0:
            if b<0:ty=-1
            else:ty=1
            a=e_crd[0]-b_crd[0]
            lim=e_crd[1]
            delta=2*abs(b)-4*a**2
            x,y=b_crd
            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

            def deqz(x,y,delta):
                return x+1,y+ty,delta-4*a**2+2*abs(b)*(2*(x-b_crd[0])+1)
            while y*ty<lim*ty:
                if delta>0:
                    d=2*delta+4*a**2
                    if d>0:
                        y+=ty
                        delta=delta-4*a**2                   
                    else:x,y,delta=deqz(x,y,delta)
                elif delta<0:
                    d=2*delta-2*abs(b)*(2*(x-b_crd[0])+1)
                    if d<=0:
                        x+=1
                        delta=delta+2*abs(b)*(2*(x-b_crd[0])+1)
                    else:x,y,delta=deqz(x,y,delta)
                else:x,y,delta=deqz(x,y,delta)
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,y*PIXEL,PIXEL,PIXEL))
                check()