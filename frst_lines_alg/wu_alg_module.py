from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

<<<<<<< HEAD
class Wu_alg(Algoritm):

    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=0
=======
class Wu_alg(Line_Alg):
>>>>>>> temp-branch

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
                check()

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

        else:
            try:
                gr=abs(dx/dy)*tx
            except:
                gr=0
            while i<=dy*ty:
                check()

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
<<<<<<< HEAD
    """if dy<0:
        ty=-1
    else:
        ty=1
    if dx<0:
        tx=-1
    else:
        tx=1
"""
    
"""    while i<=m_l:
        y+=gr
        b_y=int(y)
        x+=1
        draw(x,b_y,255*(y-b_y),255*(b_y-y+1))
        i+=1"""
"""e=round(dy/dx,1)
    
    e=2*dy*ty-dx*tx

    print([x,y],e)
    def draw():
        while i<=dy*ty:
            if e<=0:
                x+=PIXEL*tx
                e+=2*dy*ty
            y+=PIXEL*ty
            e-=2*dx*tx
            i+=PIXEL
            print([x,y])
            #pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
            
    if e>dx*tx:
        while i<=dy*ty:
            if e<=dx*tx:
                x+=tx
                e+=2*dy*ty
            y+=ty
            e-=2*dx*tx
            i+=1
            print([x,y],e)
            #pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
    else:
        while i<=dx*tx:
            if e>=0:
                y+=ty
                e-=2*dx*tx
            x+=tx
            e+=2*dy*ty
            i+=1
            print([x,y],e)
            #pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))


cc((2,1),(6,3))"""
"""    while i<=dx:
        if e>=0:
            y+=PIXEL
            e-=2*dx
        x+=PIXEL
        e+=2*dy
        i+=PIXEL
        pg.draw.rect(display,BLACK,(x,y,PIXEL,PIXEL))"""
=======
                check()
>>>>>>> temp-branch
