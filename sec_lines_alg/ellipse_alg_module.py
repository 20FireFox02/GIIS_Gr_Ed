from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

class Ellipse_alg(Line_Alg):

    def draw_line(self,points,check):

        # Получение заданных точек и приращения
        b_crd,e_crd=points
        a=e_crd[0]-b_crd[0]
        b=e_crd[1]-b_crd[1]
        lim=b_crd[1]

        # Начальная ошибка и координаты начальной точки
        delta=a**2*(1-2*abs(b))+b**2
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
                if d<=0:

                    # Двигаемя по горизонтали
                    x+=1
                    delta=delta+b**2*(2*(x-b_crd[0])+1)
                    
                else:x,y,delta=deqz(x,y,delta)
            elif delta>0:

                d=2*delta-2*(x-b_crd[0])*b**2-1
                if d>0:

                    # Двигаемя по вертикали
                    y-=1
                    delta=delta+a**2*(-2*(y-b_crd[1])+1)

                else:x,y,delta=deqz(x,y,delta)
            else:x,y,delta=deqz(x,y,delta)

            # Отображение полученных точек
            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,(x*PIXEL,(b_crd[1]-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,(b_crd[1]-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,y*PIXEL,PIXEL,PIXEL))

            # Отладка
            check()