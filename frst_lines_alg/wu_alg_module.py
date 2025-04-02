from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

class Wu_alg(Line_Alg):

    def draw_line(self,points,check):
        x,y=points[0]
        dx=points[1][0]-x
        dy=points[1][1]-y
        pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

        if dy<0:
            ty=-1
        else:
            ty=1
        if dx<0:
            tx=-1
        else:
            tx=1
    
        def draw(x,y,col1,col2,xs,ys):
            pg.draw.rect(display,(col1,col1,col1),(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,(col2,col2,col2),\
                         ((x+xs)*PIXEL,(y+ys)*PIXEL,PIXEL,PIXEL))
        i=1
        if abs(dx)>abs(dy):
            try:
                gr=abs(dy/dx)*ty
            except:
                gr=0
            while i<=dx*tx:
                y+=gr
                b_y=int(y)
                x+=tx
                col1=255*(y-b_y)
                col2=255*(b_y-y+1)
                i+=1
                pg.draw.rect(display,(col1,col1,col1),\
                             (x*PIXEL,b_y*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,(col2,col2,col2),\
                             (x*PIXEL,(b_y+1)*PIXEL,PIXEL,PIXEL))
                check()
        else:
            try:
                gr=abs(dx/dy)*tx
            except:
                gr=0
            while i<=dy*ty:
                x+=gr
                b_x=int(x)
                y+=ty
                col1=255*(x-b_x)
                col2=255*(b_x-x+1)
                pg.draw.rect(display,(col1,col1,col1),\
                             (b_x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,(col2,col2,col2),\
                             ((b_x+1)*PIXEL,y*PIXEL,PIXEL,PIXEL))
                i+=1
                check()