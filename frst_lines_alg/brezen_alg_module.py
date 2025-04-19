from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

<<<<<<< HEAD
class Brz_alg(Algoritm):

    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=0
    
    def draw_line(self,points,check):
=======
class Brz_alg(Line_Alg):

    def draw_line(self,points,check,color=BLACK):
>>>>>>> temp-branch
        x,y=points[0]
        dx=points[1][0]-x
        dy=points[1][1]-y
        i=1
        pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

        if dy<0:ty=-1
        else:ty=1
        if dx<0:tx=-1
        else:tx=1
        
        e=2*dy*ty-dx*tx
            
        if e>dx*tx:
            while i<=dy*ty:
                check()
                
                if e<=dx*tx:
                    x+=tx
                    e+=2*dy*ty
                y+=ty
                e-=2*dx*tx
                i+=1
<<<<<<< HEAD
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

=======
                pg.draw.rect(display,color,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                check()
>>>>>>> temp-branch
        else:
            while i<=dx*tx:
                check()

                if e>=0:
                    y+=ty
                    e-=2*dx*tx
                x+=tx
                e+=2*dy*ty
                i+=1
<<<<<<< HEAD
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

"""    while i<=dx:
        if e>=0:
            y+=PIXEL
            e-=2*dx
        x+=PIXEL
        e+=2*dy
        i+=PIXEL
        pg.draw.rect(display,BLACK,(x,y,PIXEL,PIXEL))"""
=======
                pg.draw.rect(display,color,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                check()
        
>>>>>>> temp-branch
