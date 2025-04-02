from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

class Parab_alg(Line_Alg):
 
    def draw_line(self,points,check):

        # Получение заданных точек и значения b
        b_crd,e_crd=points
        b=e_crd[1]-b_crd[1]
        
        # Проверка валидности
        if b!=0:

            # Получение знака построения
            if b<0:ty=-1
            else:ty=1

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

                if delta>0:

                    d=2*delta+4*a**2
                    if d>0:

                        # Двигаемся по вертикали
                        y+=ty
                        delta=delta-4*a**2

                    else:x,y,delta=deqz(x,y,delta)
                elif delta<0:

                    d=2*delta-2*abs(b)*(2*(x-b_crd[0])+1)
                    if d<=0:

                        # Двигаемся по горизонтали
                        x+=1
                        delta=delta+2*abs(b)*(2*(x-b_crd[0])+1)

                    else:x,y,delta=deqz(x,y,delta)
                else:x,y,delta=deqz(x,y,delta)

                # Отображение полученных точек
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,y*PIXEL,PIXEL,PIXEL))

                # Отладка
                check()