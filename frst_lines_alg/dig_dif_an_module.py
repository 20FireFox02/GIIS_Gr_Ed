from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

class Dda(Line_Alg):

    def draw(self, draw_click):
        return super().draw(draw_click)
    
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
            
            pg.draw.rect(display,BLACK,(int(x)*PIXEL,int(y)*PIXEL,PIXEL,PIXEL))
            x+=dx
            y+=dy
            i+=1
            check()