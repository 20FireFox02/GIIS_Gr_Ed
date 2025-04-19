from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

<<<<<<< HEAD
class Parab_alg(Algoritm):
    
    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=0

    def draw_line(self,points,check):
        b=points[1][1]-points[0][1]
=======
class Parab_alg(Line_Alg):
 
    def draw_line(self,points,check):

        # Получение заданных точек и значения b
        b_crd,e_crd=points
        b=e_crd[1]-b_crd[1]
>>>>>>> temp-branch
        
        # Проверка валидности
        if b!=0:

            # Получение знака построения
            if b<0:ty=-1
            else:ty=1
<<<<<<< HEAD
            a=points[1][0]-points[0][0]
            lim=points[1][1]
            delta=2*abs(b)-4*a**2
            x,y=points[0]
            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

            def deqz(x,y,delta):
                return x+1,y+ty,delta-4*a**2+2*abs(b)*(2*(x-points[0][0])+1)
            while y*ty<lim*ty:
                check()
=======

            # Значение а, предела, начальной ошибки, координаты начальной точки
            a=e_crd[0]-b_crd[0]
            lim=e_crd[1]
            delta=2*abs(b)-4*a**2
            x,y=b_crd

            # Обображение начальной точки
            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

            # Двигаемся по диагонали
            def deqz(x,y,delta):return x+1,y+ty,delta-4*a**2+2*abs(b)*(2*(x-b_crd[0])+1)

            # Отображение
            while y*ty<lim*ty:
>>>>>>> temp-branch

                if delta>0:

                    d=2*delta+4*a**2
<<<<<<< HEAD
                    if d>=0:
=======
                    if d>0:

                        # Двигаемся по вертикали
>>>>>>> temp-branch
                        y+=ty
                        delta=delta-4*a**2

                    else:x,y,delta=deqz(x,y,delta)
                elif delta<0:
<<<<<<< HEAD
                    d=2*delta-2*abs(b)*(2*(x-points[0][0])+1)
                    if d<0:
                        x+=1
                        delta=delta+2*abs(b)*(2*(x-points[0][0])+1)
=======

                    d=2*delta-2*abs(b)*(2*(x-b_crd[0])+1)
                    if d<=0:

                        # Двигаемся по горизонтали
                        x+=1
                        delta=delta+2*abs(b)*(2*(x-b_crd[0])+1)

>>>>>>> temp-branch
                    else:x,y,delta=deqz(x,y,delta)
                else:x,y,delta=deqz(x,y,delta)

                # Отображение полученных точек
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
<<<<<<< HEAD
                pg.draw.rect(display,BLACK,((points[0][0]-x+points[0][0])*PIXEL,y*PIXEL,PIXEL,PIXEL))
=======
                pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,y*PIXEL,PIXEL,PIXEL))

                # Отладка
                check()
>>>>>>> temp-branch
