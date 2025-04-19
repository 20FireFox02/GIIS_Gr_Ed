from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

<<<<<<< HEAD
class Brz_circle_alg(Algoritm):
    
    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=0

    def draw_line(self,points,check):
        dx=points[1][0]-points[0][0]
        dy=points[1][1]-points[0][1]
        lim=points[0][1]
=======
class Brz_circle_alg(Line_Alg):

    def draw_line(self,points,check):

        # Получение заданных точек и приращений
        b_crd,e_crd=points
        dx=e_crd[0]-b_crd[0]
        dy=e_crd[1]-b_crd[1]
        lim=b_crd[1]
>>>>>>> temp-branch
        
        # Начальная ошибка
        r=int((dx**2+dy**2)**0.5)
        delta=2-2*r

<<<<<<< HEAD
        x=points[0][0]
        y=points[0][1]+r
        pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
        pg.draw.rect(display,BLACK,(x*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
        def deqz(x,y,delta):
            return x+1,y-1,delta+2*(x-points[0][0]+1)-2*(y-points[0][1]-1)+2
        while y>lim:
            check()

            if delta<0:
                d=2*delta+2*(y-points[0][1])-1
=======
        # Координаты начальной точки
        x=b_crd[0]
        y=b_crd[1]+r

        # Отображение начальных точек
        pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
        pg.draw.rect(display,BLACK,(x*PIXEL,(b_crd[1]-y+b_crd[1])*PIXEL,PIXEL,PIXEL))

        # Двигаемя по диагонали
        def deqz(x,y,delta):return x+1,y-1,delta+2*(x-b_crd[0]+1)-2*(y-b_crd[1]-1)+2

        # Отображение
        while y>lim:

            if delta<0:

                d=2*delta+2*(y-b_crd[1])-1
>>>>>>> temp-branch
                if d<=0:

                    # Двигаемся по горизонтали
                    x+=1
<<<<<<< HEAD
                    delta=delta+2*(x-points[0][0])+1
                else:x,y,delta=deqz(x,y,delta)
            elif delta>0:
                d=2*delta-2*(x-points[0][0])-1
=======
                    delta=delta+2*(x-b_crd[0])+1

                else:x,y,delta=deqz(x,y,delta)
            elif delta>0:

                d=2*delta-2*(x-b_crd[0])-1
>>>>>>> temp-branch
                if d>0:

                    # Двигаемся по вертикали
                    y-=1
<<<<<<< HEAD
                    delta=delta-2*(y-points[0][1])+1
=======
                    delta=delta-2*(y-b_crd[1])+1

>>>>>>> temp-branch
                else:x,y,delta=deqz(x,y,delta)
            else:x,y,delta=deqz(x,y,delta)

            # Отображение найденных точек
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
