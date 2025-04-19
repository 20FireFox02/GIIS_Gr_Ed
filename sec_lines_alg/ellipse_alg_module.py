from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

<<<<<<< HEAD
class Ellipse_alg(Algoritm):
    
    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=0

    def draw_line(self,points,check):
        a=points[1][0]-points[0][0]
        b=points[1][1]-points[0][1]
        lim=points[0][1]
=======
class Ellipse_alg(Line_Alg):

    def draw_line(self,points,check):

        # Получение заданных точек и приращения
        b_crd,e_crd=points
        a=e_crd[0]-b_crd[0]
        b=e_crd[1]-b_crd[1]
        lim=b_crd[1]
>>>>>>> temp-branch

        # Начальная ошибка и координаты начальной точки
        delta=a**2*(1-2*abs(b))+b**2
<<<<<<< HEAD
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
=======
        x=b_crd[0]
        y=b_crd[1]+abs(b)

        # Отображение начальных точек
        pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
        pg.draw.rect(display,BLACK,(x*PIXEL,(b_crd[1]-y+b_crd[1])*PIXEL,PIXEL,PIXEL))

        # Двигаемя по диагонали
        def deqz(x,y,delta):return x+1,y-1,delta+(2*(x-b_crd[0])+1)*b**2+(-2*(y-b_crd[1])+1)*a**2

        # Отображение
        while y>lim:

            if delta<0:

                d=2*delta+2*(y-b_crd[1])*a**2-1
>>>>>>> temp-branch
                if d<=0:

                    # Двигаемя по горизонтали
                    x+=1
<<<<<<< HEAD
                    delta=delta+b**2*(2*(x-points[0][0])+1)
                else:x,y,delta=deqz(x,y,delta)
            elif delta>0:
                d=2*delta-2*(x-points[0][0])*b**2-1
=======
                    delta=delta+b**2*(2*(x-b_crd[0])+1)
                    
                else:x,y,delta=deqz(x,y,delta)
            elif delta>0:

                d=2*delta-2*(x-b_crd[0])*b**2-1
>>>>>>> temp-branch
                if d>0:

                    # Двигаемя по вертикали
                    y-=1
<<<<<<< HEAD
                    delta=delta+a**2*(-2*(y-points[0][1])+1)
=======
                    delta=delta+a**2*(-2*(y-b_crd[1])+1)

>>>>>>> temp-branch
                else:x,y,delta=deqz(x,y,delta)
            else:x,y,delta=deqz(x,y,delta)

            # Отображение полученных точек
            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
<<<<<<< HEAD
            pg.draw.rect(display,BLACK,(x*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,y*PIXEL,PIXEL,PIXEL))
=======
            pg.draw.rect(display,BLACK,(x*PIXEL,(b_crd[1]-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,(b_crd[1]-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,y*PIXEL,PIXEL,PIXEL))

            # Отладка
            check()
>>>>>>> temp-branch
